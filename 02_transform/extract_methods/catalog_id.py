import json

def datasetCatalog(entity_id):
    nid_file = open('../tmp/extract/data/' + entity_id + '/field_data_field_organization.json')
    nid_field = json.load(nid_file)

    org_nid = nid_field['field_organization_nid'].get('0')
    
    if org_nid is not None:
        orgnr_file = open('../tmp/extract/organization/' + str(org_nid) + '/field_data_field_organization_number.json')
        orgnr_field = json.load(orgnr_file)

        return orgnr_field['field_organization_number_value'].get('0')
