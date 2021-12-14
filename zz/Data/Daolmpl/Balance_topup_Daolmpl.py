from Data.Database import database


class balance_topup_daolmpl:
    def __init__(self, name, conn, query, query2, query3, money):
        self.name = name
        self.conn = conn
        self.query = query
        self.query2 = query2
        self.query3 = query3
        self.money = money

    def connect_to_database(self):
        # connect to database
        d = database()
        self.conn = d.get_conn()
        self.query = d.create_cmd(f"SELECT acc_balance FROM user_acc WHERE user_name = \"{self.name}\"")

    def update_to_database(self):
        d = database()
        self.conn = d.get_conn()
        self.query2 = d.create_cmd(f"UPDATE user_acc SET acc_balance = \"{self.money}\" WHERE user_name = \"{self.name}\"")
        self.query3 = d.create_cmd(f"UPDATE user_info SET acc_balance = \"{self.money}\" WHERE user_name = \"{self.name}\"")

