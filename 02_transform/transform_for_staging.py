import json

datasets_file = open('../tmp/extract/data.json')
datasets = json.load(datasets_file)

uploadUrl = 'http://localhost:8114/catalogs/admin'

for dataset_index in datasets['nid']:
    ds_id = str(datasets["nid"][dataset_index])
    
    ds_file = open('../tmp/transform/dataset/' + ds_id + '.json')
    dataset = json.load(ds_file)

    dataset['catalogId'] = '910244999'

    with open('../tmp/transform/dataset/' + ds_id + '.json', 'w') as outfile:
        json.dump(dataset, outfile, ensure_ascii=False)