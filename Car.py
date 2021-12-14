import pandas as pd
from Data.Database import database
from Data.Daolmpl.Car_Daolmpl import car_daolmpl


class Car:
    def __init__(self):
        pass

    def car(self):
        # connect to the database
        d = database()
        cdl = car_daolmpl(None, None)
        cdl.connect_to_database()
        #Pointers to manipulate the database
        cursor = cdl.conn.cursor()
        cursor.execute(cdl.sql)

        data = pd.read_sql(cdl.sql, cdl.conn)

        print(data)
        d.close_conn()

