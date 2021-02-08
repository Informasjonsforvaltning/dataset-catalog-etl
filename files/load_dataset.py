import json
import os
from pymongo import MongoClient
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()
connection = MongoClient(
    f"""mongodb://{os.environ['MONGO_USERNAME']}:{os.environ['MONGO_PASSWORD']}@mongodb:27017/datasetCatalog?authSource=admin&authMechanism=SCRAM-SHA-1""")
db = connection.datasetCatalog

with open(args.outputdirectory + 'dataset.json') as dataset_file:
    dataset_json = json.load(dataset_file)
    for dataset in dataset_json:
        print("To be inserted: " + str(dataset))
        print(db.datasets.insert({"_id": dataset["_id"],
                                  "catalogId": dataset["catalogId"],
                                  "lastModified": dataset["lastModified"],
                                  "registrationStatus": dataset["registrationStatus"],
                                  "concepts": dataset["concepts"],
                                  "subject": dataset["subject"],
                                  "uri": dataset["uri"],
                                  "title": dataset["title"],
                                  "description": dataset["description"],
                                  "objective": dataset["objective"],
                                  "contactPoint": dataset["contactPoint"],
                                  "keyword": dataset["keyword"],
                                  "publisher": dataset["publisher"],
                                  "language": dataset["language"],
                                  "landingPage": dataset["landingPage"],
                                  "theme": dataset["theme"],
                                  "distribution": dataset["distribution"],
                                  "sample": dataset["sample"],
                                  "temporal": dataset["temporal"],
                                  "spatial": dataset["spatial"],
                                  "accessRights": dataset["accessRights"],
                                  "legalBasisForRestriction": dataset["legalBasisForRestriction"],
                                  "legalBasisForProcessing": dataset["legalBasisForProcessing"],
                                  "legalBasisForAccess": dataset["legalBasisForAccess"],
                                  "provenance": dataset["provenance"],
                                  "identifier": dataset["identifier"],
                                  "accrualPeriodicity": dataset["accrualPeriodicity"],
                                  "conformsTo": dataset["conformsTo"],
                                  "informationModel": dataset["informationModel"],
                                  "type": dataset["type"],
                                  "_class": dataset["_class"]
                                  }))
