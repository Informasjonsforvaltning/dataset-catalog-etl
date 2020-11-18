import json
import urllib.request
import argparse
import re


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()


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
                transformed = []

                for dataset in data_datasets:
                    dataset["_lastModified"] = re.sub(""".0000$""", "", dataset['_lastModified'])

                    issued = dataset.get("issued")
                    if issued:
                        dataset['issued'] = re.sub(""".0000$""", "", dataset['issued'])

                    modified = dataset.get("modified")
                    if modified:
                        dataset["modified"] = re.sub(""".0000$""", "", dataset['modified'])

                    transformed.append(dataset)

                with open(args.outputdirectory + 'transformed_datasets_' + orgId + '.json', 'w', encoding="utf-8") as outfile:
                    json.dump(transformed, outfile, ensure_ascii=False, indent=4)

        except BaseException as err:
            print(f'{orgId} - {err}')
