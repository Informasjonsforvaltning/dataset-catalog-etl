import json
import os
from pymongo import MongoClient
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o',
                    '--outputdirectory',
                    help="the path to the directory of the output files",
                    required=True)
args = parser.parse_args()
connection = MongoClient(
    f"""mongodb://{input("Username: ")}:{input("Password: ")}@localhost:27017/datasetCatalog?authSource=admin&authMechanism=SCRAM-SHA-1""")

db = connection["datasetCatalog"]
datasets = {}
dict_list = list(db.datasets.find({"concepts.identifier": {"$exists": "true"}}))
for id_dict in dict_list:
    id_str = id_dict["_id"]
    datasets[id_str] = {}
    datasets[id_str]["concepts"] = id_dict.get("concepts")
print("Total number of extracted datasets: " + str(len(datasets)))

with open(args.outputdirectory + 'mongo_datasets.json', 'w', encoding="utf-8") as outfile:
    json.dump(datasets, outfile, ensure_ascii=False, indent=4)

db = connection["conceptHarvester"]
concepts = {}
dict_list = list(db.conceptMeta.find())
for id_dict in dict_list:
    id_str = id_dict["fdkId"]
    concepts[id_str] = id_dict["_id"]
print("Total number of extracted concepts: " + str(len(concepts)))

with open(args.outputdirectory + 'mongo_concepts.json', 'w', encoding="utf-8") as outfile:
    json.dump(concepts, outfile, ensure_ascii=False, indent=4)
