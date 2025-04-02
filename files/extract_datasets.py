import json
import os
from pymongo import MongoClient
import argparse
from datetime import datetime


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


parser = argparse.ArgumentParser()
parser.add_argument('-o',
                    '--outputdirectory',
                    help="the path to the directory of the output files",
                    required=True)
args = parser.parse_args()
connection = MongoClient(
    f"""mongodb://{input("Username: ")}:{input("Password: ")}@localhost:27017/datasetCatalog?authSource=admin&authMechanism=SCRAM-SHA-1""")

db = connection["datasetCatalog"]

with open(args.outputdirectory + 'mongo_datasets.json', 'w', encoding="utf-8") as outfile:
    json.dump(list(db.datasets.find()), outfile, cls=DateTimeEncoder, ensure_ascii=False, indent=4)
