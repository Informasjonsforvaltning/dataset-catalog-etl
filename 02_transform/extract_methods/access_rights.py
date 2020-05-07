import json

def datasetAccessRights(entity_id):
    id_file = open('../tmp/extract/data/' + entity_id + '/field_data_field_access_rights.json')
    id_field = json.load(id_file)

    access_rights_id = id_field['field_access_rights_target_id'].get('0')

    if access_rights_id is not None:
        value_file = open('../tmp/extract/access_rights/' + str(access_rights_id) + '/field_data_field_key.json')
        value_field = json.load(value_file)

        access_rights = {}
        access_rights['uri'] = value_field['field_key_value'].get('0')
        return access_rights if access_rights['uri'] is not None else None

    else:
        return None
