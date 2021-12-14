import pandas as pd
import pymysql
from Data.Daolmpl.Map_Daolmpl import map_daolmpl

from Data.Database import database


class map:
    def __init__(self):
        pass

    def map(self):

        d = database()
        mdl = map_daolmpl(None, None)
        mdl.connect_to_database()

        # Pointers to manipulate the database
        cursor = mdl.conn.cursor()
        cursor.execute(mdl.sql)

        data = pd.read_sql(mdl.sql, mdl.conn)

        print(data)
        d.close_conn()
