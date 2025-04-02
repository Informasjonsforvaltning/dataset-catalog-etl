import json
import os
from pymongo import MongoClient
import argparse
from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()
connection = MongoClient(
    f"""mongodb://{input("Username: ")}:{input("Password: ")}@localhost:27017/datasetCatalog?authSource=admin&replicaSet={input("Replicaset: ")}&directConnection=true""")
dataset_date_fields = ["created", "lastModified", "issued", "temporal.startDate", "temporal.endDate", "modified"]

def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


def convert_date_fields_to_datetime(doc, date_fields):
    for field in date_fields:
        keys = field.split(".")
        current_level = doc
        for key in keys[:-1]:
            if key in current_level and isinstance(current_level[key], dict):
                current_level = current_level[key]
            else:
                current_level = None
                break
        if current_level and keys[-1] in current_level and isinstance(current_level[keys[-1]], str):
            try:
                current_level[keys[-1]] = datetime.fromisoformat(current_level[keys[-1]])
            except ValueError:
                pass
    return doc


def load_datasets(datasets):
    processed_datasets = [
        convert_date_fields_to_datetime(doc, dataset_date_fields) for doc in datasets
    ]
    db = connection["datasetCatalog"]
    if len(processed_datasets) > 0:
        print("---\nStarting to load datasetCatalog...")
        result = db.datasets.insert_many(processed_datasets)
        print(f"Successfully inserted {len(result.inserted_ids)}/{len(processed_datasets)} datasets.")


load_datasets(openfile(args.outputdirectory + "datasets_transformed.json"))
