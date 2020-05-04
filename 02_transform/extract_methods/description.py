import json
import re
from .utils import isEnOrNb

def entityDescription(entity_id):
    description = {}
    description_file = open('../tmp/extract/data/' + entity_id + '/field_data_field_data_description.json')
    description_field = json.load(description_file)

    for index in description_field['field_data_description_value']:
        lang = description_field['language'][index]
        if(isEnOrNb(lang)):
            description[lang] = stripHtml(description_field['field_data_description_value'][index])
    
    return description

def stripHtml(value):
    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
    return removeExtraSpaces(tag_re.sub(' ', value))

def removeExtraSpaces(value):
    return re.sub(' +', ' ', value.strip())