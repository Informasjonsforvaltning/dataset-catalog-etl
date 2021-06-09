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
dict_list = list(db.catalogs.find())
catalogs = {}
for id_dict in dict_list:
    id_str = id_dict["_id"]
    catalogs[id_str] = {}
    catalogs[id_str]["uri"] = id_dict.get("uri")
    catalogs[id_str]["references"] = id_dict.get("references")
print("Total number of extracted catalogs: " + str(len(catalogs)))

with open(args.outputdirectory + 'mongo_catalogs.json', 'w', encoding="utf-8") as outfile:
    json.dump(catalogs, outfile, ensure_ascii=False, indent=4)
