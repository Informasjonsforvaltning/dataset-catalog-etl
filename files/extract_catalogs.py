import json
import requests

import argparse
token_file = open('./tmp/token.txt')

token = str([line.rstrip('\n') for line in token_file][0])
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()

output_file = "./tmp/catalogs.json"
url = 'http://dataset-catalog:8080/catalogs'
headers = {'Accept': 'application/json', 'Authorization': 'Bearer ' + token}

print("Getting the following url: ", url)

with open(output_file) as output:

    try:
        rsp = requests.get(url, headers=headers)
        rsp.raise_for_status()
        output.write(rsp.text)

    except requests.HTTPError as err:
        print(f'{err}')
