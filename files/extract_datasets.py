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
    downloadURL = id_dict["downloadURL"] if id_dict.get("downloadURL") else None
    accessURL = id_dict["accessURL"] if id_dict.get("accessURL") else None
    conformsTo = id_dict["conformsTo"] if id_dict.get("conformsTo") else None
    datasets[id_str] = id_str
    print(str(downloadURL))
    print(str(accessURL))
    print(str(conformsTo))
    if downloadURL:
        datasets[downloadURL[0]] = downloadURL[0]
    if accessURL:
        datasets[accessURL[0]] = accessURL[0]
    if conformsTo:
        datasets[conformsTo[0]] = conformsTo[0]


with open(args.outputdirectory + 'mongo_datasets.json', 'w', encoding="utf-8") as outfile:
    json.dump(datasets, outfile, ensure_ascii=False, indent=4)

