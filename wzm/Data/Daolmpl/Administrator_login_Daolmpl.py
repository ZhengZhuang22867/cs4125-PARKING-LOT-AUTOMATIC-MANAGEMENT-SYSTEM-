from Data.Database import database


class administrator_login_daolmpl:
    def __init__(self, conn, sql):
        self.conn = conn
        self.sql = sql

    def connect_to_database(self):
        d = database()
        self.conn = d.get_conn()
        self.sql = d.create_cmd('SELECT * FROM adm_acc')
