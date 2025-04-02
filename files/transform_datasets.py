import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()


def transform_theme(themes, is_los):
    base_uri = "https://psi.norge.no/los" if is_los else "http://publications.europa.eu/resource/authority/data-theme"
    transformed_themes = list()

    for theme in themes:
        if theme.get("uri") is not None and base_uri in theme["uri"]:
            transformed_themes.append(theme["uri"])
    return transformed_themes


def transform_distribution(dist):
    transformed_dist = dict()
    if dist.get("title") is not None:
        transformed_dist["title"] = dist.get("title")
    if dist.get("description") is not None:
        transformed_dist["description"] = dist.get("description")
    if dist.get("downloadURL") is not None:
        transformed_dist["downloadURL"] = dist.get("downloadURL")
    if dist.get("accessURL") is not None:
        transformed_dist["accessURL"] = dist.get("accessURL")
    if dist.get("license") is not None:
        transformed_dist["license"] = dist["license"].get("uri")

    if dist.get("conformsTo") is not None:
        conforms_to_list = list()
        for conforms_to in dist["conformsTo"]:
            transformed_conforms_to = dict()
            if conforms_to.get("uri") is not None:
                transformed_conforms_to["uri"] = conforms_to.get("uri")
            if conforms_to.get("prefLabel") is not None:
                transformed_conforms_to["prefLabel"] = conforms_to.get("prefLabel")
            if len(transformed_conforms_to) > 0:
                conforms_to_list.append(transformed_conforms_to)
        if len(conforms_to_list) > 0:
            transformed_dist["conformsTo"] = conforms_to_list

    if dist.get("page") is not None:
        page_uris = list()
        for page in dist["page"]:
            if page.get("uri") is not None:
                page_uris.append(page.get("uri"))
        if len(page_uris) > 0:
            transformed_dist["page"] = page_uris

    if dist.get("format"):
        transformed_dist["format"] = dist.get("format")
    if dist.get("mediaType"):
        transformed_dist["mediaType"] = dist.get("mediaType")

    if dist.get("accessService") is not None:
        service_uris = list()
        for service in dist["accessService"]:
            if len(service_uris) > 0:
                service_uris.append(service.get("uri"))
        if len(service_uris) > 0:
            transformed_dist["accessServices"] = service_uris

    return transformed_dist


