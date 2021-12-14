import pymysql
from DesignPattern.Observer import observer

class user_register:
    def __init__(self, name, password, carnum):
        self.name = name
        self.password = password
        self.carnum = carnum

    # 获取用户信息（登录用）
    def get_useracc(self):
        # connect to mysql database
        conn = pymysql.connect(host='127.0.0.1', user='root', password='12345678',
                               db='cs4125', charset="utf8")

        sql = 'SELECT * FROM user_acc'

        # Use the cursor() method to get the action cursor
        cursor = conn.cursor()

        # Execute SQL statements using the execute() method
        cursor.execute(sql)

        # Use the fetchall() method to get all the data
        result = cursor.fetchall()

        # Store the data as a dictionary in result
        result = [dict(zip([k[0] for k in cursor.description], row)) for row in result]

        # close database
        cursor.close()
        conn.close()
        return result

    def insert_useracc(self):
        # connect to database
        conn = pymysql.connect(host='127.0.0.1', user='root', password='12345678',
                               db='cs4125', charset="utf8")

        sql = 'SELECT * FROM user_acc'
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        result = [dict(zip([k[0] for k in cursor.description], row)) for row in result]
        ulist = []
        for item in result:
            ulist.append(item['user_name'])
        cursor = conn.cursor()

        # Set the account balance and user level of the new user to 0
        acc_balance = 0
        user_lvl = 0
        cursor.execute(
            'INSERT INTO user_acc(user_name,user_password,car_num, acc_balance, user_lvl) VALUES(%s,%s,%s,%s,%s)',
            (self.name, self.password, self.carnum, acc_balance, user_lvl))
        if self.name == '' or self.password == '':
            conn.rollback()
            print("Registration failed!")
        elif self.name in ulist:
            print("Username already exists!")
        else:
            # Synchronously import the created new user name and license plate number into the 'CAR_info',' Reservation_info 'and 'user_info' tables

            cursor.execute('INSERT INTO car_info(car_num, user_name) VALUES(%s, %s)', (self.carnum, self.name))
            '''
            ob = observer()
            ob.update(conn.cursor(),self.carnum, self.name)
            '''


            cursor.execute('INSERT INTO reservation_info(user_name, car_num, user_lvl) VALUES(%s,%s,%s)',
                           (self.name, self.carnum, user_lvl))
            cursor.execute('INSERT INTO user_info(user_name, car_num, user_lvl) VALUES(%s,%s,%s)',
                           (self.name, self.carnum, user_lvl))

            #
            conn.commit()

            print("Registration success!")
        cursor.close()
        conn.close()

