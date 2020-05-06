import json

frequencies = {
    '615': {
      'uri': 'http://publications.europa.eu/resource/authority/frequency/ANNUAL',
      'code': 'ANNUAL',
      'prefLabel': {'no': 'årlig'}
    },
    '614': {
      'uri':
        'http://publications.europa.eu/resource/authority/frequency/ANNUAL_3',
      'code': 'ANNUAL_3',
      'prefLabel': {'no': 'tre ganger per år'}
    },
    '616': {
      'uri':
        'http://publications.europa.eu/resource/authority/frequency/BIENNIAL',
      'code': 'BIENNIAL',
      'prefLabel': {'no': 'annethvert år'}
    },
    '611': {
      'uri':
        'http://publications.europa.eu/resource/authority/frequency/BIMONTHLY',
      'code': 'BIMONTHLY',
      'prefLabel': {'no': 'annenhver måned'}
    },
    '607': {
      'uri':
        'http://publications.europa.eu/resource/authority/frequency/BIWEEKLY',
      'code': 'BIWEEKLY',
      'prefLabel': {'no': 'hver fjortende dag'}
    },
    '602': {
      'uri': 'http://publications.europa.eu/resource/authority/frequency/CONT',
      'code': 'CONT',
      'prefLabel': {'no': 'kontinuerlig'}
    },
    '603': {
      'uri': 'http://publications.europa.eu/resource/authority/frequency/DAILY',
      'code': 'DAILY',
      'prefLabel': {'no': 'daglig'}
    },
    '618': {
      'uri': 'http://publications.europa.eu/resource/authority/frequency/IRREG',
      'code': 'IRREG',
      'prefLabel': {'no': 'uregelmessig'}
    },
    '610': {
      'uri': 'http://publications.europa.eu/resource/authority/frequency/MONTHLY',
      'code': 'MONTHLY',
      'prefLabel': {'no': 'månedlig'}
    },
    '608': {
      'uri':
        'http://publications.europa.eu/resource/authority/frequency/MONTHLY_3',
      'code': 'MONTHLY_3',
      'prefLabel': {'no': 'tre ganger i måneden'}
    },
    '609': {
      'uri': 'http://publications.europa.eu/resource/authority/frequency/OTHER',
      'code': 'OTHER',
      'prefLabel': {'no': 'annet'}
    },
    '605': {
      'uri': 'http://publications.europa.eu/resource/authority/frequency/OTHER',
      'code': 'OTHER',
      'prefLabel': {'no': 'annet'}
    },
    '612': {
      'uri':
        'http://publications.europa.eu/resource/authority/frequency/QUARTERLY',
      'code': 'QUARTERLY',
      'prefLabel': {'no': 'kvartalsvis'}
    },
    '617': {
      'uri':
        'http://publications.europa.eu/resource/authority/frequency/TRIENNIAL',
      'code': 'TRIENNIAL',
      'prefLabel': {'no': 'hvert tredje år'}
    },
    '613': {
      'uri': 'http://publications.europa.eu/resource/authority/frequency/UNKNOWN',
      'code': 'UNKNOWN',
      'prefLabel': {'no': 'ukjent'}
    },
    '606': {
      'uri': 'http://publications.europa.eu/resource/authority/frequency/WEEKLY',
      'code': 'WEEKLY',
      'prefLabel': {'no': 'ukentlig'}
    },
    '604': {
      'uri':
        'http://publications.europa.eu/resource/authority/frequency/WEEKLY_3',
      'code': 'WEEKLY_3',
      'prefLabel': {'no': 'tre ganger i uken'}
    }
}

def datasetUpdateFrequency(entity_id):
    id_file = open('../tmp/extract/data/' + entity_id + '/field_data_field_accrual_periodicity.json')
    id_field = json.load(id_file)

    frequency_id = id_field['field_accrual_periodicity_target_id'].get('0')

    if frequency_id is not None:
        return frequencies[str(frequency_id)]
    else:
        return None
