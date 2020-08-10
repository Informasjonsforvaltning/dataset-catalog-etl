import csv
import json
import requests
import sys

import argparse

from rdflib import Graph, URIRef, Literal, XSD
from rdflib.namespace import FOAF, RDF, DCTERMS
import logging

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()


datasetsGraph = None
with open("fuseki_datasets.ttl") as fuseki_file:
    datasetsGraph = Graph().parse(data=fuseki_file.read(), format='turtle')
metabaseURI = 'https://datasets.fellesdatakatalog.digdir.no/datasets/'
catalogrecordRef = URIRef("http://www.w3.org/ns/dcat#CatalogRecord")
fusekibaseURI = 'http://fdk-fuseki-service:8080/fuseki/dataset-meta'

inputfileName = args.outputdirectory + "datasets_metadata.json"

with open(inputfileName) as json_file:

    data = json.load(json_file)
    # Load the publisher by posting the data:
    totalLoaded = 0
    totalFailed = 0
    for dataset in data:
        elasticID = dataset["doc"]["id"]
        elasticURI = dataset["doc"]["uri"]
        elasticFirst = dataset["doc"]["harvest"]["firstHarvested"]
        elasticLast = dataset["doc"]["harvest"]["lastHarvested"]
        elasticChanged = dataset["doc"]["harvest"]["changed"]

        for recordURI in datasetsGraph.subjects(
                predicate=RDF.type, object=catalogrecordRef
        ):
            primaryTopicURI = datasetsGraph.value(recordURI, FOAF.primaryTopic)
            if primaryTopicURI and primaryTopicURI.toPython() == elasticURI:
                g = Graph()
                resourceURI = URIRef(metabaseURI + elasticID)
                partOfURI = datasetsGraph.value(recordURI, DCTERMS.isPartOf)
                g.resource(resourceURI)
                g.add((resourceURI, RDF.type, catalogrecordRef))
                g.add((resourceURI, DCTERMS.identifier, Literal(elasticID)))
                g.add((resourceURI, DCTERMS.isPartOf, partOfURI))
                g.add((resourceURI, DCTERMS.issued, Literal(elasticFirst, datatype=XSD.dateTime)))
                for date in elasticChanged:
                    g.add((resourceURI, DCTERMS.modified, Literal(date, datatype=XSD.dateTime)))
                g.add((resourceURI, FOAF.primaryTopic, URIRef(elasticURI)))
                identifier = datasetsGraph.value(recordURI, DCTERMS.identifier)

                try:
                    response = requests.put(
                        fusekibaseURI + '?graph=' + elasticID, data=g.serialize(), headers={"Content-type": "application/rdf+xml"}  # , cookies=cookies
                    )
                    response.raise_for_status()
                    print("Response.status: " + str(response.status_code) + " -- " + elasticURI)
                    if response.status_code == "201":
                        totalLoaded += 1
                    try:
                        response = requests.delete(
                            fusekibaseURI + '?graph=' + identifier  # , cookies=cookies
                        )
                        response.raise_for_status()
                        print("Delete response.status: " + str(response.status_code) + " -- " + elasticURI)
                    except requests.HTTPError as err:
                        logging.error(f'Http delete error response from reference-data: ({err})')
                    except Exception as err:
                        logging.error(f"Error occured when deleting data from reference-data: ({err})")
                except requests.HTTPError as err:
                    logging.error(f"Http error response from reference-data: ({err})")
                except Exception as err:
                    logging.error(f"Error occured when getting data from reference-data: ({err})")
