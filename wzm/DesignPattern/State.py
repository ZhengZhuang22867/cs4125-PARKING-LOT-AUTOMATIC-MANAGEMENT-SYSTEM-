from Data.Daolmpl.Space_reservation_Daolmpl import space_reservation_daolmpl
from Data.Daolmpl.Space_reservation_cancel_Daolmpl import space_reservation_cancel_daolmpl


class state:
    def __init__(self):
        pass

    def getAvailable(self):
        srcd = space_reservation_cancel_daolmpl(self.name, None, None, None, None)
        srcd.connect_to_database()
        cursor = srcd.conn.cursor()
        cursor.execute(srcd.sql)
        srcd.conn.commit()
        raise NotImplementedError

    # Motor
    def getOccupied(self):
        srd = space_reservation_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None,
                                        None, None, None)
        srd.connect_to_database()
        #
        cursor = srd.conn.cursor()
        cursor.execute(srd.sql)
        srd.conn.commit()
        raise NotImplementedError

    # Car
    def getOccupied1(self):
        srd3 = space_reservation_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None,
                                         None, None, None)
        srd3.connect_to_database1()
        #
        cursor = srd3.conn.cursor()
        cursor.execute(srd3.sql4)
        srd3.conn.commit()
        raise NotImplementedError

    # Truck
    def getOccupied2(self):
        srd6 = space_reservation_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None,
                                         None, None, None)
        srd6.connect_to_database2()
        #
        cursor = srd6.conn.cursor()
        cursor.execute(srd6.sql7)
        srd6.conn.commit()
        raise NotImplementedError

    # Govern
    def getOccupied3(self):
        srd9 = space_reservation_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None,
                                         None, None, None)
        srd9.connect_to_database3()
        #
        cursor = srd9.conn.cursor()
        cursor.execute(srd9.sql10)
        srd9.conn.commit()
        raise NotImplementedError