import json
import urllib.request
import argparse
import requests


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()

output_file = open('./tmp/load_datasets_output.txt', 'w')
error_file = open('./tmp/load_datasets_errors.txt', 'w')

catalogs = "./tmp/catalogs.json"

with open(catalogs) as catalog_file:
    count = 0
    embedded = json.load(catalog_file).get("_embedded")
    data = embedded.get("catalogs") if embedded else []

    for catalog in data:
        orgId = catalog['id']

        try:

            inputfileName = args.outputdirectory + "datasets_" + orgId + ".json"
            with open(inputfileName) as json_file:
                count = 0
                embedded_datasets = json.load(json_file).get("_embedded")
                data_datasets = embedded_datasets.get("datasets") if embedded_datasets else []

                for dataset in data_datasets:
                    uploadUrl = 'http://dataset-catalog:8080/catalogs/' + orgId + '/datasets'

                    json_data = json.dumps(dataset)

                    try:
                        rsp = requests.post(uploadUrl, json_data, headers={'content-type': 'application/json', 'accept': 'application/json'})
                        rsp.raise_for_status()
                        output_file.write(f'{rsp.status_code}' + ': ' + json_data + "\n")

                    except requests.HTTPError as err:
                        print(f'{err}' + ': ' + dataset["title"].get("nb"))
                        error_file.write(f'{err}' + ': ' + json_data + "\n")
        except BaseException as err:
            print(f'{orgId} - {err}')
