from Data.Database import database


class info_improve_daolmpl:
    def __init__(self, name, tele, conn, sql, sql2):
        self.name = name
        self.tele = tele
        self.conn = conn
        self.sql = sql
        self.sql2 = sql2

    def connect_to_database(self):
        d = database()
        self.conn = d.get_conn()
        self.sql = d.create_cmd('SELECT * FROM user_info')

    def database_operation(self):
        d = database()
        self.conn = d.get_conn()
        self.sql2 = d.create_cmd(f'UPDATE user_info SET user_tele = \'{self.tele}\' WHERE user_name = \'{self.name}\'')
