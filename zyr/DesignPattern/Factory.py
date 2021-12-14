from Data.System_management.Register.User_register import user_register
from Data.System_management.Login.User_login import user_login
from User.User_controller import user_controller
from Administrator.Administrator_controller import administrator_controller
from Data.System_management.Login.Administrator_login import administrator_login

#改完报错：说"循环导入"，所以导入action的文件都不在写入factory中
#from Administrator.Modify_parking_status import modify_parking_status
#from User.Reservation import Reservation

class Factory:
    def __init__(self):
        pass

    def getRegister(self, name, password, carnum):
        return user_register(name, password, carnum)

    def getUser_login(self, user_name, user_password):
        return user_login(user_name, user_password)

    def getUser_controller(self, user_name):
        return user_controller(user_name)

    def getAdministrator_action(self, adm_name):
        return administrator_controller(adm_name)

    def getAdministrator_login(self, adm_name, adm_password):
        return administrator_login(adm_name, adm_password)

