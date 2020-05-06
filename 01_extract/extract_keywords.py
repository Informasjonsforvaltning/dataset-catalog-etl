from sqlalchemy import create_engine
from fields import fields, node_types
import pymysql
import pandas as pd
from pathlib import Path
import json

sqlEngine       = create_engine('mysql+pymysql://user:password@127.0.0.1', pool_recycle=3600)
dbConnection    = sqlEngine.connect()
Path("../tmp/extract").mkdir(parents=True, exist_ok=True)
dataset_frame = pd.read_sql("""
    SELECT *
    FROM
    drupal_datanorge.taxonomy_term_data""", dbConnection)

pd.set_option('display.expand_frame_repr', False)
dataset_frame.to_json('../tmp/extract/taxonomy_term_data.json')

dbConnection.close() 