import json
import requests

import argparse
token_file = open('./tmp/token.txt')
# output_file = open('./tmp/datasets.json', 'w')
catalogs = "./tmp/catalogs.json"

token = str([line.rstrip('\n') for line in token_file][0])
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()

with open(catalogs) as catalog_file:

    embedded = json.load(catalog_file).get("_embedded")
    data = embedded.get("catalogs") if embedded else []

    for catalog in data:
        orgId = catalog['id']

        url = 'http://dataset-catalog:8080/catalogs/' + orgId + '/datasets'
        headers = {'Accept': 'application/json', 'Authorization': 'Bearer ' + token}
        print("Getting the following url: ", url)

        with open(f'./tmp/datasets-{orgId}.json', 'w') as output_file:

            try:
                rsp = requests.get(url, headers=headers)
                rsp.raise_for_status()
                output_file.write(rsp.text)

            except requests.HTTPError as err:
                print(f'{err}')
