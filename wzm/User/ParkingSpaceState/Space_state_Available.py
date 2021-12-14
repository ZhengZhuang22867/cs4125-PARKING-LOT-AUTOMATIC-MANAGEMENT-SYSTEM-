from Data.Daolmpl.Space_reservation_cancel_Daolmpl import space_reservation_cancel_daolmpl
from DesignPattern.State import state


class space_state_available(state):

    def __init__(self, name):
        self.name = name

    def getAvailable(self):
        srcd = space_reservation_cancel_daolmpl(self.name, None, None, None, None)
        srcd.connect_to_database()
        cursor = srcd.conn.cursor()
        cursor.execute(srcd.sql)
        srcd.conn.commit()

        srcd1 = space_reservation_cancel_daolmpl(self.name, None, None, None, None)
        srcd1.database_operation()
        cursor = srcd1.conn.cursor()
        cursor.execute(srcd1.sql2)
        srcd1.conn.commit()

        srcd2 = space_reservation_cancel_daolmpl(self.name, None, None, None, None)
        srcd2.database_operation1()
        cursor = srcd2.conn.cursor()
        cursor.execute(srcd2.sql3)
        srcd2.conn.commit()