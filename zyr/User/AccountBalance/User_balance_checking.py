from Data.Database import database
from Data.Daolmpl.Balance_checking_Daolmpl import balance_checking_daolmpl

class user_balance_checking:
    def __init__(self, name):
        self.name = name
        self.b = None

    def balance_checking(self):
        # connect to the database
        d = database()
        bcd = balance_checking_daolmpl(self.name, None, None)
        bcd.connect_to_database()
        # Manipulates a pointer to a database
        cursor = bcd.conn.cursor()
        cursor.execute(bcd.query)
        bcd.conn.commit()
        # Save data from the database to variables in Python
        r = cursor.fetchall()
        for i in r:
            self.b = i[0]
            print("Dear", self.name, ", your balance is: ", self.b)

        d.close_conn()
