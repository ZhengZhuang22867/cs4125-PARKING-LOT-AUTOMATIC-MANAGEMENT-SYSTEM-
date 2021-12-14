from Data.Database import database


class modify_parking_status_daolmpl:
    def __init__(self, conn, sql, sql1, n):
        self.conn = conn
        self.sql = sql
        self.sql1 = sql1
        self.n = n

    def connect_to_databse(self):
        d = database()
        self.conn = d.get_conn()
        self.sql = d.create_cmd('SELECT * FROM parking_space')

    def database_operation(self):
        d = database()
        self.conn = d.get_conn()
        self.sql1 = f'UPDATE parking_space SET space_state = "Maintenance" WHERE space_id = \'{self.n}\''
