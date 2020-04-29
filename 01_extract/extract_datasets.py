
from sqlalchemy import create_engine
import pymysql
import pandas as pd
 
sqlEngine       = create_engine('mysql+pymysql://usr:pwd@127.0.0.1', pool_recycle=3600)
dbConnection    = sqlEngine.connect()
frame           = pd.read_sql("""
SELECT nid
FROM
  drupal_datanorge.node
WHERE
  type = 'data'
""", dbConnection);
 
pd.set_option('display.expand_frame_repr', False)
frame.to_json(r'../tmp/datasets.json')
 
dbConnection.close()