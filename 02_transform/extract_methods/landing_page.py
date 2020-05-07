import json

def entityLandingPage(entity_id):
    landingpage = []
    file = open('../tmp/extract/data/' + entity_id + '/field_data_field_landing_page.json')
    field = json.load(file)

    for index in field['field_landing_page_url']:
        landingpage.append(field['field_landing_page_url'][index])

    return landingpage if len(landingpage) > 0 else None
