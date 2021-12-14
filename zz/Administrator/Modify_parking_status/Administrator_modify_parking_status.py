import pandas as pd
import pymysql

from Data.Daolmpl.Modify_parking_status_Daolmpl import modify_parking_status_daolmpl
from Data.Database import database
from UI.Ui_controller import ui_controller


class administrator_modify_parking_status:
    def __init__(self):
        pass

    def modify_parking_status(self):

        d = database()
        mpsd = modify_parking_status_daolmpl(None, None, None, None)
        mpsd.connect_to_databse()

        print("View the status of parking spaces:")

        data = pd.read_sql(mpsd.sql, mpsd.conn)
        print(data)


        while True:
            u = ui_controller()
            u.modify_parking_status_interface()
            cmd = int(input("Please enter the instruction number："))
            if cmd == 1:
                n = input("Please enter the 'space_id' of the parking space you want to change: ")

                mpsd1 = modify_parking_status_daolmpl(None, None, None, n)
                mpsd1.database_operation()
                cursor = mpsd1.conn.cursor()
                cursor.execute(mpsd1.sql1)
                mpsd1.conn.commit()

                data = pd.read_sql(mpsd.sql, mpsd1.conn)
                print("The current parking status is: ")
                print(data)
                break
                
            elif cmd == 2:
                break



