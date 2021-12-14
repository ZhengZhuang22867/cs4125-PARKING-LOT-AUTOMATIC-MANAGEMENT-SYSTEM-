from Data.Daolmpl.Pay_fee_Daolmpl import pay_fee_daolmpl
from Data.Database import database
from User.AccountBalance.User_balance_checking import user_balance_checking
from UI.Ui_controller import ui_controller
from User.Level_update.User_level_update import user_level_update


class user_pay_fee:
    def __init__(self, name):
        self.name = name

    def pay(self):
        #Determine vehicle type
        #Connect to the database and execute the directive to return space_type
        d = database()

        pfd = pay_fee_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None, None)
        pfd.connect_to_database()

        cursor = pfd.conn.cursor()
        cursor.execute(pfd.query)
        pfd.conn.commit()

        #Store the found data into R and return it as an array
        result = cursor.fetchall()
        for i in result:
            type = i[0]
            # The returned user level LVL is of type string

        #Judge whether the user has a parking record, if not, it will be directly prompted to exit; If so,
        # continueJudge whether the user has a parking record, if not, it will be directly prompted to exit; If so, continue
        if type == None:
            print("You have no parking record!")
        else:
            #Type now stands for vehicle type

            #Determine the parking time:
            #for type Motor: first half hour is free; one euros an hour; fee not exceed 20 euros in the first 24 hours,
                #not exceed 25 euros in the second 24 hours and 30 euros for every 24 hours from the third
            #for type Car: first half hour is free; two euros an hour;  fee not exceed 40 euros in the first 24 hours,
                #not exceed 50 euros in the second 24 hours and 60 euros for every 24 hours from the third
            #for type Truck: first half hour is free; four euros an hour; fee not exceed 80 euros in the first 24 hours,
                #not exceed 100 euros in the second 24 hours and 120 euros for every 24 hours from the third

            cmd = int(input("Please enter your parking time: "))
            pt = cmd

            # Update the time of this stop
            pfd2 = pay_fee_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, pt, None)
            pfd2.datebase_operation()

            cursor = pfd2.conn.cursor()
            cursor.execute(pfd2.query2)
            pfd2.conn.commit()

            # Returns the previous user's parking time
            pdf7 = pay_fee_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None, None)
            pdf7.database_total_parking_time()

            cursor = pdf7.conn.cursor()
            cursor.execute(pdf7.query7)
            pdf7.conn.commit()

            result7 = cursor.fetchall()
            for i in result7:
                old_total_time = i[0]


            # Add new parking time to total parking time
            tt = old_total_time + pt
            pdf8 = pay_fee_daolmpl(self.name, None, None, None, None, None, None, None, None, None, tt, None, None)
            pdf8.database_total_parking_time2()

            cursor = pdf8.conn.cursor()
            cursor.execute(pdf8.query8)
            pdf8.conn.commit()


            # Determine the user level：
            # level 0: nothing；Students and level 1: 10% discount; Employees and level 2: 20% discount
    
            # Connect to the database and execute the command to return user_LVL
            pfd3 = pay_fee_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None, None)
            pfd3.database_operation2()

            cursor = pfd3.conn.cursor()
            cursor.execute(pfd3.query3)
            pfd3.conn.commit()
    
            # Store the found data into R and return it as an array
            result3 = cursor.fetchall()
            for i in result3:
                lvl = int(i[0])#The returned user level LVL converts string to int

            fee = 0 #The default parking fee is 0
            
            #Calculate parking fees by judging user levels
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
                    if cmd == 1:#The cost will be deducted from the balance
                        money = balance - fee
                        pfd4 = pay_fee_daolmpl(self.name, None, None, None, None, None, None, None, None, None, None, None, money)
                        pfd4.database_operation3()
                        cursor = pfd4.conn.cursor()
                        cursor.execute(pfd4.query4)
                        pfd4.conn.commit()

                        #Update 'parking_space' parking information and user parking information
                        pfd5 = pay_fee_daolmpl(None, None, None, None, None, None, None, None, None, None, None, None, None)
                        pfd5.database_operation4()
                        cursor = pfd5.conn.cursor()
                        cursor.execute(pfd5.query5)
                        pfd5.conn.commit()
                        #Update the information in 'reservation_info'
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






