from Administrator.Modify_user_acc.Change_user_level import change_user_level
from Administrator.Modify_user_acc.Delete_user_acc import delete_user_acc
from Administrator.View_user_account.Administrator_view_user_account import administrator_view_user_account
from UI.Ui_controller import ui_controller


class administrator_modify_user_acc:
    def __init__(self, name):
        self.name = name

    def modify_user_acc(self):
        while True:
            u = ui_controller()
            u.modify_user_acc_interface()
            cmd = int(input("Please enter the instruction number："))
            if cmd == 1:
                dua = delete_user_acc()
                dua.view_user_acc()
                dua.connnect_to_databse()

                name = input("Please enter an username of the account you want to modify:")

                dua.operate_datebase(name)
                print(f"Successfully modified, user {name} has been deleted!")

            elif cmd == 2:
                cul = change_user_level()
                cul.view_user_acc()
                cul.connnect_to_databse()

                name = input("Please enter an username of the account you want to modify:")
                new_lvl = input("Please enter a new user level of the account you want to modify:")

                cul.operate_datebase(name, new_lvl)
                print(f"Successfully modified, the user level of {name} has been changed to {new_lvl}!")

            elif cmd == 3:
                break





