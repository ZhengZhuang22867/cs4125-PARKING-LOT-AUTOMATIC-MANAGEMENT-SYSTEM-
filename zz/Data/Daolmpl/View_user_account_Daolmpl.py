from Data.Database import database


class view_user_account_daolmpl:
    def __init__(self, conn, sql):
        self.conn = conn
        self.sql = sql

    def connect_to_database(self):
        # connect to mysql database
        d = database()
        self.conn = d.get_conn()
        # choose'user_account'in table'user_acc'
        self.sql = d.create_cmd("select * from user_acc")
