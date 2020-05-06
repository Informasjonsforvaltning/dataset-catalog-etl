import json
from pathlib import Path

from extract_methods import (
    entityTitle,
    entityDescription,
    entityLandingPage,
    dateFromTimestamp,
    datasetDistributions,
    datasetAccessRights,
    datasetUpdateFrequency,
    datasetLanguage
)

f = open('../tmp/extract/data.json')
datasets = json.load(f)

for dataset_index in datasets['nid']:
    Path('../tmp/transform/dataset').mkdir(parents=True, exist_ok=True)
    ds_id = str(datasets["nid"][dataset_index])
    fdk_dataset = {}

    fdk_dataset['title'] = entityTitle(ds_id)
    fdk_dataset['description'] = entityDescription(ds_id)
    fdk_dataset['landingPage'] = entityLandingPage(ds_id)
    fdk_dataset['issued'] = dateFromTimestamp(datasets['created'][dataset_index])
    fdk_dataset['modified'] = dateFromTimestamp(datasets['changed'][dataset_index])
    fdk_dataset['distribution'] = datasetDistributions(ds_id)
    fdk_dataset['accessRights'] = datasetAccessRights(ds_id)
    fdk_dataset['accrualPeriodicity'] = datasetUpdateFrequency(ds_id)
    fdk_dataset['language'] = datasetLanguage(ds_id)

    fdk_dataset['registrationStatus'] = "PUBLISH"

    # Save dataset to file
    with open('../tmp/transform/dataset/' + ds_id + '.json', 'w') as outfile:
        json.dump(fdk_dataset, outfile, ensure_ascii=False)
