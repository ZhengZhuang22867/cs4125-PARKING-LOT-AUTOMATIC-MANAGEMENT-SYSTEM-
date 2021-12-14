from Administrator.Modify_parking_status.Administrator_modify_parking_status import administrator_modify_parking_status
from Administrator.View_user_account.Administrator_view_user_account import administrator_view_user_account
from Administrator.Modify_user_acc.Administrator_modify_user_acc import administrator_modify_user_acc
from UI.Ui_controller import ui_controller

class administrator_controller:
    def __init__(self, name):
        self.name = name

    def adm_controller(self):
        while True:
            u = ui_controller()
            u.adm_interface(self.name)
            cmd = int(input("Please enter the instruction number："))
            #View user account
            if cmd == 1:
                avuc = administrator_view_user_account()
                avuc.view_user_account()

            #Modify user information(Not finish)
            elif cmd == 2:#modify user account information
                amui = administrator_modify_user_acc(self.name)
                amui.modify_user_acc()

            #Modify parking status
            elif cmd == 3:
                mps = administrator_modify_parking_status()
                mps.modify_parking_status()

            elif cmd == 4:
                break