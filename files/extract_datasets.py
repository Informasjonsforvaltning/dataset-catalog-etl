import json
import os
from pymongo import MongoClient
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()
connection = MongoClient(
    f"""mongodb://{os.environ['MONGO_USERNAME']}:{os.environ['MONGO_PASSWORD']}@mongodb:27017/datasetCatalog?authSource=admin&authMechanism=SCRAM-SHA-1""")

db = connection.datasetCatalog
dict_list = list(db.datasets.find())
datasets = {}
for id_dict in dict_list:
    id_str = id_dict["_id"]
    downloadURL = id_dict["downloadURL"] if not None else None
    accessURL = id_dict["accessURL"] if not None else None
    conformsTo = id_dict["conformsTo"] if not None else None
    datasets["_id"] = id_str
    datasets["_id"].append(downloadURL)
    datasets["_id"].append(downloadURL)
    datasets["_id"].append(downloadURL)


with open(args.outputdirectory + 'mongo_datasets.json', 'w', encoding="utf-8") as outfile:
    json.dump(datasets, outfile, ensure_ascii=False, indent=4)

