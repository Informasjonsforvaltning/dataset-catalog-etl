
from sqlalchemy import create_engine
from fields import fields
import pymysql
import pandas as pd

datasets = {"0": "77","1": "78"}

sqlEngine       = create_engine('mysql+pymysql://user:password@127.0.0.1', pool_recycle=3600)
dbConnection    = sqlEngine.connect()


for index in datasets:

    for field in fields:
        frame           = pd.read_sql("""
        SELECT *
        FROM
          drupal_datanorge.""" + field + """
        WHERE
          entity_id = '""" + datasets[index] + """'
        """, dbConnection)

        pd.set_option('display.expand_frame_repr', False)
        frame.to_json(r'../tmp/dataset/' + datasets[index] + '-' + field + '.json')



dbConnection.close()