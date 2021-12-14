from Data.Database import database


class pay_fee_daolmpl:
    def __init__(self, name, conn, query, query2, query3, query4, query5, query6, query7, query8, tt, pt, money):
        self.name = name
        self.conn = conn
        self.query = query
        self.query2 = query2
        self.query3 = query3
        self.query4 = query4
        self.query5 = query5
        self.query6 = query6
        self.query7 = query7
        self.query8 = query8
        self.tt = tt
        self.pt = pt
        self.money = money

    def connect_to_database(self):
        d = database()
        self.conn = d.get_conn()
        self.query = d.create_cmd(f"SELECT space_type FROM reservation_info WHERE user_name = \"{self.name}\"")

    def datebase_operation(self):
        d = database()
        self.conn = d.get_conn()
        self.query2 = d.create_cmd(
            f'UPDATE reservation_info SET parking_time = \'{self.pt}\' WHERE user_name = \'{self.name}\'')

    # Returns the current total parking time
    def database_total_parking_time(self):
        d = database()
        self.conn = d.get_conn()
        self.query7 = d.create_cmd(f"SELECT tot_parking_time FROM user_info WHERE user_name = \"{self.name}\"")

    # Update total parking times
    def database_total_parking_time2(self):
        d = database()
        self.conn = d.get_conn()
        self.query8 = d.create_cmd(f'UPDATE user_info SET tot_parking_time = \'{self.tt}\' WHERE user_name = \'{self.name}\'')

    def database_operation2(self):
        d = database()
        self.conn = d.get_conn()
        self.query3 = d.create_cmd(f"SELECT user_lvl FROM reservation_info WHERE user_name = \"{self.name}\"")

    def database_operation3(self):
        d = database()
        self.conn = d.get_conn()
        self.query4 = d.create_cmd(
            f"UPDATE user_acc SET acc_balance = \"{self.money}\" WHERE user_name = \"{self.name}\"")

    def database_operation4(self):
        d = database()
        self.conn = d.get_conn()
        self.query5 = d.create_cmd(
            f'UPDATE parking_space p, reservation_info r SET p.space_state = "Available" WHERE r.space_id = p.space_id')

    def database_operation5(self):
        d = database()
        self.conn = d.get_conn()
        self.query6 = d.create_cmd(
            f'UPDATE reservation_info SET space_id = null, space_type = null, parking_time = null WHERE user_name = \'{self.name}\'')
