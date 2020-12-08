import json
import requests
from pathlib import Path
import os

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()

inputfileName = "./tmp/catalogs.json"
error_file = open('./tmp/extract_datasets_errors.txt', 'w')
token_file = open('./tmp/token.txt')

token = [line.rstrip('\n') for line in token_file]

with open(inputfileName) as catalog_file:
    count = 0
    embedded = json.load(catalog_file).get("_embedded")
    data = embedded.get("catalogs") if embedded else []

    for catalog in data:
        orgId = catalog['id']
        datasetsURI = 'http://dataset-catalogue:8080/catalogs/' + orgId + '/datasets' + '?size=1000'

        try:
            r = requests.get(datasetsURI, headers={'accept': 'application/json','Authorization': 'Bearer ' + token})

            with open(args.outputdirectory + 'datasets_' + orgId + '.json', 'w', encoding="utf-8") as outfile:
                json.dump(r.json(), outfile, ensure_ascii=False, indent=4)
        except requests.HTTPError as err:
            print(f'{err}' + ': ' + catalog['id'].get("nb"))
            # error_file.write(f'{err}')
