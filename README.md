# dataset-catalog-etl
ETL type utilities related to our dataset catalog

This version of the ETL was created for migrating from dataset-catalogue (elastic) to dataset-catalog (mongodb)

The ETL must be deployed, and run from the container in the respective namespace.
Auth token must be inserted into tmp/token.txt after container has been created.
Branch must be set in workflow files.
For helm to work properly, GitHub Pages source must be set in the repository

1. Make extract_catalogs (extracts catalogs from old service)
2. make extract (extracts all data from old service)
3. make transform (does necessary transformation of data, in this ETL-case, minimal changes to date/timestamps)
4. make load_catalogs (uploads catalogs to new service)
5. make load (loads transformed data to new service)