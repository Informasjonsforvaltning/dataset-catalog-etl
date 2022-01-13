import json
import os
from pymongo import MongoClient
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()
connection = MongoClient(
    f"""mongodb://{os.environ['MONGO_USERNAME']}:{os.environ['MONGO_PASSWORD']}@mongodb:27017/datasetCatalog?authSource=admin&authMechanism=SCRAM-SHA-1""")

db = connection['datasetCatalog']
dataset_list = list(db.datasets.find())
datasets = {}
skipped_datasets = 0


def filter_legal_basis(legal_basis):
    filtered = []
    if legal_basis and len(legal_basis) > 0:
        for basis in legal_basis:
            uri = basis.get("uri")
            if uri and len(uri) > 0:
                filtered.append(basis)
    return filtered


for id_dict in dataset_list:
    accessRights = id_dict.get("accessRights")
    legalBasisForRestriction = filter_legal_basis(id_dict.get("legalBasisForRestriction"))
    legalBasisForProcessing = filter_legal_basis(id_dict.get("legalBasisForProcessing"))
    legalBasisForAccess = filter_legal_basis(id_dict.get("legalBasisForAccess"))

    if len(legalBasisForAccess) == 0 and len(legalBasisForProcessing) == 0 and len(legalBasisForRestriction) == 0:
        skipped_datasets += 1
    elif accessRights and accessRights.get("uri") and re.search("RESTRICTED$", accessRights):
        _id = id_dict["_id"]
        datasets[_id] = {}
        datasets[_id]["accessRights"] = accessRights
        datasets[_id]["legalBasisForRestriction"] = legalBasisForRestriction
        datasets[_id]["legalBasisForProcessing"] = legalBasisForProcessing
        datasets[_id]["legalBasisForAccess"] = legalBasisForAccess
    else:
        skipped_datasets += 1
print("Total number of datasets: " + str(len(dataset_list)))
print("Total number of extracted datasets: " + str(len(datasets)))
print("Total number of skipped datasets (no accessRights or legalBasis present): " + str(skipped_datasets))

with open(args.outputdirectory + 'mongo_datasets.json', 'w', encoding="utf-8") as outfile:
    json.dump(datasets, outfile, ensure_ascii=False, indent=4)
