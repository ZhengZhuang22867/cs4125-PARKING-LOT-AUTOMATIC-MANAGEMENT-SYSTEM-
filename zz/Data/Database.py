import pymysql
import pandas as pd

class database:
    # connect to database
    def __init__(self):
        self.get_conn()

    # get connected
    def get_conn(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='12345678',
            db='cs4125',
            charset='utf8'
        )

        return self.conn

    # create instruction
    def create_cmd(self, sql):
        return sql

    # close connection
    def close_conn(self):
        self.conn.close()

