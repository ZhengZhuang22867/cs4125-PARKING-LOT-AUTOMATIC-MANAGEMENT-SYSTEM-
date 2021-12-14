import pandas as pd
import pymysql

from Data.Daolmpl.View_reservation_info_Daolmpl import view_reservation_info_daolmpl
from Data.Database import database


class user_view_reservation_info:
    def __init__(self, name):
        self.name = name

    def view_reservation_info(self):
        print("Currently reserved parking spaces: ")
        d = database()
        vrid = view_reservation_info_daolmpl(self.name, None, None)
        vrid.connect_to_database()
        cursor = vrid.conn.cursor()
        cursor.execute(vrid.sql)
        data = pd.read_sql(vrid.sql, vrid.conn)
        print(data)
        vrid.conn.commit()
        d.close_conn()