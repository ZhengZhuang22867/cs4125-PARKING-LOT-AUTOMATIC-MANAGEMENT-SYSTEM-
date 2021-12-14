import pymysql

from Data.Daolmpl.Administrator_login_Daolmpl import administrator_login_daolmpl
from Data.Database import database
'''
内含万恶之源！！！！看这个怎么连接数据库和操作数据库
'''

class administrator_login:
    # 获取管理员信息（登陆用）
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.deter = None

    def get_admacc(self):
        '''
        # 万恶之源!!!!!!!!!! 以后可以看这个连接数据库
        # 连接mysql
        conn = pymysql.connect(host='127.0.0.1', user='root', password='12345678',
                               db='cs4125', charset="utf8")

        sql = 'SELECT * FROM adm_acc'
        '''
        d = database()
        ald = administrator_login_daolmpl(None, None)
        ald.connect_to_database()

        # Use the cursor() method to get the action cursor
        cursor = ald.conn.cursor()

        # Execute SQL statements using the execute() method
        cursor.execute(ald.sql)

        # Use the fetchall() method to get all the data
        result = cursor.fetchall()

        # Store the data as a dictionary in result
        result = [dict(zip([k[0] for k in cursor.description], row)) for row in result]

        # close connect
        cursor.close()
        # conn.close()
        d.close_conn()
        return result

    def adm_login(self):
        # Obtain the administrator username and password
        result = self.get_admacc()
        ulist = []
        plist = []
        for item in result:
            ulist.append(item['adm_name'])
            plist.append(item['adm_password'])
        self.deter = True
        for i in range(len(ulist)):
            while True:
                if self.name == ulist[i] and self.password == plist[i]:
                    print("Login successful!")
                    self.deter = False
                    break
                else:
                    break


