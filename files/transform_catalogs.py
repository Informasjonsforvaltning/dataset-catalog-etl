import json
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()


def transform(inputfile, inputfile2):
    uris = openfile(inputfile)
    datasets = openfile(inputfile2)
    transformed_datasets = {}
    print("Total number of extracted uris: " + str(len(uris)))
    print("Total number of extracted datasets: " + str(len(datasets)))
    transformed_count = 0
    for dataset_key in datasets:
        transformed = transform_dataset(datasets[dataset_key], uris)
        if transformed:
            transformed_datasets[dataset_key] = transformed
            transformed_count += 1
    print("Total number of transformed datasets: " + str(transformed_count))
    return transformed_datasets


def transform_dataset(dataset, dataset_uris):
    transformed_references = []
    references = dataset.get("references")
    references = references if references else []
    for reference in references:
        source = reference.get("source")
        old_uri = source.get("uri") if source else None
        new_uri = dataset_uris.get(old_uri) if old_uri else None
        if new_uri:
            updated_reference = reference
            updated_reference["source"]["uri"] = new_uri
            transformed_references.append(updated_reference)
        else:
            transformed_references.append(reference)
    old_dataset_uri = dataset.get("uri")
    transformed_dataset = {}
    if len(transformed_references) > 0:
        transformed_dataset["references"] = transformed_references
    if old_dataset_uri:
        new_dataset_uri = dataset_uris.get(old_dataset_uri)
        if new_dataset_uri:
            transformed_dataset["uri"] = new_dataset_uri
    return transformed_dataset if len(transformed_dataset) > 0 else None


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


inputfileName = args.outputdirectory + "transformed_uris.json"
inputfileName2 = args.outputdirectory + "mongo_datasets.json"
outputfileName = args.outputdirectory + "transformed_datasets.json"


with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(inputfileName, inputfileName2), outfile, ensure_ascii=False, indent=4)
