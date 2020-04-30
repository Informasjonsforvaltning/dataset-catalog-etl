

from sqlalchemy import create_engine
from fields import fields
import pymysql
import pandas as pd
from pathlib import Path
import json

f = open('../tmp/datasets.json')
datasets = json.load(f)["nid"]

sqlEngine       = create_engine('mysql+pymysql://user:password@127.0.0.1', pool_recycle=3600)
dbConnection    = sqlEngine.connect()


for index in datasets:
    entity_id = str(datasets[index])
    Path("../tmp/dataset/" + entity_id).mkdir(parents=True, exist_ok=True)
    for field in fields:
        frame           = pd.read_sql("""
        SELECT *
        FROM
          drupal_datanorge.""" + field + """
        WHERE
          entity_id = '""" + entity_id + """'
        """, dbConnection)

        pd.set_option('display.expand_frame_repr', False)
        frame.to_json(r'../tmp/dataset/' + entity_id + '/' + field + '.json')



dbConnection.close()