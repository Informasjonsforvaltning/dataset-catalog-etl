import json

languages = {
    643: {
        "uri" : "http://publications.europa.eu/resource/authority/language/NOR",
        "code" : "NOR",
        "prefLabel" : {
            "nb" : "Norsk"
        }
    },
    644: {
        "uri" : "http://publications.europa.eu/resource/authority/language/ENG",
        "code" : "ENG",
        "prefLabel" : {
            "nb" : "Engelsk"
        }
    }
}

def datasetLanguage(entity_id):
    values = []
    lang_file = open('../tmp/extract/data/' + entity_id + '/field_data_field_language.json')
    lang_id_field = json.load(lang_file)

    for index in lang_id_field['field_language_target_id']:
        lang = languages.get(lang_id_field['field_language_target_id'][index])
        
        if lang is not None:
            values.append(lang)
    
    return values if len(values) > 0 else None
