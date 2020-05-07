import json

def indexOfValue(value, values):
    for index in values:
        if values[index] == value:
            return index
            

def datasetKeywords(entity_id):
    keywords = []
    id_file = open('../tmp/extract/data/' + entity_id + '/field_data_field_los.json')
    id_field = json.load(id_file)

    for index in id_field['field_los_tid']:
        term_data_id = id_field['field_los_tid'][index]

        term_data_file = open('../tmp/extract/taxonomy_term_data.json')
        term_data = json.load(term_data_file)

        value_index = indexOfValue(term_data_id, term_data['tid'])

        if value_index is not None:
                value = {}
                value['nb'] = term_data['name'][value_index]
                keywords.append(value)

    return keywords if len(keywords) > 0 else None
