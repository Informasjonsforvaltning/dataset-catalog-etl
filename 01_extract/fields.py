fields = ["field_data_body","field_data_comment_body","field_data_field_access_rights","field_data_field_access_url","field_data_field_accrual_periodicity","field_data_field_antall_datasett","field_data_field_app_contact_mail","field_data_field_app_contact_name","field_data_field_app_description","field_data_field_app_resource","field_data_field_approved","field_data_field_category","field_data_field_data","field_data_field_data_contact_mail","field_data_field_data_contact_name","field_data_field_data_description","field_data_field_data_resource","field_data_field_data_resources_data","field_data_field_data_version","field_data_field_dcat_key","field_data_field_delete","field_data_field_description","field_data_field_distribution","field_data_field_distribution_documentation","field_data_field_distribution_title","field_data_field_distribution_type","field_data_field_docs","field_data_field_documentation","field_data_field_download_url","field_data_field_file_image_alt_text","field_data_field_file_image_title_text","field_data_field_format","field_data_field_formatlist","field_data_field_geo","field_data_field_hidden_comment","field_data_field_image","field_data_field_images","field_data_field_ingress","field_data_field_key","field_data_field_landing_page","field_data_field_language","field_data_field_licence_software","field_data_field_license","field_data_field_lisens","field_data_field_los","field_data_field_organization","field_data_field_organization_homepage","field_data_field_organization_mail","field_data_field_organization_number","field_data_field_sektorkode","field_data_field_sektornavn","field_data_field_shortname","field_data_field_slide_image","field_data_field_slide_number","field_data_field_slide_text","field_data_field_slide_url","field_data_field_slideshow_image","field_data_field_slideshow_number","field_data_field_slideshow_title","field_data_field_temporal","field_data_field_temporal_end","field_data_field_temporal_start","field_data_field_tfaq","field_data_field_theme_uri","field_data_field_type","field_data_field_uri","field_data_field_url","field_data_field_user_org_ref","field_data_field_user_organization","field_data_field_web_service","field_data_title_field"]

# dataset 77
dataset_fields = ["field_data_field_access_rights",
                  "field_data_field_antall_datasett",
                  "field_data_field_approved",
                  "field_data_field_category",
                  "field_data_field_data_contact_mail",
                  "field_data_field_data_contact_name",
                  "field_data_field_data_description",
                  "field_data_field_data_resource",
                  "field_data_field_data_resources_data",
                  "field_data_field_distribution",
                  "field_data_field_formatlist",
                  "field_data_field_geo",
                  "field_data_field_language",
                  "field_data_field_lisens",
                  "field_data_field_los",
                  "field_data_field_organization",
                  "field_data_field_user_org_ref",
                  "field_data_title_field"
]

table_structure = {
    "field_data_field_access_rights": { "valuefield" : "field_access_rights_target_id", "isnode" : True},
    "field_data_field_antall_datasett": { "antall_datasett" : "field_antall_datasett_value", "isnode" : False},
    "field_data_field_approved": { "valuefield": "field_approved_value", "isnode" : False},
    "field_data_field_category": { "valuefield": "field_category_tid", "isnode" : False},
    "field_data_field_data_contact_mail": { "valuefield": "field_data_contact_mail_value", "isnode" : False},
    "field_data_field_data_contact_name": { "valuefield": "field_data_contact_name_value", "isnode" : False},
    "field_data_field_data_description": { "valuefield": "field_data_description_value", "isnode" : False},
    "field_data_field_data_resource": { "valuefields": [{"valuefield": "field_data_resource_url", "isnode": False}, {"valuefield": "field_data_resource_title", "isnode": False}]},
    "field_data_field_data_resources_data": { "valuefields": [{"valuefield": "field_data_resources_data_url", "isnode": False}, {"valuefield": "field_data_resources_data_title", "isnode": False}]},
    "field_data_field_distribution": { "valuefield": "field_distribution_target_id", "isnode" : True},
    "field_data_field_formatlist": { "valuefield": "field_formatlist_target_id", "isnode" : True},
    "field_data_field_geo": { "valuefield": "field_geo_tid", "isnode" : False},
    "field_data_field_language": { "valuefield": "field_language_target_id", "isnode" : True},
    "field_data_field_lisens": { "valuefields": [{"valuefield": "field_lisens_licence", "isnode" : False}, {"valuefield":"field_lisens_name", "isnode" : False}, {"valuefield": "field_lisens_url", "isnode" : False}]},
    "field_data_field_los": { "valuefield": "field_los_tid", "isnode" : False },
    "field_data_field_organization": { "valuefield": "field_organization_nid", "isnode" : True},
    "field_data_field_user_org_ref": { "valuefield": "field_user_org_ref_nid", "isnode" : True},
    "field_data_title_field": { "valuefield": "title_field_value", "isnode": False}
}