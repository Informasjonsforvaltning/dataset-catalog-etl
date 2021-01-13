import json
import urllib.request
import argparse
import re
import os

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()

catalogs = "./tmp/catalogs.json"
match_string = '\\d{9}\\z'
environment = '' if os.environ['NAMESPACE'] == 'prod' else '.' + os.environ['NAMESPACE']
orgcat_uri = 'https://organization-catalogue' + environment + '.fellesdatakatalog.digdir.no/organizations/'

with open(catalogs) as catalog_file:
    count = 0
    embedded = json.load(catalog_file).get("_embedded")
    data = embedded.get("catalogs") if embedded else []
    transformed = []

    for catalog in data:
        orgId = catalog['id']
        updated_publisher = {'uri': orgcat_uri + orgId, 'id': orgId}

        try:
            catalog["publisher"] = updated_publisher
            transformed.append(catalog)
        except BaseException as err:
            print(f'{orgId} - {err}')

    with open(args.outputdirectory + 'transformed_catalogs.json', 'w', encoding="utf-8") as outfile:
        json.dump(transformed, outfile, ensure_ascii=False, indent=4)
