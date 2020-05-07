import json

def datasetSpatial(entity_id):
    spatial = []
    id_file = open('../tmp/extract/data/' + entity_id + '/field_data_field_geo.json')
    id_field = json.load(id_file)

    for index in id_field['field_geo_tid']:
        spatial_id = id_field['field_geo_tid'][index]

        geo_file = open('../tmp/extract/geo.json')
        geo_field = json.load(geo_file)

        for geo_index in geo_field['entity_id']:
            if geo_field['entity_id'][geo_index] == spatial_id:
                value = {}
                value['uri'] = geo_field['field_uri_value'][geo_index]
                spatial.append(value)

    return spatial if len(spatial) > 0 else None
