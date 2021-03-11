import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()


def transform(inputfile):

    datasets = openfile(inputfile)

    transformed = {}
    for dataset in datasets:
        if dataset["downloadURL"] is not None and dataset["downloadURL"][0][:13] == 'http://hotell':
            dataset["downloadURL"][0] = fix_url(dataset["downloadURL"][0])
        if dataset["accessURL"] is not None and dataset["accessURL"][0][:13] == 'http://hotell':
            dataset["accessURL"][0] = fix_url(dataset["accessURL"][0])
        if dataset["conformsTo"] is not None and dataset["conformsTo"][0][:13] == 'http://hotell':
            dataset["conformsTo"][0] = fix_url(dataset["conformsTo"][0])
        transformed[dataset["_id"]] = dataset
    return transformed


def fix_url(url):
    new_url = 'https' + url[4:]
    return new_url


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


inputfileName = args.outputdirectory + "mongo_datasets.json"
outputfileName = args.outputdirectory + "datasets_transformed.json"


with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(inputfileName), outfile, ensure_ascii=False, indent=4)
