import json

themes = {
    990: {
        "uri": "http://publications.europa.eu/resource/authority/data-theme/GOVE",
        "title": {
            "nb": "Forvaltning og offentlig sektor"
        }
    },
    995: {
        "uri": "http://publications.europa.eu/resource/authority/data-theme/ECON",
        "title": {
            "nb": "Økonomi og finans"
        }
    },
    984: {
        "uri": "http://publications.europa.eu/resource/authority/data-theme/TECH",
        "title": {
            "nb": "Vitenskap og teknologi"
        }
    },
    982: {
        "uri": "http://publications.europa.eu/resource/authority/data-theme/INTR",
        "title": {
            "nb": "Internasjonale temaer"
        }
    },
    991: {
        "uri": "http://publications.europa.eu/resource/authority/data-theme/JUST",
        "title": {
            "nb": "Justis, rettssystem og allmenn sikkerhet"
        }
    },
    994: {
        "uri": "http://publications.europa.eu/resource/authority/data-theme/EDUC",
        "title": {
            "nb": "Utdanning, kultur og sport"
        }
    },
    988: {
        "uri": "https://psi.norge.no/los/tema/natur-klima-og-miljo"
    },
    987: {
        "uri": "https://psi.norge.no/los/tema/landbruk"
    },
    983: {
        "uri": "https://psi.norge.no/los/tema/bygg-og-eiendom"
    },
    977: {
        "uri": "https://psi.norge.no/los/tema/familie-og-barn"
    },
    992: {
        "uri": "https://psi.norge.no/los/tema/trafikk-og-transport"
    },
    980: {
        "uri": "https://psi.norge.no/los/tema/helse-og-omsorg"
    },
    976: {
        "uri": "https://psi.norge.no/los/tema/energi"
    }
}

def datasetTheme(entity_id):
    values = []
    theme_file = open('../tmp/extract/data/' + entity_id + '/field_data_field_category.json')
    theme_id_field = json.load(theme_file)

    for index in theme_id_field['field_category_tid']:
        theme = themes.get(theme_id_field['field_category_tid'][index])
        
        if theme is not None:
            values.append(theme)
    
    return values if len(values) > 0 else None