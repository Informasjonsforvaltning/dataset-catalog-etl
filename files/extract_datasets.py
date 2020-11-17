import json
import requests
import os

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()

inputfileName = "catalogs.json"
error_file = open('./tmp/extract_datasets_errors.txt', 'w')

with open(inputfileName) as catalog_file:
    count = 0
    data = json.load(catalog_file)["_embedded"]["catalogs"]
    for catalog in data:
        datasetsURI = 'http://dataset-catalogue:8080/catalogs/' + catalog['id'] + '/datasets'

        try:
            r = requests.get(datasetsURI, headers={'accept': 'application/json'})

            with open('datasets_' + catalog['id'] + '.json', 'w', encoding="utf-8") as outfile:
                json.dump(r.json(), outfile, ensure_ascii=False, indent=4)
        except requests.HTTPError as err:
            print(f'{err}' + ': ' + catalog['id'].get("nb"))
            # error_file.write(f'{err}')


