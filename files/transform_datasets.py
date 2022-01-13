import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()


def transform(d_file):
    datasets = openfile(d_file)
    transformed_datasets = {}
    non_public = {"accessRights": {"uri": "http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC"}}
    for dataset_key in datasets:
        transformed_datasets[dataset_key] = non_public
    print("Total number of transformed datasets: " + str(len(transformed_datasets)))
    return transformed_datasets


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


datasets_file = args.outputdirectory + "mongo_datasets.json"
outputfileName = args.outputdirectory + "transformed_datasets.json"


with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(datasets_file), outfile, ensure_ascii=False, indent=4)
