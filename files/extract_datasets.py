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
    _id = id_dict["_id"]
    publishers = id_dict.get("publishers")
    datasets[_id] = {}
    datasets[_id]["publishers"] = publishers

print("Total number of datasets: " + str(len(dataset_list)))
print("Total number of extracted datasets: " + str(len(datasets)))

with open(args.outputdirectory + 'mongo_datasets.json', 'w', encoding="utf-8") as outfile:
    json.dump(datasets, outfile, ensure_ascii=False, indent=4)
