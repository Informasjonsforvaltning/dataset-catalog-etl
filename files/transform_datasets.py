import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()


def transform(c_file, c_type):
    collection = openfile(c_file)
    transformed_collection = {}
    for key in collection:
        transformed_collection[key] = collection[key]
        collection_distributions = collection[key].get("distribution")
        transformed_distribution = []
        if collection_distributions:
            for dist in collection_distributions:
                old_dist = dist
                dist_license = dist.get("license")
                dist_uri = None
                if dist_license:
                    dist_uri = dist_license.get("uri")
                if dist_uri:
                    old_dist["license"]["uri"] = transform_uri(dist_uri)
                    transformed_distribution.append(old_dist)
                else:
                    transformed_distribution.append(dist)
            transformed_collection[key]["distribution"] = transformed_distribution
    print("Total number of transformed " + c_type + ": " + str(len(transformed_collection)))
    return transformed_collection


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


def transform_uri(uri):
    if "creativecommons.org/licenses/by/4.0" in uri:
        return "http://publications.europa.eu/resource/authority/licence/CC_BY_4_0"
    elif "creativecommons.org/publicdomain/zero/1.0" in uri:
        return "http://publications.europa.eu/resource/authority/licence/CC0"
    elif "data.norge.no/nlod" in uri:
        return "http://publications.europa.eu/resource/authority/licence/NLOD_2_0"
    else:
        return uri


datasets_file = args.outputdirectory + "mongo_datasets.json"
outputfileName = args.outputdirectory + "transformed_datasets.json"
with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(datasets_file, "datasets"), outfile, ensure_ascii=False, indent=4)

