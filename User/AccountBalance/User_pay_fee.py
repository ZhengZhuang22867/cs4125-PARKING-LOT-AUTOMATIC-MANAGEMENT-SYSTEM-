from Data.Daolmpl.Pay_fee_Daolmpl import pay_fee_daolmpl
from Data.Database import database
from User.AccountBalance.User_balance_checking import user_balance_checking
from UI.Ui_controller import ui_controller
from User.Level_update.User_level_update import user_level_update


class user_pay_fee:
    def __init__(self, name):
        self.name = name

    def pay(self):
        #确定车辆类型
        #连接数据库并执行指令返回space_type
        d = database()

        pfd = pay_fee_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None, None)
        pfd.connect_to_database()

        cursor = pfd.conn.cursor()
        cursor.execute(pfd.query)
        pfd.conn.commit()

        #将查到的数据存入r中，并用数组的形式返回出来
        result = cursor.fetchall()
        for i in result:
            type = i[0]
            # 返回的用户等级 lvl 是string类型

        #判断用户是否有停车记录，如果没有则直接提示后退出；如果有则继续
        if type == None:
            print("You have no parking record!")
        else:
            #type现在代表车辆类型

            #确定停车时间：
            #for type Motor: first half hour is free; one euros an hour; fee not exceed 20 euros in the first 24 hours,
                #not exceed 25 euros in the second 24 hours and 30 euros for every 24 hours from the third
            #for type Car: first half hour is free; two euros an hour;  fee not exceed 40 euros in the first 24 hours,
                #not exceed 50 euros in the second 24 hours and 60 euros for every 24 hours from the third
            #for type Truck: first half hour is free; four euros an hour; fee not exceed 80 euros in the first 24 hours,
                #not exceed 100 euros in the second 24 hours and 120 euros for every 24 hours from the third

            cmd = int(input("Please enter your parking time: "))
            pt = cmd

            # 更新本次停车的时间
            pfd2 = pay_fee_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, pt, None)
            pfd2.datebase_operation()

            cursor = pfd2.conn.cursor()
            cursor.execute(pfd2.query2)
            pfd2.conn.commit()

            # 将之前用户的停车时间返回
            pdf7 = pay_fee_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None, None)
            pdf7.database_total_parking_time()

            cursor = pdf7.conn.cursor()
            cursor.execute(pdf7.query7)
            pdf7.conn.commit()

            result7 = cursor.fetchall()
            for i in result7:
                old_total_time = i[0]


            # 将新的停车时间加入总停车时间
            tt = old_total_time + pt
            pdf8 = pay_fee_daolmpl(self.name, None, None, None, None, None, None, None, None, None, tt, None, None)
            pdf8.database_total_parking_time2()

            cursor = pdf8.conn.cursor()
            cursor.execute(pdf8.query8)
            pdf8.conn.commit()


            # 确定用户等级：
            # level 0: nothing；Students and level 1: 10% discount; Employees and level 2: 20% discount
    
            # 连接数据库并执行指令返回user_lvl
            pfd3 = pay_fee_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None, None)
            pfd3.database_operation2()

            cursor = pfd3.conn.cursor()
            cursor.execute(pfd3.query3)
            pfd3.conn.commit()
    
            # 将查到的数据存入r中，并用数组的形式返回出来
            result3 = cursor.fetchall()
            for i in result3:
                lvl = int(i[0])#返回的用户等级 lvl 将string类型转换为int类型

            fee = 0 #默认停车费为0
            
            #判断用户等级来计算停车费用
            if lvl == 0:
                if type == "Motor":
                    if pt <= 0.5:
                        fee = 0
                    elif pt <= 20:
                        fee = 1 * pt
                    elif pt <= 24:
                        fee = 20
                    elif pt <= 48:
                        fee = 20 + 25
                    elif pt <= 72:
                        fee = 20 + 25 + 30
                    else:
                        fee = 20 + 25 + 30 * ((pt-24)/24)
                elif type == "Car":
                    if pt <= 0.5:
                        fee = 0
                    elif pt < 20:
                        fee = 2 * pt
                    elif pt <= 24:
                        fee = 40
                    elif pt <= 48:
                        fee = 40 + 50
                    elif pt <= 72:
                        fee = 40 + 50 + 60
                    else:
                        fee = 40 + 50 + 60 * ((pt-24)/24)
                elif type == "Truck":
                    if pt <= 0.5:
                        fee = 0
                    elif pt < 20:
                        fee = 4 * pt
                    elif pt <= 24:
                        fee = 80
                    elif pt <= 48:
                        fee = 80 + 100
                    elif pt <= 72:
                        fee = 80 + 100 + 120
                    else:
                        fee = 80 + 100 + 120 * ((pt-24)/24)
                else: #type == "Govern"
                    fee = 0
            elif lvl == 1:
                if type == "Motor":
                    if pt <= 0.5:
                        fee = 0
                    elif pt <= 20:
                        fee = 1 * pt * 0.9
                    elif pt <= 24:
                        fee = 20 * 0.9
                    elif pt <= 48:
                        fee = (20 + 25) * 0.9
                    elif pt <= 72:
                        fee = (20 + 25 + 30) * 0.9
                    else:
                        fee = (20 + 25 + 30 * ((pt-24)/24)) * 0.9
                elif type == "Car":
                    if pt <= 0.5:
                        fee = 0
                    elif pt < 20:
                        fee = 2 * pt * 0.9
                    elif pt <= 24:
                        fee = 40 * 0.9
                    elif pt <= 48:
                        fee = (40 + 50) * 0.9
                    elif pt <= 72:
                        fee = (40 + 50 + 60) * 0.9
                    else:
                        fee = (40 + 50 + 60 * ((pt-24)/24)) * 0.9
                elif type == "Truck":
                    if pt <= 0.5:
                        fee = 0
                    elif pt < 20:
                        fee = 4 * pt * 0.9
                    elif pt <= 24:
                        fee = 80 * 0.9
                    elif pt <= 48:
                        fee = (80 + 100) * 0.9
                    elif pt <= 72:
                        fee = (80 + 100 + 120) * 0.9
                    else:
                        fee = (80 + 100 + 120 * ((pt-24)/24)) * 0.9
                else:
                    fee = 0
            else: # lvl == 2
                if type == "Motor":
                    if pt <= 0.5:
                        fee = 0
                    elif pt <= 20:
                        fee = 1 * pt * 0.8
                    elif pt <= 24:
                        fee = 20 * 0.8
                    elif pt <= 48:
                        fee = (20 + 25) * 0.8
                    elif pt <= 72:
                        fee = (20 + 25 + 30) * 0.8
                    else:
                        fee = (20 + 25 + 30 * ((pt-24)/24)) * 0.8
                elif type == "Car":
                    if pt <= 0.5:
                        fee = 0
                    elif pt < 20:
                        fee = 2 * pt * 0.8
                    elif pt <= 24:
                        fee = 40 * 0.8
                    elif pt <= 48:
                        fee = (40 + 50) * 0.8
                    elif pt <= 72:
                        fee = (40 + 50 + 60) * 0.8
                    else:
                        fee = (40 + 50 + 60 * ((pt-24)/24)) * 0.8
                elif type == "Truck":
                    if pt <= 0.5:
                        fee = 0
                    elif pt < 20:
                        fee = 4 * pt * 0.8
                    elif pt <= 24:
                        fee = 80 * 0.8
                    elif pt <= 48:
                        fee = (80 + 100) * 0.8
                    elif pt <= 72:
                        fee = (80 + 100 + 120) * 0.8
                    else:
                        fee = (80 + 100 + 120 * ((pt-24)/24)) * 0.8
                else:
                    fee = 0

            print("Dear", self.name, ", Your parking fare is:", fee)

            ubc = user_balance_checking(self.name)
            ubc.balance_checking()
            balance = float(ubc.b)

            if balance >= fee:
                while True:
                    u = ui_controller()
                    u.pay_fare_interface()
                    cmd = float(input("Please enter the instruction number："))
                    if cmd == 1:#从余额中扣除本次费用
                        money = balance - fee
                        pfd4 = pay_fee_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None, money)
                        pfd4.database_operation3()
                        cursor = pfd4.conn.cursor()
                        cursor.execute(pfd4.query4)
                        pfd4.conn.commit()

                        #更新'parking_space'车位信息和用户停车信息
                        pfd5 = pay_fee_daolmpl(None, None, None, None, None, None, None, None, None, None, None, None, None)
                        pfd5.database_operation4()
                        cursor = pfd5.conn.cursor()
                        cursor.execute(pfd5.query5)
                        pfd5.conn.commit()
                        #更新'reservation_info'中的信息
                        pfd6 = pay_fee_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None, None)
                        pfd6.database_operation5()
                        cursor = pfd6.conn.cursor()
                        cursor.execute(pfd6.query6)
                        pfd6.conn.commit()

                        print("Payment successful! Your current account balance is: ", money)
                        d.close_conn()
                        break
                    elif cmd == 2:
                        print("You have a charge to pay......")
                        break
            else:
                print("Your balance is insufficient, please top it up!")






