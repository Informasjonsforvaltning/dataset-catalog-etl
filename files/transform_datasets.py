import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()


def transform(datasets_file, concepts_file):
    datasets = openfile(datasets_file)
    concepts_meta = openfile(concepts_file)
    transformed_datasets = {}
    count_modified = 0
    for dataset_key in datasets:
        concepts = datasets[dataset_key]["concepts"]
        modified_concepts = []
        for concept in concepts:
            if concept["identifier"] is not None:
                old_uri = concept["uri"]
                fdk_id = old_uri.split("/")[-1]
                modified_concept = concept
                new_concept_uri = concepts_meta.get(fdk_id)
                if new_concept_uri is not None:
                    modified_concept["uri"] = concepts_meta[fdk_id]
                else:
                    modified_concept["uri"] = concept["identifier"]
                modified_concepts.append(modified_concept)
                count_modified += 1
                print("Old concept uri: " + old_uri + " -------- " + "New concept uri: " + modified_concept["uri"])
            else:
                modified_concepts.append(concept)
        transformed_datasets[dataset_key] = datasets[dataset_key]
        transformed_datasets[dataset_key]["concepts"] = modified_concepts
    return transformed_datasets


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


datasetfileName = args.outputdirectory + "mongo_datasets.json"
conceptfileName = args.outputdirectory + "mongo_concepts.json"
outputfileName = args.outputdirectory + "datasets_transformed.json"


with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(datasetfileName, conceptfileName), outfile, ensure_ascii=False, indent=4)

