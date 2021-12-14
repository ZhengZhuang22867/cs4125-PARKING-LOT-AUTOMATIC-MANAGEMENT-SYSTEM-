from Data.Database import database


class user_register_daolmpl:
    def __init__(self, name, conn, sql, sql2, sql3, sql4, sql5, password, carnum, acc_balance, user_lvl):
        self.conn = conn
        self.sql = sql
        self.sql2 = sql2
        self.sql3 = sql3
        self.sql4 = sql4
        self.sql5 = sql5
        self.name = name
        self.password = password
        self.carnum = carnum
        self.acc_balance = acc_balance
        self.user_lvl = user_lvl

    def connect_to_database(self):
        d = database()
        self.conn = d.get_conn()
        self.sql = d.create_cmd('SELECT * FROM user_acc')

    def database_operation(self):
        d = database()
        self.conn = d.get_conn()
        self.sql2 = f'INSERT INTO user_acc(user_name,user_password,car_num, acc_balance, user_lvl) VALUES(\"{self.name}\",\"{self.password}\",\"{self.carnum}\",\"{self.acc_balance}\",\"{self.user_lvl}\")'

    def databse_operation1(self):
        d = database()
        self.conn = d.get_conn()
        self.sql3 = f'INSERT INTO car_info(car_num, user_name) VALUES(\"{self.carnum}\", \"{self.name}\")'

    def database_operation2(self):
        d = database()
        self.conn = d.get_conn()
        self.sql4 = f'INSERT INTO reservation_info(user_name, car_num, user_lvl) VALUES(\"{self.name}\",\"{self.carnum}\",\"{self.user_lvl}\")'

    def database_operation3(self):
        d = database()
        self.conn = d.get_conn()
        self.sql5 = f'INSERT INTO user_info(user_name, car_num, user_lvl) VALUES(\"{self.name}\",\"{self.carnum}\",\"{self.user_lvl}\")'
