from Data.Daolmpl.Balance_topup_Daolmpl import balance_topup_daolmpl
from Data.Database import database
from User.AccountBalance.User_balance_checking import user_balance_checking


class user_balance_topup:
    def __init__(self, name):
        self.name = name

    def topup(self):
        print("Dear", self.name,
              ", Our company currently has top-up offers: 5 for 50, 20 for 100, 150 for 500 and 400 for 1000!")
        # Connect to the database and return the original account balance first
        d = database()

        btd = balance_topup_daolmpl(self.name, None, None, None, None, None)
        btd.connect_to_database()
        #
        cursor = btd.conn.cursor()
        cursor.execute(btd.query)
        btd.conn.commit()
        # Store the found data into R and return it as an array
        r = cursor.fetchall()
        for i in r:
            b = i[0]
            print("Dear", self.name, ", your current balance is:", b)
            #The returned balance B is a string

        # Top-up rules
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

        # Operating database
        btd2 = balance_topup_daolmpl(self.name, None, None, None, None, money)
        btd2.update_to_database()

        cursor = btd2.conn.cursor()
        cursor.execute(btd2.query2)
        cursor.execute(btd2.query3)
        btd2.conn.commit()

        # Display the balance after recharge
        bc = user_balance_checking(self.name)
        bc.balance_checking()
        d.close_conn()

