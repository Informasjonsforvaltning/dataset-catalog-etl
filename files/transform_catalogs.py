import json
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()
new_base_uri = os.environ['FDK_REGISTRATION_BASE_URI']


def transform(inputfile):

    catalogs = openfile(inputfile)
    transformed_catalogs = {}
    print("Total number of extracted catalogs: " + str(len(catalogs)))
    for catalog_key in catalogs:
        catalogs[catalog_key].get("_id")
        transformed_uri = transform_uri(catalogs[catalog_key].get("uri"))
        transformed_catalogs[catalog_key] = {"uri": transformed_uri}
    return transformed_catalogs


def transform_uri(uri):
    str_spl = uri.split('catalogs/')
    return new_base_uri + '/catalogs/' + str_spl[-1]


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


inputfileName = args.outputdirectory + "mongo_catalogs.json"
outputfileName = args.outputdirectory + "catalogs_transformed.json"


with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(inputfileName), outfile, ensure_ascii=False, indent=4)
