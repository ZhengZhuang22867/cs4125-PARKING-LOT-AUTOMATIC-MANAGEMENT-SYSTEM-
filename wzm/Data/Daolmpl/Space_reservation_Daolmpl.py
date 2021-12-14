from Data.Database import database


class space_reservation_daolmpl:
    def __init__(self, name, conn, sql, sql2, sql3, sql4, sql5, sql6, sql7, sql8, sql9, sql10, sql11, sql12, spacechoose):
        self.name = name
        self.conn = conn
        self.sql = sql
        self.sql2 = sql2
        self.sql3 = sql3
        self.sql4 = sql4
        self.sql5 = sql5
        self.sql6 = sql6
        self.sql7 = sql7
        self.sql8 = sql8
        self.sql9 = sql9
        self.sql10 = sql10
        self.sql11 = sql11
        self.sql12 = sql12
        self.spacechoose = spacechoose


    def connect_to_database(self):
        d = database()
        self.conn = d.get_conn()
        self.sql = 'SELECT space_id FROM parking_space WHERE space_type = "Motor" and space_state = "Available";'

    def connect_to_database1(self):
        d = database()
        self.conn = d.get_conn()
        self.sql4 = 'SELECT space_id FROM parking_space WHERE space_type = "Car" and space_state = "Available";'

    def connect_to_database2(self):
        d = database()
        self.conn = d.get_conn()
        self.sql7 = 'SELECT space_id FROM parking_space WHERE space_type = "Truck" and space_state = "Available"'

    def connect_to_database3(self):
        d = database()
        self.conn = d.get_conn()
        self.sql10 = 'SELECT space_id FROM parking_space WHERE space_type = "Govern" and space_state = "Available";'

    def database_operation(self):
        d = database()
        self.conn = d.get_conn()
        self.sql2 = f'UPDATE parking_space SET space_state = "Occupied" WHERE space_id = \"{self.spacechoose}\"'

    def database_operation1(self):
        d = database()
        self.conn = d.get_conn()
        self.sql3 = f'UPDATE reservation_info SET space_id = \"{self.spacechoose}\", space_type = "Motor" WHERE user_name = \"{self.name}\"'

    def database_operation2(self):
        d = database()
        self.conn = d.get_conn()
        self.sql5 = f'UPDATE parking_space SET space_state = "Occupied" WHERE space_id = \"{self.spacechoose}\"'

    def database_operation3(self):
        d = database()
        self.conn = d.get_conn()
        self.sql6 = f'UPDATE reservation_info SET space_id = \"{self.spacechoose}\", space_type = "Car" WHERE user_name = \"{self.name}\"'

    def database_operation4(self):
        d = database()
        self.conn = d.get_conn()
        self.sql8 = f'UPDATE parking_space SET space_state = "Occupied" WHERE space_id = \"{self.spacechoose}\"'

    def database_operation5(self):
        d = database()
        self.conn = d.get_conn()
        self.sql9 = f'UPDATE reservation_info SET space_id = \"{self.spacechoose}\", space_type = "Truck" WHERE user_name = \'{self.name}\''

    def database_operation6(self):
        d = database()
        self.conn = d.get_conn()
        self.sql11 = f'UPDATE parking_space SET space_state = "Occupied" WHERE space_id = \'{self.spacechoose}\''

    def database_operation7(self):
        d = database()
        self.conn = d.get_conn()
        self.sql12 = f'UPDATE reservation_info SET space_id = \"{self.spacechoose}\", space_type = "Govern" WHERE user_name = \'{self.name}\''
