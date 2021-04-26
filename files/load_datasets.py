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

with open(args.outputdirectory + 'datasets_transformed.json') as datasets_file:
    transformed_json = json.load(datasets_file)

    for mongo_id in transformed_json:
        to_be_updated = transformed_json[mongo_id]
        if to_be_updated and to_be_updated.get('description'):
            print("Mongo_id: " + mongo_id + " || To be updated: " + str(to_be_updated))
            print(db.datasets.find_one_and_update({'_id': mongo_id},  {'$set': to_be_updated}))
        print(db.datasets.find_one_and_update({'_id': mongo_id}, {'$unset': {"objective": "", "accessRightsComment": "", "descriptionFormatted": ""}}))
