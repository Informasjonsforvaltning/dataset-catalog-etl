import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()


def transform(inputfile):

    datasets = openfile(inputfile)
    transformed_datasets = {}
    count_objective = 0
    count_transformed = 0
    print("Total number of extracted datasets: " + str(len(datasets)))
    for dataset_key in datasets:
        transformed_description = None
        if datasets[dataset_key].get("objective"):
            count_objective += 1
            transformed_description = desc_dict(datasets[dataset_key])
        transformed_datasets[dataset_key] = {"description": transformed_description}
    print("Number of datasets w/objectives found: " + str(count_objective))
    return transformed_datasets


def desc_dict(str_dict):
    description = str_dict.get("description")
    description = description if description else {}
    return_dict = description
    for key in str_dict["objective"]:
        if key == "en":
            connection_string = """


Objective
"""
        else:
            connection_string = """


Formål
"""
        description_key_str = description.get(key)
        description_key_str = description_key_str if description_key_str else ""
        return_dict[key] = description_key_str + connection_string + str_dict["objective"][key]
    return return_dict


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


inputfileName = args.outputdirectory + "mongo_datasets.json"
outputfileName = args.outputdirectory + "datasets_transformed.json"


with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(inputfileName), outfile, ensure_ascii=False, indent=4)
