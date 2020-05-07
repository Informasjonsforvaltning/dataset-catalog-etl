import json
from .utils import isEnOrNb, stripHtml

def entityTitle(entity_id):
    title = {}
    title_file = open('../tmp/extract/data/' + entity_id + '/field_data_title_field.json')
    title_field = json.load(title_file)

    
    if len(title_field['title_field_value']) == 1 and not isEnOrNb(title_field['language']['0']):
        title['nb'] = title_field['title_field_value']['0']
    else:
        for index in title_field['title_field_value']:
            lang = title_field['language'][index]
            if(isEnOrNb(lang)):
                title[lang] = stripHtml(title_field['title_field_value'][index])
    
    return title if len(title) > 0 else None
