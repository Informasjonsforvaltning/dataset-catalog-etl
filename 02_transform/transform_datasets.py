import json
from pathlib import Path

f = open('../tmp/extract/data.json')
datasets = json.load(f)["nid"]

for dataset_index in datasets:
    Path('../tmp/transform/dataset').mkdir(parents=True, exist_ok=True)
    ds_id = str(datasets[dataset_index])
    fdk_dataset = {}

    # Extract title
    fdk_dataset['title'] = {}
    title_file = open('../tmp/extract/data/' + ds_id + '/field_data_title_field.json')
    title_field = json.load(title_file)

    for index in title_field['title_field_value']:
        fdk_dataset['title'][title_field['language'][index]] = title_field['title_field_value'][index]

    # Save dataset to file
    with open('../tmp/transform/dataset/' + ds_id + '.json', 'w') as outfile:
        json.dump(fdk_dataset, outfile)