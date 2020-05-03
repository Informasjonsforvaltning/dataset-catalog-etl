
from sqlalchemy import create_engine
from fields import fields, node_types
import pymysql
import pandas as pd
from pathlib import Path
import json
 
sqlEngine       = create_engine('mysql+pymysql://user:password@127.0.0.1', pool_recycle=3600)
dbConnection    = sqlEngine.connect()
 
for node_type in node_types:
    Path("../tmp/extract").mkdir(parents=True, exist_ok=True)
    dataset_frame = pd.read_sql("""
        SELECT nid
        FROM
        drupal_datanorge.node
        WHERE
        type = '""" + node_type + "'", dbConnection)
    
    pd.set_option('display.expand_frame_repr', False)
    dataset_frame.to_json('../tmp/extract/' + node_type + '.json')

    f = open('../tmp/extract/' + node_type + '.json')
    nodes = json.load(f)["nid"]

    for index in nodes:
        entity_id = str(nodes[index])
        Path("../tmp/extract/" + node_type + "/" + entity_id).mkdir(parents=True, exist_ok=True)
        for field in fields:
            field_frame           = pd.read_sql("""
            SELECT *
            FROM
            drupal_datanorge.""" + field + """
            WHERE
            entity_id = '""" + entity_id + """'
            """, dbConnection)

            pd.set_option('display.expand_frame_repr', False)
            field_frame.to_json('../tmp/extract/' + node_type + '/' + entity_id + '/' + field + '.json')

        print("Completed extraction of " + node_type + " with nid " + entity_id)

dbConnection.close()