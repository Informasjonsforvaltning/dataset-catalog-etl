import json
from pathlib import Path

from utils import isEnOrNb

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
        lang = title_field['language'][index]
        if(isEnOrNb(lang)):
            fdk_dataset['title'][lang] = title_field['title_field_value'][index]

    # Extract description
    fdk_dataset['description'] = {}
    description_file = open('../tmp/extract/data/' + ds_id + '/field_data_field_data_description.json')
    description_field = json.load(description_file)

    for index in description_field['field_data_description_value']:
        lang = description_field['language'][index]
        if(isEnOrNb(lang)):
            fdk_dataset['description'][lang] = description_field['field_data_description_value'][index]

    # Save dataset to file
    with open('../tmp/transform/dataset/' + ds_id + '.json', 'w') as outfile:
        json.dump(fdk_dataset, outfile)
