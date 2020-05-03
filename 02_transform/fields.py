dataset_fields = [
    "field_data_field_access_rights",
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
    "field_data_body": { "valuefields": [
        {"valuefield": "body_value", "isnode" : False},
        {"valuefield": "body_summary", "isnode" : False},
        {"valuefield": "body_format", "isnode" : False}] },
    "field_data_comment_body": { "valuefields": [
        {"valuefield": "comment_body_value", "isnode" : False}, 
        {"valuefield": "comment_body_format", "isnode" : False}] },
    "field_data_field_access_rights": { "valuefields": [
        {"valuefield" : "field_access_rights_target_id", "isnode" : True}]},
    "field_data_field_access_url": { "valuefields": [
        {"valuefield": "field_access_url_url", "isnode" : False}] },
    "field_data_field_accrual_periodicity": { "valuefields": [
        {"valuefield" : "field_accrual_periodicity_target_id", "isnode" : True}] },
    "field_data_field_app_contact_mail": { "valuefields": [
        {"valuefield": "field_app_contact_mail_value", "isnode" : False}] },
    "field_data_field_app_contact_name": { "valuefields": [
        {"valuefield": "field_app_contact_name_value", "isnode" : False}] },
    "field_data_field_app_description": { "valuefields": [
        {"valuefield": "field_app_description_value", "isnode" : False}, 
        {"valuefield": "field_app_description_format", "isnode" : False}] },
    "field_data_field_app_resource": { "valuefields": [
        {"valuefield": "field_app_resource_url", "isnode" : False}, 
        {"valuefield": "field_app_resource_title", "isnode" : False}] },
    "field_data_field_approved": { "valuefields": [
        {"valuefield": "field_approved_value", "isnode" : False}]},
    "field_data_field_category": { "valuefields": [
        {"valuefield": "field_category_tid", "isnode" : False}]},
    "field_data_field_data": { "valuefields": [
        {"valuefield" : "field_data_nid", "isnode" : True}] },
    "field_data_field_data_contact_mail": { "valuefields": [
        {"valuefield": "field_data_contact_mail_value", "isnode" : False}]},
    "field_data_field_data_contact_name": { "valuefields": [
        {"valuefield": "field_data_contact_name_value", "isnode" : False}]},
    "field_data_field_data_description": { "valuefields": [
        {"valuefield": "field_data_description_value", "isnode" : False}]},
    "field_data_field_data_resource": { "valuefields": [
        {"valuefield": "field_data_resource_url", "isnode": False}, 
        {"valuefield": "field_data_resource_title", "isnode": False}]},
    "field_data_field_data_resources_data": { "valuefields": [
        {"valuefield": "field_data_resources_data_url", "isnode": False}, 
        {"valuefield": "field_data_resources_data_title", "isnode": False}]},
    "field_data_field_data_version": { "valuefields": [
        {"valuefield": "field_data_version_value", "isnode": False}] },
    "field_data_field_dcat_key": { "valuefields": [
        {"valuefield": "field_dcat_key_value", "isnode": False}] },
    "field_data_field_delete": { "valuefields": [
        {"valuefield": "field_delete_value", "isnode": False}] },
    "field_data_field_description": { "valuefields": [
        {"valuefield": "field_description_value", "isnode": False}] },
    "field_data_field_distribution": { "valuefields": [
        {"valuefield": "field_distribution_target_id", "isnode" : True}]},
    "field_data_field_distribution_documentation": { "valuefields": [
        {"valuefield": "field_distribution_documentation_url", "isnode": False}, 
        {"valuefield": "field_distribution_documentation_title", "isnode": False}] },
    "field_data_field_distribution_title": { "valuefields": [
        {"valuefield": "field_distribution_title_value", "isnode": False}] },
    "field_data_field_distribution_type": { "valuefields": [
        {"valuefield": "field_distribution_type_nid", "isnode": True}] },
    "field_data_field_docs": { "valuefields": [
        {"valuefield": "field_docs_fid", "isnode": False}] },
    "field_data_field_documentation": { "valuefields": [
        {"valuefield": "field_documentation_url", "isnode": False}, 
        {"valuefield": "field_documentation_title", "isnode": False}] },
    "field_data_field_download_url": { "valuefields": [
        {"valuefield": "field_download_url_url", "isnode": False}] },
    "field_data_field_file_image_alt_text": { "valuefields": [
        {"valuefield": "field_file_image_alt_text_value", "isnode": False}] },
    "field_data_field_file_image_title_text": { "valuefields": [
        {"valuefield": "field_file_image_title_text_value", "isnode": False}] },
    "field_data_field_format": { "valuefields": [
        {"valuefield": "field_format_target_id", "isnode": True}] },
    "field_data_field_formatlist": { "valuefields": [
        {"valuefield": "field_formatlist_target_id", "isnode" : True}]},
    "field_data_field_geo": { "valuefields": [
        {"valuefield": "field_geo_tid", "isnode" : False}]},
    "field_data_field_hidden_comment": { "valuefields": [
        {"valuefield": "field_hidden_comment_value", "isnode": False}] },
    "field_data_field_image": { "valuefields": [
        {"valuefield": "field_image_fid", "isnode": False}, 
        {"valuefield": "field_image_width", "isnode": False}, 
        {"valuefield": "field_image_height", "isnode": False}] },
    "field_data_field_images": { "valuefields": [
        {"valuefield": "field_images_fid", "isnode": False}, 
        {"valuefield": "field_images_alt", "isnode": False}, 
        {"valuefield": "field_images_width", "isnode": False}, 
        {"valuefield": "field_images_height", "isnode": False}] },
    "field_data_field_ingress": { "valuefields": [
        {"valuefield": "field_ingress_value", "isnode": False}] },
    "field_data_field_key": { "valuefields": [
        {"valuefield": "field_key_value", "isnode": False}] },
    "field_data_field_landing_page": { "valuefields": [
        {"valuefield": "field_landing_page_url", "isnode": False}] },
    "field_data_field_language": { "valuefields": [
        {"valuefield": "field_language_target_id", "isnode" : True}]},
    "field_data_field_licence_software": { "valuefields": [
        {"valuefield": "field_licence_software_tid", "isnode": False}] },
    "field_data_field_license": { "valuefields": [
        {"valuefield": "field_license_target_id", "isnode": True}] },
    "field_data_field_lisens": { "valuefields": [
        {"valuefield": "field_lisens_licence", "isnode" : False}, 
        {"valuefield":"field_lisens_name", "isnode" : False}, 
        {"valuefield": "field_lisens_url", "isnode" : False}]},
    "field_data_field_los": { "valuefields": [
        {"valuefield": "field_los_tid", "isnode" : False }]},
    "field_data_field_organization": { "valuefields": [
        {"valuefield": "field_organization_nid", "isnode" : True}]},
    "field_data_field_organization_homepage": { "valuefields": [
        {"valuefield": "field_organization_homepage_value", "isnode": False}] },
    "field_data_field_organization_mail": { "valuefields": [
        {"valuefield": "field_organization_mail_value", "isnode": False}] },
    "field_data_field_organization_number": { "valuefields": [
        {"valuefield": "field_organization_number_value", "isnode": False}] },
    "field_data_field_sektorkode": { "valuefields": [
        {"valuefield": "field_sektorkode_value", "isnode": False}] },
    "field_data_field_sektornavn": { "valuefields": [
        {"valuefield": "field_sektornavn_value", "isnode": False}] },
    "field_data_field_shortname": { "valuefields": [
        {"valuefield": "field_shortname_value", "isnode": False}] },
    "field_data_field_slide_image": { "valuefields": [
        {"valuefield": "field_slide_image_fid", "isnode": False}, 
        {"valuefield": "field_slide_image_width", "isnode": False}, 
        {"valuefield": "field_slide_image_height", "isnode": False}] },
    "field_data_field_slide_number": { "valuefields": [
        {"valuefield": "field_slide_number_value", "isnode": False}] },
    "field_data_field_slide_text": { "valuefields": [
        {"valuefield": "field_slide_text_value", "isnode": False}] },
    "field_data_field_slide_url": { "valuefields": [
        {"valuefield": "field_slide_url_url", "isnode": False}] },
    "field_data_field_slideshow_image": { "valuefields": [
        {"valuefield": "field_slideshow_image_fid", "isnode": False}, 
        {"valuefield": "field_slideshow_image_width", "isnode": False}, 
        {"valuefield": "field_slideshow_image_height", "isnode": False}] },
    "field_data_field_slideshow_number": { "valuefields": [
        {"valuefield": "field_slideshow_number_value", "isnode": False}] },
    "field_data_field_slideshow_title": { "valuefields": [
        {"valuefield": "field_slideshow_title_value", "isnode": False}] },
    "field_data_field_temporal": { "valuefields": [
        {"valuefield": "field_temporal_value", "isnode": False}, 
        {"valuefield": "field_temporal_value2", "isnode": False}] },
    "field_data_field_temporal_end": { "valuefields": [
        {"valuefield": "field_temporal_end_value", "isnode": False}] },
    "field_data_field_temporal_start": { "valuefields": [
        {"valuefield": "field_temporal_start_value", "isnode": False}] },
    "field_data_field_tfaq": { "valuefields": [
        {"valuefield": "field_tfaq_tid", "isnode": False}] },
    "field_data_field_theme_uri": { "valuefields": [
        {"valuefield": "field_theme_uri_value", "isnode": False}] },
    "field_data_field_type": { "valuefields": [
        {"valuefield": "field_type_value", "isnode": False}] },
    "field_data_field_uri": { "valuefields": [
        {"valuefield": "field_uri_value", "isnode": False}] },
    "field_data_field_url": { "valuefields": [
        {"valuefield": "field_url_url", "isnode": False}] },
    "field_data_field_user_org_ref": { "valuefields": [
        {"valuefield": "field_user_org_ref_nid", "isnode" : True}]},
    "field_data_field_user_organization": { "valuefields": [
        {"valuefield": "field_user_organization_nid", "isnode": True}] },
    "field_data_field_web_service": { "valuefields": [
        {"valuefield": "field_web_service_url", "isnode": False}] },
    "field_data_title_field": { "valuefields": [
        {"valuefield": "title_field_value", "isnode": False}]}
}