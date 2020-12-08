import json
import requests
from pathlib import Path
import os

import argparse
token_file = open('./tmp/token.txt')

token = token_file.read()
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()

inputfile = "./tmp/catalogs.json"
host = 'http://dataset-catalogue:8080'
url = host + "/catalogs" + "?size=200"
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}

print("Posting to the following url: ", url)
# Load the publisher by posting the data:
r = requests.get(url, headers=headers)
with open(inputfile, 'w', encoding="utf-8") as outfile:
    json.dump(r.json(), outfile, ensure_ascii=False, indent=4)
