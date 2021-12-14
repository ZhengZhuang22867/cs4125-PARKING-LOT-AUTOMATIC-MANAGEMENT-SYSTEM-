from Data.Database import database
'''
万恶之源 之 如何将数据库的数值保存入python的变量中！！！！！
注意改变数字类型！！！！！
'''

class balance_checking_daolmpl:
    def __init__(self, name, conn, query):
        self.name = name
        self.conn = conn
        self.query = query

    def connect_to_database(self):
        # connnect to databse
        d = database()
        self.conn = d.get_conn()

        # create instruction
        self.query = d.create_cmd(f'SELECT acc_balance FROM cs4125.user_acc WHERE user_name = \'{self.name}\'')

