import json
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()


def transform(inputfile, inputfile2):
    dataservices = openfile(inputfile)
    datasets = openfile(inputfile2)
    transformed_datasets = {}
    print("Total number of extracted dataservices: " + str(len(dataservices)))
    print("Total number of extracted datasets: " + str(len(datasets)))
    transformed_count = 0
    for dataset_key in datasets:
        transformed = transform_dataset(datasets[dataset_key], dataservices)
        if transformed:
            transformed_datasets[dataset_key] = transformed
            transformed_count += 1
    print("Total number of transformed datasets: " + str(transformed_count))
    return transformed_datasets


def transform_dataset(dataset, dataservices):
    distribution = dataset.get("distribution")
    distribution = distribution if distribution else []
    modified_distributions = []
    for dist in distribution:
        access_service = dist.get("accessService")
        access_service = access_service if access_service else []
        modified_services = []
        for service in access_service:
            fdk_id = service.get("_id")
            dataservice = dataservices.get(fdk_id)
            if dataservice:
                modified_service = service
                modified_service["uri"] = dataservice.get("uri")
                modified_services.append(modified_service)
            else:
                modified_services.append(service)
        modified_distribution = dist
        modified_distribution["accessService"] = modified_services
        modified_distributions.append(modified_distribution)
    transformed_dataset = {}
    if len(modified_distributions) > 0:
        transformed_dataset["distribution"] = modified_distributions
    return transformed_dataset if len(transformed_dataset) > 0 else None


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


inputfileName = args.outputdirectory + "mongo_dataservices.json"
inputfileName2 = args.outputdirectory + "mongo_datasets.json"
outputfileName = args.outputdirectory + "transformed_datasets.json"


with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(inputfileName, inputfileName2), outfile, ensure_ascii=False, indent=4)
