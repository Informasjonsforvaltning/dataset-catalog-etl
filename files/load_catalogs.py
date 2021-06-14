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

with open(args.outputdirectory + 'transformed_datasets.json') as catalogs_file:
    transformed_json = json.load(catalogs_file)

    total_updated = 0
    for mongo_id in transformed_json:
        to_be_updated = transformed_json[mongo_id]
        print(db.datasets.find_one_and_update({'_id': mongo_id},  {'$set': to_be_updated}))
        total_updated += 1
    print("Total number of catalogs updated: " + str(total_updated))
