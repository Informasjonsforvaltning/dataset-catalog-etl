import json
import os
from pymongo import MongoClient
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()
connection = MongoClient(
    f"""mongodb://{os.environ['MONGO_USERNAME']}:{os.environ['MONGO_PASSWORD']}@mongodb:27017/datasetCatalog?authSource=admin&authMechanism=SCRAM-SHA-1""")

db = connection['datasetCatalog']

dataset_list = list(db.datasets.find())
datasets = {}
skipped_datasets = 0
for id_dict in dataset_list:
    subject = id_dict.get("subject")
    if subject and len(subject) > 0:
        _id = id_dict["_id"]
        datasets[_id] = {}
        datasets[_id]["subject"] = subject
    else:
        skipped_datasets += 1
print("Total number of datasets: " + str(len(dataset_list)))
print("Total number of extracted datasets: " + str(len(datasets)))
print("Total number of skipped datasets (no subject present): " + str(skipped_datasets))

with open(args.outputdirectory + 'mongo_datasets.json', 'w', encoding="utf-8") as outfile:
    json.dump(datasets, outfile, ensure_ascii=False, indent=4)
