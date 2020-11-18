import json
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()

output_file = open('./tmp/load_catalogs_output.txt', 'w')
error_file = open('./tmp/load_catalogs_errors.txt', 'w')

catalogs = "./tmp/catalogs.json"
url = 'http://dataset-catalog:8080/catalogs'

with open(catalogs) as catalog_file:
    count = 0
    embedded = json.load(catalog_file).get("_embedded")
    data = embedded.get("catalogs") if embedded else []

    try:
        for catalog in data:
            orgId = catalog['id']
            print("Posting to the following url: ", url)
            # Load the publisher by posting the data:
            try:
                rsp = requests.post(url, catalog, headers={'content-type': 'application/json', 'accept': 'application/json'})
                rsp.raise_for_status()
                output_file.write(f'{rsp.status_code}' + ': ' + catalog + "\n")

            except requests.HTTPError as err:
                print(f'{err}' + ': ' + orgId)
                error_file.write(f'{err}' + ': ' + catalog + "\n")

    except BaseException as err:
        print(f'{orgId} - {err}')
