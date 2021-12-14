from Data.Database import database


class level_update_daolmpl:
    def __init__(self, name, query, query2, query3, query4, query5, new_lvl):
        self.name = name
        self.query = query
        self.query2 = query2
        self.query3 = query3
        self.query4 = query4
        self.query5 = query5
        self.new_lvl = new_lvl


    def get_total_parking_time(self):
        d = database()
        self.conn = d.get_conn()
        self.query = d.create_cmd(f"SELECT tot_parking_time FROM user_info WHERE user_name = \"{self.name}\"")

    def change_user_level(self):
        d = database()
        self.conn = d.get_conn()
        self.query2 = d.create_cmd(f'UPDATE user_info SET user_lvl = \'{self.new_lvl}\' WHERE user_name = \'{self.name}\'')
        self.query3 = d.create_cmd(f'UPDATE user_acc SET user_lvl = \'{self.new_lvl}\' WHERE user_name = \'{self.name}\'')
        self.query4 = d.create_cmd(f'UPDATE reservation_info SET user_lvl = \'{self.new_lvl}\' WHERE user_name = \'{self.name}\'')

    def show_new_user_level(self):
        d = database()
        self.conn = d.get_conn()
        self.query5 = d.create_cmd(f"SELECT user_lvl FROM user_info WHERE user_name = \"{self.name}\"")


