import json
import urllib.request
import time

token_file = open('../tmp/token.json')
token = json.load(token_file)['admin']

datasets_file = open('../tmp/extract/data.json')
datasets = json.load(datasets_file)

for dataset_index in datasets['nid']:
    ds_id = str(datasets["nid"][dataset_index])
    
    body_file = open('../tmp/transform/dataset/' + ds_id + '.json')
    dataset_body = json.load(body_file)

    uploadUrl = 'https://registrering.staging.fellesdatakatalog.digdir.no/catalogs/' + dataset_body['catalogId'] + '/datasets/admin'
    data = json.dumps(dataset_body).encode('utf8')

    req = urllib.request.Request(uploadUrl, data, headers={'content-type': 'application/json', 'accept': 'application/json', 'Authorization': 'Bearer ' + token}, method='POST')
            
    try:
        rsp = urllib.request.urlopen(req)
        print(f'{rsp.code}' + ': ' + dataset_body['catalogId'])

    except urllib.error.HTTPError as err:
        print(f'{err.code}' + ': ' + str(ds_id))