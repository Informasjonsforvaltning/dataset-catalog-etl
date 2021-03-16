import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()


def transform(inputfile):

    datasets = openfile(inputfile)

    transformed = {}
    for dataset in datasets:
        transformed_dataset = {}
        if dataset["downloadURL"] is not None:
            transformed_dataset["downloadURL"] = fix_url_list(dataset["downloadURL"])
        if dataset["accessURL"] is not None:
            transformed_dataset["accessURL"] = fix_url_list(dataset["accessURL"])
        if dataset["conformsTo"] is not None:
            transformed_dataset["conformsTo"] = fix_conforms_to_list(dataset["conformsTo"])
        transformed[dataset["_id"]] = dataset
    return transformed


def fix_url(url):
    new_url = 'https' + url[4:]
    return new_url


def fix_conforms_to_list(conforms_list):
    new_list = []
    for conforms in conforms_list:
        url = conforms.get("uri")
        fixed_conforms = conforms
        if url and len(url) > 13 and url[:13] == 'http://hotell':
            fixed_conforms["uri"] = fix_url(url)
        new_list.append(fixed_conforms)
    return new_list


def fix_url_list(url_list):
    new_list = []
    for url in url_list:
        if len(url) > 13 and url[:13] == 'http://hotell':
            new_list.append(fix_url(url))
        else:
            new_list.append(url)
    return new_list


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


inputfileName = args.outputdirectory + "mongo_datasets.json"
outputfileName = args.outputdirectory + "datasets_transformed.json"


with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(inputfileName), outfile, ensure_ascii=False, indent=4)
