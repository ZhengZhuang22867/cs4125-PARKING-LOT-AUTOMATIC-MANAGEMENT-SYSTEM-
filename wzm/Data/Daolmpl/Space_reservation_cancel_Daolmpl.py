from Data.Database import database


class space_reservation_cancel_daolmpl:
    def __init__(self, name, conn, sql, sql2, sql3):
        self.name = name
        self.conn = conn
        self.sql = sql
        self.sql2 = sql2
        self.sql3 = sql3

    def connect_to_database(self):
        d = database()
        self.conn = d.get_conn()
        self.sql = 'UPDATE parking_space p, reservation_info r SET p.space_state = "Available" WHERE r.space_id = p.space_id'

    def database_operation(self):
        d = database()
        self.conn = d.get_conn()
        self.sql2 = f'UPDATE reservation_info SET space_id = null, space_type = null WHERE user_name = \'{self.name}\''

    def database_operation1(self):
        d = database()
        self.conn = d.get_conn()
        self.sql3 = 'SELECT * FROM reservation_info WHERE user_name = \'{self.name}\''
