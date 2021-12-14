#from User.Register import Register
#from User.User_login import user_login
#from User.User_action import user_action
#from Administrator.Administrator_action import administrator_action
#from Administrator.Administrator_login import administrator_login
from DesignPattern.Factory import Factory
from UI.Ui_controller import ui_controller
from Data.System_management.System_management_controller import system_management_controller

print("******************* Welcome to Park Administrator System *******************")

while True:
    u = ui_controller()
    u.main_interface()
    cmd = int(input("Please enter the instruction number："))

    #user login and continue user part
    if cmd == 1:
        user_name = input("Please enter your user name: ")
        user_password = input("Please enter your password: ")

        # user login and judgement
        smc = system_management_controller(user_name, user_password, False, False)
        smc.user_login_judgement()
        if smc.beta == True:
            break

        # This method enters ‘user_interface’ and performs operations that the user can do
        f = Factory()
        a = f.getUser_controller(user_name)
        a.user_controller()

    #administrator login
    elif cmd == 2:
        adm_name = input("Please enter your administrator name: ")
        adm_password = input("Please enter your administrator password: ")

        # administrator login and judgement
        smc = system_management_controller(adm_name, adm_password, False, False)
        smc.adm_login_judgement()
        if smc.gamma == True:
            break

        # This method enters ‘adm_interface’ and performs operations that the administrators can do
        f = Factory()
        aa = f.getAdministrator_action(adm_name)
        aa.adm_controller()

    #user register
    elif cmd == 3:
        user_name = input("Please enter your user name: ")
        user_password = input("Please enter your password: ")
        car_num = input("Please enter your car number: ")

        smc = system_management_controller(user_name, user_password, False, False)
        smc.user_register(car_num)

    #quit system
    elif cmd == 4:
        print('See you!')
        break