def transform(datasets_file):
    datasets = openfile(datasets_file)
    transformed_datasets = []

    for old_dataset in datasets:
        transformed_dataset = {}
        transformed_dataset["_id"] = old_dataset["_id"]
        transformed_dataset["catalogId"] = old_dataset["catalogId"]

        if old_dataset.get("uri"):
            transformed_dataset["uri"] = old_dataset.get("uri")
        if old_dataset.get("_lastModified"):
            transformed_dataset["lastModified"] = old_dataset.get("_lastModified")
        if old_dataset.get("specializedType"):
            transformed_dataset["specializedType"] = old_dataset.get("specializedType")
        if old_dataset.get("originalUri"):
            transformed_dataset["originalUri"] = old_dataset.get("originalUri")

        if old_dataset.get("registrationStatus"):
            transformed_dataset["published"] = bool(old_dataset["registrationStatus"] == "PUBLISH")
        if old_dataset.get("registrationStatus"):
            transformed_dataset["approve"] = bool(
                old_dataset["registrationStatus"] == "APPROVE" or old_dataset["registrationStatus"] == "PUBLISH")

        if old_dataset.get("concepts") is not None:
            concept_uris = list()
            for concept in old_dataset["concepts"]:
                if concept.get("uri") is not None:
                    concept_uris.append(concept.get("uri"))
            if len(concept_uris) > 0:
                transformed_dataset["concepts"] = concept_uris

        if old_dataset.get("title") is not None:
            transformed_dataset["title"] = old_dataset.get("title")
        if old_dataset.get("description"):
            transformed_dataset["description"] = old_dataset.get("description")

        if old_dataset.get("contactPoint") is not None:
            contact_point_list = list()
            for contact_point in old_dataset.get("contactPoint"):
                transformed_contact_point = dict()
                if contact_point.get("organizationUnit") is not None:
                    transformed_contact_point["name"] = dict()
                    transformed_contact_point["name"]["nb"] = contact_point.get("organizationUnit")
                if contact_point.get("email") is not None:
                    transformed_contact_point["email"] = contact_point.get("email")
                if contact_point.get("hasURL") is not None:
                    transformed_contact_point["url"] = contact_point.get("hasURL")
                if contact_point.get("hasTelephone") is not None:
                    transformed_contact_point["phone"] = contact_point.get("hasTelephone")
                if len(transformed_contact_point) > 0:
                    contact_point_list.append(transformed_contact_point)
            if len(contact_point_list) > 0:
                transformed_dataset["contactPoints"] = contact_point_list

        if old_dataset.get("keywords") is not None:
            en = list()
            nb = list()
            nn = list()

            for keyword in old_dataset["keywords"]:
                if keyword.get("en") is not None:
                    en.append(keyword["en"])
                if keyword.get("nb") is not None:
                    nb.append(keyword["nb"])
                if keyword.get("nn") is not None:
                    nn.append(keyword["nn"])

            if len(en) > 0 or len(nb) > 0 or len(nn) > 0:
                transformed_dataset["keywords"] = {"en": en, "nb": nb, "nn": nn}

        if old_dataset.get("issued") is not None:
            transformed_dataset["issued"] = old_dataset.get("issued")

        if old_dataset.get("modified") is not None:
            transformed_dataset["modified"] = old_dataset.get("modified")

        if old_dataset.get("language") is not None:
            language_uris = list()
            for lang in old_dataset["language"]:
                language_uris.append(lang.get("uri"))
            if len(language_uris) > 0:
                transformed_dataset["language"] = language_uris

        if old_dataset.get("landingPage"):
            transformed_dataset["landingPage"] = old_dataset.get("landingPage")

        if old_dataset.get("theme") is not None:
            dataThemes = transform_theme(old_dataset.get("theme"), False)
            losThemes = transform_theme(old_dataset.get("theme"), True)
            if len(dataThemes) > 0:
                transformed_dataset["euDataTheme"] = dataThemes
            if len(losThemes) > 0:
                transformed_dataset["losTheme"] = losThemes

        if old_dataset.get("distribution") is not None:
            transformed_distributions = list()
            for dist in old_dataset["distribution"]:
                if dist is not None:
                    transformed_distributions.append(transform_distribution(dist))
            if len(transformed_distributions) > 0:
                transformed_dataset["distribution"] = transformed_distributions

        if old_dataset.get("sample") is not None:
            transformed_samples = list()
            for dist in old_dataset["sample"]:
                if dist is not None:
                    ts_dist = transform_distribution(dist)
                    if len(ts_dist) > 0:
                        transformed_samples.append(ts_dist)
            if len(transformed_samples) > 0:
                transformed_dataset["sample"] = transformed_samples

        if old_dataset.get("temporal") is not None:
            temporal_list = list()
            for temp in old_dataset.get("temporal"):
                transformed_temporal = dict()
                if temp.get("startDate") is not None:
                    transformed_temporal["startDate"] = temp.get("startDate")
                if temp.get("endDate") is not None:
                    transformed_temporal["endDate"] = temp.get("endDate")
                if len(transformed_temporal) > 0:
                    temporal_list.append(transformed_temporal)
            if len(temporal_list) > 0:
                transformed_dataset["temporal"] = temporal_list

        if old_dataset.get("spatial") is not None:
            spatial_uris = list()
            for spatial in old_dataset["spatial"]:
                if spatial.get("uri") is not None:
                    spatial_uris.append(spatial.get("uri"))
            if len(spatial_uris) > 0:
                transformed_dataset["spatial"] = spatial_uris

        if old_dataset.get("accessRights") is not None:
            if old_dataset["accessRights"].get("uri") is not None:
                transformed_dataset["accessRight"] = old_dataset["accessRights"].get("uri")

        if old_dataset.get("legalBasisForRestriction") is not None:
            restriction_list = list()
            for restriction in old_dataset["legalBasisForRestriction"]:
                transformed_restrictions = dict()
                if restriction.get("uri") is not None:
                    transformed_restrictions["uri"] = restriction.get("uri")
                if restriction.get("prefLabel") is not None:
                    transformed_restrictions["prefLabel"] = restriction.get("prefLabel")
                if len(restriction_list) > 0:
                    restriction_list.append(transformed_restrictions)
            if len(restriction_list) > 0:
                transformed_dataset["legalBasisForRestriction"] = restriction_list

        if old_dataset.get("legalBasisForProcessing") is not None:
            legal_basis_list = list()
            for legal_basis in old_dataset["legalBasisForProcessing"]:
                transformed_legal_basis = dict()
                if legal_basis.get("uri") is not None:
                    transformed_legal_basis["uri"] = legal_basis.get("uri")
                if legal_basis.get("prefLabel") is not None:
                    transformed_legal_basis["prefLabel"] = legal_basis.get("prefLabel")
                if len(transformed_legal_basis) > 0:
                    legal_basis_list.append(transformed_legal_basis)
            if len(legal_basis_list) > 0:
                transformed_dataset["legalBasisForProcessing"] = legal_basis_list

        if old_dataset.get("legalBasisForAccess") is not None:
            legal_basis_list = list()
            for legal_basis in old_dataset["legalBasisForAccess"]:
                transformed_legal_basis = dict()
                if legal_basis.get("uri") is not None:
                    transformed_legal_basis["uri"] = legal_basis.get("uri")
                if legal_basis.get("prefLabel") is not None:
                    transformed_legal_basis["prefLabel"] = legal_basis.get("prefLabel")
                if len(transformed_legal_basis) > 0:
                    legal_basis_list.append(transformed_legal_basis)
            if len(legal_basis_list) > 0:
                transformed_dataset["legalBasisForAccess"] = legal_basis_list

        if old_dataset.get("hasAccuracyAnnotation") is not None:
            accuracy = old_dataset["hasAccuracyAnnotation"]
            transformed_accuracy = dict()
            if accuracy.get("inDimension") is not None:
                transformed_accuracy["inDimension"] = accuracy.get("inDimension")
            if accuracy.get("motivatedBy") is not None:
                transformed_accuracy["motivatedBy"] = accuracy.get("motivatedBy")
            if accuracy.get("hasBody") is not None:
                transformed_accuracy["hasBody"] = accuracy.get("hasBody")
            if len(transformed_accuracy) > 0:
                transformed_dataset["accuracy"] = transformed_accuracy

        if old_dataset.get("hasCompletenessAnnotation") is not None:
            completeness = old_dataset["hasCompletenessAnnotation"]
            transformed_completeness = dict()
            if completeness.get("inDimension") is not None:
                transformed_completeness["inDimension"] = completeness.get("inDimension")
            if completeness.get("motivatedBy") is not None:
                transformed_completeness["motivatedBy"] = completeness.get("motivatedBy")
            if completeness.get("hasBody") is not None:
                transformed_completeness["hasBody"] = completeness.get("hasBody")
            if len(transformed_completeness) > 0:
                transformed_dataset["completeness"] = transformed_completeness

        if old_dataset.get("hasCurrentnessAnnotation") is not None:
            currentness = old_dataset["hasCurrentnessAnnotation"]
            transformed_currentness = dict()
            if currentness.get("inDimension") is not None:
                transformed_currentness["inDimension"] = currentness.get("inDimension")
            if currentness.get("motivatedBy") is not None:
                transformed_currentness["motivatedBy"] = currentness.get("motivatedBy")
            if currentness.get("hasBody") is not None:
                transformed_currentness["hasBody"] = currentness.get("hasBody")
            if len(transformed_currentness) > 0:
                transformed_dataset["currentness"] = transformed_currentness

        if old_dataset.get("hasAvailabilityAnnotation") is not None:
            availability = old_dataset["hasAvailabilityAnnotation"]
            transformed_availability = dict()
            if availability.get("inDimension") is not None:
                transformed_availability["inDimension"] = availability.get("inDimension")
            if availability.get("motivatedBy") is not None:
                transformed_availability["motivatedBy"] = availability.get("motivatedBy")
            if  availability.get("hasBody") is not None:
                transformed_availability["hasBody"] = availability.get("hasBody")
            if len(transformed_availability) > 0:
                transformed_dataset["availability"] = transformed_availability

        if old_dataset.get("hasRelevanceAnnotation") is not None:
            relevance = old_dataset["hasRelevanceAnnotation"]
            transformed_relevance = dict()
            if relevance.get("inDimension") is not None:
                transformed_relevance["inDimension"] = relevance.get("inDimension")
            if relevance.get("motivatedBy") is not None:
                transformed_relevance["motivatedBy"] = relevance.get("motivatedBy")
            if relevance.get("hasBody") is not None:
                transformed_relevance["hasBody"] = relevance.get("hasBody")
            if len(transformed_relevance) > 0:
                transformed_dataset["relevance"] = transformed_relevance

        if old_dataset.get("references") is not None:
            references = old_dataset["references"]
            transformed_references = list()

            for reference in references:
                transformed_reference = dict()
                if reference.get("referenceType") is not None:
                    transformed_reference["referenceType"] = reference.get("referenceType").get("code")
                if reference.get("source") is not None:
                    transformed_reference["source"] = reference.get("source").get("uri")
                if len(transformed_reference) > 0:
                    transformed_references.append(transformed_reference)
            if len(transformed_references) > 0:
                transformed_dataset["references"] = transformed_references

        if old_dataset.get("relations") is not None:
            related_resources = old_dataset["relations"]
            transformed_relations = list()

            for relation in related_resources:
                transformed_relation = dict()
                if relation.get("uri") is not None:
                    transformed_relation["uri"] = relation.get("uri")
                if relation.get("prefLabel") is not None:
                    transformed_relation["prefLabel"] = relation.get("prefLabel")
                if len(transformed_relation) > 0:
                    transformed_relations.append(transformed_relation)
            if len(transformed_relations) > 0:
                transformed_dataset["relatedResources"] = transformed_relations

        if old_dataset.get("provenance") is not None:
            transformed_dataset["provenance"] = old_dataset["provenance"].get("uri")

        if old_dataset.get("frequency") is not None:
            transformed_dataset["frequency"] = old_dataset["frequency"].get("uri")

        if old_dataset.get("conformsTo") is not None:
            conforms_to_list = list()
            for conforms_to in old_dataset["conformsTo"]:
                transformed_conforms_to = dict()
                if conforms_to.get("uri") is not None:
                    transformed_conforms_to["uri"] = conforms_to.get("uri")
                if conforms_to.get("prefLabel") is not None:
                    transformed_conforms_to["prefLabel"] = conforms_to.get("prefLabel")
                if len(transformed_conforms_to) > 0:
                    conforms_to_list.append(transformed_conforms_to)
            if len(conforms_to_list) > 0:
                transformed_dataset["conformsTo"] = conforms_to_list

        if old_dataset.get("informationModel") is not None:
            information_model_list = list()
            for information_model in old_dataset["informationModel"]:
                transformed_information_model = dict()
                if information_model.get("uri") is not None:
                    transformed_information_model["uri"] = information_model.get("uri")
                if information_model.get("prefLabel") is not None:
                    transformed_information_model["prefLabel"] = information_model.get("prefLabel")
                if len(transformed_information_model) > 0:
                    information_model_list.append(transformed_information_model)
            if len(information_model_list) > 0:
                transformed_dataset["informationModelsFromOtherSources"] = information_model_list

        if old_dataset.get("informationModelsFromFDK"):
            transformed_dataset["informationModelsFromFDK"] = old_dataset.get("informationModelsFromFDK")
        if old_dataset.get("qualifiedAttributions") is not None:
            transformed_dataset["qualifiedAttributions"] = old_dataset.get("qualifiedAttributions")
        if old_dataset.get("type") is not None:
            transformed_dataset["type"] = old_dataset.get("type")
        if old_dataset.get("inSeries") is not None:
            transformed_dataset["inSeries"] = old_dataset.get("inSeries")
        if old_dataset.get("seriesDatasetOrder") is not None:
            transformed_dataset["seriesDatasetOrder"] = old_dataset.get("seriesDatasetOrder")

        transformed_datasets.append(transformed_dataset)

    return transformed_datasets


def openfile(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


datasetfileName = args.outputdirectory + "mongo_datasets.json"
outputfileName = args.outputdirectory + "datasets_transformed.json"

with open(outputfileName, 'w', encoding="utf-8") as outfile:
    json.dump(transform(datasetfileName), outfile, ensure_ascii=False, indent=4)
