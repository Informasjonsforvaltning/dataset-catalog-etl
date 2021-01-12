import json
import requests

import argparse
token_file = open('./tmp/token.txt')

token = str([line.rstrip('\n') for line in token_file][0])
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()

output_file = "./tmp/datasets.json"
url = 'http://dataset-catalog:8080/datasets'
headers = {'Accept': 'application/json', 'Authorization': 'Bearer ' + token}

print("Getting the following url: ", url)

with open(output_file) as output:

    try:
        rsp = requests.get(url, headers=headers)
        rsp.raise_for_status()
        json.dump(rsp.json(), output, ensure_ascii=False, indent=4)

    except requests.HTTPError as err:
        print(f'{err}')
