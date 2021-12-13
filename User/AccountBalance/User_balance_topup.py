from Data.Daolmpl.Balance_topup_Daolmpl import balance_topup_daolmpl
from Data.Database import database
from User.AccountBalance.User_balance_checking import user_balance_checking


class user_balance_topup:
    def __init__(self, name):
        self.name = name

    def topup(self):
        print("Dear", self.name,
              ", Our company currently has top-up offers: 5 for 50, 20 for 100, 150 for 500 and 400 for 1000!")
        # 连接数据库并先返回原本账户的余额
        d = database()

        btd = balance_topup_daolmpl(self.name, None, None, None, None, None)
        btd.connect_to_database()
        #
        cursor = btd.conn.cursor()
        cursor.execute(btd.query)
        btd.conn.commit()
        # 将查到的数据存入r中，并用数组的形式返回出来
        r = cursor.fetchall()
        for i in r:
            b = i[0]
            print("Dear", self.name, ", your current balance is:", b)
            #返回的余额 b 是string类型

        # 充值规则
        cmd = int(input("Please enter the amount you want to top up:"))
        money = cmd
        if money < 50:
            money += float(b)
        elif 50 <= money < 100:
            money += 5 + float(b)
        elif 100 <= money < 500:
            money += 20 + float(b)
        elif 500 <= money < 1000:
            money += 150 + float(b)
        else:
            money += 400 + float(b)

        # 操作数据库
        btd2 = balance_topup_daolmpl(self.name, None, None, None, None, money)
        btd2.update_to_database()

        cursor = btd2.conn.cursor()
        cursor.execute(btd2.query2)
        cursor.execute(btd2.query3)
        btd2.conn.commit()

        # 显示充值后余额
        bc = user_balance_checking(self.name)
        bc.balance_checking()
        d.close_conn()

