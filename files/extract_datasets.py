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
    dataset = {}
    id_str = id_dict["_id"]
    dataset["_id"] = id_str
    downloadURL = id_dict.get("downloadURL")
    accessURL = id_dict.get("accessURL")
    conformsTo = id_dict.get("conformsTo")
    if downloadURL:
        dataset["downloadURL"] = downloadURL
    if accessURL:
        dataset["accessURL"] = accessURL
    if conformsTo:
        dataset["conformsTo"] = conformsTo
    datasets[id_str] = dataset


with open(args.outputdirectory + 'mongo_datasets.json', 'w', encoding="utf-8") as outfile:
    json.dump(datasets, outfile, ensure_ascii=False, indent=4)

