import json
from . import dateFromTemporalTimestamp

def entityTemporal(entity_id):
    temporal = []
    timestamp = {}
    file_start = open('../tmp/extract/data/' + entity_id + '/field_data_field_temporal_start.json')
    file_end = open('../tmp/extract/data/' + entity_id + '/field_data_field_temporal_end.json')
    start = json.load(file_start)
    end = json.load(file_end)

    if start['field_temporal_start_value'].get('0'):
        timestamp['startDate'] = dateFromTemporalTimestamp(start['field_temporal_start_value'].get('0'))

    if end['field_temporal_end_value'].get('0') :
        timestamp['endDate'] = dateFromTemporalTimestamp(end['field_temporal_end_value'].get('0'))

    temporal.append(timestamp)

    return temporal