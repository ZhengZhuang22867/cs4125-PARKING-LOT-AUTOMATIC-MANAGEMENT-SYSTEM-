from Data.Database import database


class view_reservation_info_daolmpl:
    def __init__(self, name, conn, sql):
        self.name = name
        self.conn = conn
        self.sql = sql

    def connect_to_database(self):
        d = database()
        self.conn = d.get_conn()
        self.sql = f'SELECT * FROM reservation_info WHERE user_name = \'{self.name}\''