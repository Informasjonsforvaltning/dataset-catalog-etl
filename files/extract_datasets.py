import json
import os
from pymongo import MongoClient
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()
connection = MongoClient(
    f"""mongodb://{os.environ['MONGO_USERNAME']}:{os.environ['MONGO_PASSWORD']}@mongodb:27017/datasetCatalog?authSource=admin&authMechanism=SCRAM-SHA-1""")


def extract(collection):
    db = connection['datasetCatalog']
    extract_list = []
    if collection == "datasets":
        extract_list = list(db.datasets.find())
    extracted_dicts = {}

    for id_dict in extract_list:
        _id = id_dict["_id"]
        distribution = id_dict.get("distribution")
        extracted_dicts[_id] = {}
        extracted_dicts[_id]["distribution"] = distribution

    print("Total number of " + collection + ": " + str(len(extract_list)))
    print("Total number of extracted " + collection + ": " + str(len(extracted_dicts)))
    return extracted_dicts


with open(args.outputdirectory + 'mongo_datasets.json', 'w', encoding="utf-8") as outfile:
    json.dump(extract("datasets"), outfile, ensure_ascii=False, indent=4)

