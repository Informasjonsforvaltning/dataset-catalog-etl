import json
import os
from pymongo import MongoClient
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()
connection = MongoClient(
    f"""mongodb://{os.environ['MONGO_USERNAME']}:{os.environ['MONGO_PASSWORD']}@mongodb:27017/dataServiceHarvester?authSource=admin&authMechanism=SCRAM-SHA-1""")

db = connection.dataServiceHarvester
dict_list = list(db.dataserviceMeta.find())
dataservices = {}
for id_dict in dict_list:
    dataservice = {"uri": id_dict["_id"], "fdkId": id_dict["fdkId"]}
    dataservices[id_dict["fdkId"]] = dataservice

with open(args.outputdirectory + 'mongo_dataservices.json', 'w', encoding="utf-8") as outfile:
    json.dump(dataservices, outfile, ensure_ascii=False, indent=4)
