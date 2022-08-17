import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()


def transform(c_file, c_type):
    collection = openfile(c_file)
    transformed_collection = {}
    for key in collection:
        collection_publisher = collection[key].get("publisher")
        if iscataloguepublisher(collection_publisher):
            transformed_collection[key] = collection[key]
            transformed_publisher = collection_publisher
            transformed_publisher["uri"] = transformuri(collection_publisher.get("uri"))
            transformed_collection[key]["publisher"] = transformed_publisher
    print("Total number of transformed " + c_type + ": " + str(len(transformed_collection)))
    return transformed_collection


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


def iscataloguepublisher(publisher):
    if publisher:
        uri = publisher.get("uri")
        return "catalogue" in uri if uri else False
    else:
        return False


def transformuri(uri):
    return uri.replace("catalogue","catalog")


datasets_file = args.outputdirectory + "mongo_datasets.json"
outputfileName = args.outputdirectory + "transformed_datasets.json"
with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(datasets_file, "datasets"), outfile, ensure_ascii=False, indent=4)

catalogs_file = args.outputdirectory + "mongo_catalogs.json"
outputfileName = args.outputdirectory + "transformed_catalogs.json"
with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(catalogs_file, "catalogs"), outfile, ensure_ascii=False, indent=4)
