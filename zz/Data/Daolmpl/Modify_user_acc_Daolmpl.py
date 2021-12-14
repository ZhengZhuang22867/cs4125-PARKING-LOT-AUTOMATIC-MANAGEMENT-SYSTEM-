from Data.Database import database


class modify_user_acc_daolmpl:
    def __init__(self, conn, query, query2, query3, query4, query5, query6, query7, query8):
        self.conn = conn
        self.query = query
        self.query2 = query2
        self.query3 = query3
        self.query4 = query4
        self.query5 = query5
        self.query6 = query6
        self.query7 = query7
        self.query8 = query8

    def connect_to_databse(self):
        d = database()
        self.conn = d.get_conn()
        self.query = d.create_cmd(f"SELECT * FROM user_acc")

    def delete_user_acc(self, name):
        d = database()
        self.conn = d.get_conn()
        self.query2 = d.create_cmd(f"DELETE FROM user_acc WHERE user_name = \"{name}\"")
        self.query3 = d.create_cmd(f"DELETE FROM user_info WHERE user_name = \"{name}\"")
        self.query4 = d.create_cmd(f"DELETE FROM reservation_info WHERE user_name = \"{name}\"")
        self.query5 = d.create_cmd(f"DELETE FROM car_info WHERE user_name = \"{name}\"")


    def change_user_lvl(self, name, new_lvl):
        d = database()
        self.conn = d.get_conn()
        self.query6 = d.create_cmd(f"UPDATE user_acc SET user_lvl = \"{new_lvl}\" WHERE user_name = \"{name}\"")
        self.query7 = d.create_cmd(f"UPDATE user_info SET user_lvl = \"{new_lvl}\" WHERE user_name = \"{name}\"")
        self.query8 = d.create_cmd(f"UPDATE reservation_info SET user_lvl = \"{new_lvl}\" WHERE user_name = \"{name}\"")





