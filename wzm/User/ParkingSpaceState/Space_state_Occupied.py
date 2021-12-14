from Data.Daolmpl.Space_reservation_Daolmpl import space_reservation_daolmpl
from DesignPattern.State import state
import pandas as pd


class space_state_occupied(state):

    def __init__(self, name):
        self.name = name

    # Motor
    def getOccupied(self):
        srd = space_reservation_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None,
                                        None, None, None)
        srd.connect_to_database()
        #
        cursor = srd.conn.cursor()
        cursor.execute(srd.sql)
        srd.conn.commit()
        #
        data = pd.read_sql(srd.sql, srd.conn)
        print("The currently available parking spaces are: ")
        print(data)

        spacechoose = input("Please select the parking space you want to reserve: ")
        # 更新'parking_space'表中的'space_state'和'space_id'
        srd1 = space_reservation_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None,
                                         None, None, spacechoose)
        srd1.database_operation()
        cursor = srd1.conn.cursor()
        cursor.execute(srd1.sql2)
        srd1.conn.commit()
        # data1 = pd.read_sql(srd1.sql2, srd1.conn)
        # 更新'reservation_info'表中的'space_id'和'space_type'
        srd2 = space_reservation_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None,
                                         None, None, spacechoose)
        srd2.database_operation1()
        cursor = srd2.conn.cursor()
        cursor.execute(srd2.sql3)
        srd2.conn.commit()

    # Car
    def getOccupied1(self):
        srd3 = space_reservation_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None,
                                         None, None, None)
        srd3.connect_to_database1()
        #
        cursor = srd3.conn.cursor()
        cursor.execute(srd3.sql4)
        srd3.conn.commit()
        #
        data2 = pd.read_sql(srd3.sql4, srd3.conn)
        print("The currently available parking spaces are: ")
        print(data2)
        spacechoose1 = input("Please select the parking space you want to reserve: ")

        srd4 = space_reservation_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None,
                                         None, None, spacechoose1)
        srd4.database_operation2()
        cursor = srd4.conn.cursor()
        cursor.execute(srd4.sql5)
        srd4.conn.commit()

        srd5 = space_reservation_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None,
                                         None, None, spacechoose1)
        srd5.database_operation3()
        cursor = srd5.conn.cursor()
        cursor.execute(srd5.sql6)
        srd5.conn.commit()

    # Truck
    def getOccupied2(self):
        srd6 = space_reservation_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None,
                                         None, None, None)
        srd6.connect_to_database2()
        #
        cursor = srd6.conn.cursor()
        cursor.execute(srd6.sql7)
        srd6.conn.commit()

        data4 = pd.read_sql(srd6.sql7, srd6.conn)
        print("The currently available parking spaces are: ")
        print(data4)
        spacechoose2 = input("Please select the parking space you want to reserve: ")

        srd7 = space_reservation_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None,
                                         None, None, spacechoose2)
        srd7.database_operation4()
        cursor = srd7.conn.cursor()
        cursor.execute(srd7.sql8)
        srd7.conn.commit()

        srd8 = space_reservation_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None,
                                         None, None, spacechoose2)
        srd8.database_operation5()
        cursor = srd8.conn.cursor()
        cursor.execute(srd8.sql9)
        srd8.conn.commit()

    # Govern
    def getOccupied3(self):
        srd9 = space_reservation_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None,
                                         None, None, None)
        srd9.connect_to_database3()
        #
        cursor = srd9.conn.cursor()
        cursor.execute(srd9.sql10)
        srd9.conn.commit()

        data6 = pd.read_sql(srd9.sql10, srd9.conn)
        print("The currently available parking spaces are: ")
        print(data6)
        spacechoose3 = input("Please select the parking space you want to reserve: ")

        srd10 = space_reservation_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None,
                                          None, None, spacechoose3)
        srd10.database_operation6()
        cursor = srd10.conn.cursor()
        cursor.execute(srd10.sql11)
        srd10.conn.commit()

        srd11 = space_reservation_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None,
                                          None, None, spacechoose3)
        srd11.database_operation7()
        cursor = srd11.conn.cursor()
        cursor.execute(srd11.sql12)
        srd11.conn.commit()