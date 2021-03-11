import json
import urllib.request
import argparse
import re
import os

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()

catalogs = "./tmp/catalogs.json"
match_string = '\d{9}$'
match_string_json = '(\d{9}).json$'
environment = '' if os.environ['NAMESPACE'] == 'prod' else '.' + os.environ['NAMESPACE']
orgcat_uri = 'https://organization-catalogue' + environment + '.fellesdatakatalog.digdir.no/organizations/'


def getPublisherId(publisher):
    if publisher.get('id'):
        ids = re.findall(match_string, publisher['id'])
        if len(ids) > 0:
            return ids[0]
    if publisher.get('uri'):
        ids = re.findall(match_string, publisher['uri'])
        if len(ids) > 0:
            return ids[0]
        ids = re.findall(match_string_json, publisher['uri'])
        if len(ids) > 0:
            return ids[0]
    return None


with open(catalogs) as catalog_file:
    embedded = json.load(catalog_file).get("_embedded")
    data = embedded.get("catalogs") if embedded else []

    for catalog in data:
        orgId = catalog['id']
        transformed = []

        with open(f'./tmp/datasets-'+orgId+'.json') as dataset_file:
            embedded = json.load(dataset_file).get("_embedded")
            datasets = embedded.get("datasets") if embedded else []

            for dataset in datasets:
                updated_publisher = dataset.get('publisher')
                publisher_id = getPublisherId(updated_publisher)
                if publisher_id:
                    updated_publisher['id'] = publisher_id
                    updated_publisher['uri'] = orgcat_uri + publisher_id
                else:

                    updated_publisher = {'uri': orgcat_uri + orgId, 'id': orgId}
                    print(f'No publisher ID found: {orgId} - ' + dataset.get('id'))

                dataset["publisher"] = updated_publisher
                transformed.append(dataset)

            with open(args.outputdirectory + 'transformed_datasets_' + orgId + '.json', 'w', encoding="utf-8") as outfile:
                json.dump(transformed, outfile, ensure_ascii=False, indent=4)
