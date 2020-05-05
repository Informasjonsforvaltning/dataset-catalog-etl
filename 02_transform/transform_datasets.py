import json
from pathlib import Path

from extract_methods import entityTitle, entityDescription, entityLandingPage

f = open('../tmp/extract/data.json')
datasets = json.load(f)["nid"]

for dataset_index in datasets:
    Path('../tmp/transform/dataset').mkdir(parents=True, exist_ok=True)
    ds_id = str(datasets[dataset_index])
    fdk_dataset = {}

    fdk_dataset['title'] = entityTitle(ds_id)
    fdk_dataset['description'] = entityDescription(ds_id)
    fdk_dataset['landingPage'] = entityLandingPage(ds_id)

    # Save dataset to file
    with open('../tmp/transform/dataset/' + ds_id + '.json', 'w') as outfile:
        json.dump(fdk_dataset, outfile, ensure_ascii=False)
