import json
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()
old_base_uri = os.environ['OLD_BASE_URI']
new_base_uri = os.environ['NEW_BASE_URI']
really_old_base_uri = os.environ['REALLY_OLD_BASE_URI']


def transform(d_file):
    datasets = openfile(d_file)
    transformed_datasets = {}
    transformed_count = 0
    failed_count = 0
    failed = {}
    for dataset_key in datasets:
        result = transform_dataset(datasets[dataset_key])
        if result["transformed"]:
            transformed_datasets[dataset_key] = result["transformed"]
            transformed_count += 1
        else:
            failed[dataset_key] = datasets[dataset_key]
            failed_count += 1
    print("Total number of transformed datasets: " + str(transformed_count))
    print("Total number of non-transformed datasets: " + str(failed_count))
    with open(args.outputdirectory + "not_transformed.json", 'w', encoding="utf-8") as err_file:
        json.dump(failed, err_file, ensure_ascii=False, indent=4)
    return transformed_datasets


def transform_dataset(dataset):
    subjects = dataset.get("subject")
    modified_subjects = []
    has_been_modified = False
    for subject in subjects:
        modified_url = replace_url(subject.get("identifier"))
        if modified_url:
            has_been_modified = True
            modified_subject = subject
            modified_subject["identifier"] = modified_url
            modified_subjects.append(modified_subject)
        else:
            modified_subjects.append(subject)
    if has_been_modified:
        transformed_dataset = {"subject": modified_subjects}
        return {"transformed": transformed_dataset}
    else:
        return {"transformed": None}


def replace_url(url):
    if old_base_uri in url:
        return url.replace(old_base_uri, f'{new_base_uri}/collections')
    elif really_old_base_uri in url:
        return url.replace(really_old_base_uri, f'{new_base_uri}/collections')
    return None


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


datasets_file = args.outputdirectory + "mongo_datasets.json"
outputfileName = args.outputdirectory + "transformed_datasets.json"


with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(datasets_file), outfile, ensure_ascii=False, indent=4)
