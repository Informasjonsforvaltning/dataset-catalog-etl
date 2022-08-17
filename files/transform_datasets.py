import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()


def transform(d_file):
    datasets = openfile(d_file)
    transformed_datasets = {}
    for dataset_key in datasets:
        dataset_publisher = datasets[dataset_key].get("publisher")
        if iscataloguepublisher(dataset_publisher):
            transformed_datasets[dataset_key] = datasets[dataset_key]
            transformed_publisher = dataset_publisher
            transformed_publisher["uri"] = transformuri(dataset_publisher.get("uri"))
            transformed_datasets[dataset_key]["publisher"] = transformed_publisher
    print("Total number of transformed datasets: " + str(len(transformed_datasets)))
    return transformed_datasets


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


def iscataloguepublisher(publisher):
    if publisher:
        uri = publisher.get("uri")
        return "catalogue" in uri if uri else False
    else:
        return False


def transformuri(uri):
    return uri.replace("catalogue","catalog")


datasets_file = args.outputdirectory + "mongo_datasets.json"
outputfileName = args.outputdirectory + "transformed_datasets.json"


with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(datasets_file), outfile, ensure_ascii=False, indent=4)
