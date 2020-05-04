import json
from .utils import isEnOrNb

def entityTitle(entity_id):
    title = {}
    title_file = open('../tmp/extract/data/' + entity_id + '/field_data_title_field.json')
    title_field = json.load(title_file)

    for index in title_field['title_field_value']:
        lang = title_field['language'][index]
        if(isEnOrNb(lang)):
            title[lang] = title_field['title_field_value'][index]
    
    return title
