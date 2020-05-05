import json
from pathlib import Path
from .description import entityDescription
from .utils import isEnOrNb

def datasetDistributions(entity_id):
    distributions = []
    title_file = open('../tmp/extract/data/' + entity_id + '/field_data_field_distribution.json')
    title_field = json.load(title_file)

    for index in title_field['field_distribution_target_id']:
        dist_id = str(title_field['field_distribution_target_id'][index])
        if Path('../tmp/extract/distribution/' + dist_id).exists():
            distribution = {}
            distribution['title'] = distributionTitle(dist_id)
            distribution['description'] = distributionDescription(dist_id)
            distribution['downloadURL'] = distributionDownloadUrl(dist_id)
            distribution['accessURL'] = distributionAccessUrl(dist_id)
            distribution['license'] = distributionLicense(dist_id)
            distribution['format'] = distributionFormat(dist_id)

            distributions.append(distribution)
    
    return distributions

def distributionTitle(entity_id):
    title = {}
    title_file = open('../tmp/extract/distribution/' + entity_id + '/field_data_field_distribution_title.json')
    title_field = json.load(title_file)

    titles = title_field['field_distribution_title_value']

    if len(titles) == 1 and not isEnOrNb(title_field['language']['0']):
        title['nb'] = titles['0']
    else:
        for index in titles:
            lang = title_field['language'][index]
            if(isEnOrNb(lang)):
                title[lang] = titles[index]
    
    return title

def distributionDescription(entity_id):
    description = {}
    description_file = open('../tmp/extract/distribution/' + entity_id + '/field_data_field_description.json')
    description_field = json.load(description_file)

    descriptions = description_field['field_description_value']

    if len(descriptions) == 1 and not isEnOrNb(description_field['language']['0']):
        description['nb'] = descriptions['0']
    else:
        for index in descriptions:
            lang = description_field['language'][index]
            if(isEnOrNb(lang)):
                description[lang] = descriptions[index]
    
    return description

def distributionAccessUrl(entity_id):
    urls = []
    json_file = open('../tmp/extract/distribution/' + entity_id + '/field_data_field_access_url.json')
    field = json.load(json_file)

    for index in field['field_access_url_url']:
        urls.append(field['field_access_url_url'][index])

    return urls

def distributionDownloadUrl(entity_id):
    urls = []
    json_file = open('../tmp/extract/distribution/' + entity_id + '/field_data_field_download_url.json')
    field = json.load(json_file)

    for index in field['field_download_url_url']:
        urls.append(field['field_download_url_url'][index])

    return urls

def distributionLicense(entity_id):
    value = None
    json_file = open('../tmp/extract/distribution/' + entity_id + '/field_data_field_license.json')
    field = json.load(json_file)

    license_id = field['field_license_target_id'].get('0')

    if license_id is not None:
        license_file = open('../tmp/extract/licens/' + str(license_id) + '/field_data_field_url.json')
        license_field = json.load(license_file)

        value = {}
        value['uri'] = license_field['field_url_url'].get('0')

    return value

def distributionFormat(entity_id):
    formats = []
    json_file = open('../tmp/extract/distribution/' + entity_id + '/field_data_field_format.json')
    field = json.load(json_file)

    for index in field['field_format_target_id']:
        format_id = str(field['field_format_target_id'][index])
        if Path('../tmp/extract/format/' + format_id).exists():
            format_file = open('../tmp/extract/format/' + format_id + '/field_data_field_key.json')
            format_field = json.load(format_file)

            formats.append(format_field['field_key_value'].get('0'))

    return formats
