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
        # 操作数据库的指针
        cursor = bcd.conn.cursor()
        cursor.execute(bcd.query)
        bcd.conn.commit()
        # 将数据库中的数据保存到python中的变量中
        r = cursor.fetchall()
        for i in r:
            self.b = i[0]
            print("Dear", self.name, ", your balance is: ", self.b)

        d.close_conn()
