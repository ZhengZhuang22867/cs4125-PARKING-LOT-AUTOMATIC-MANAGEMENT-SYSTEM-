from Data.System_management.System_management_controller import system_management_controller
from User.Info_improve.User_info_improve import user_info_improve
from User.AccountBalance.User_balance_topup import user_balance_topup
from User.Reservation.User_view_reservation_info import user_view_reservation_info
from Administrator.View_user_account.Administrator_view_user_account import administrator_view_user_account
from Administrator.Modify_user_acc.Administrator_modify_user_acc import administrator_modify_user_acc


import unittest
class User_function_Test(unittest.TestCase):
    def test_user_register(self):

        user_name = 'Jelly' ,
        user_password = '123456',
        car_num= '12345'

        smc = system_management_controller(user_name, user_password, False, False)
        smc.user_register(car_num)


    def test_user_login(self):
        user_name = 'Jelly',
        user_password = '123456',

        smc = system_management_controller(user_name, user_password, False, False)
        smc.user_login_judgement()
        if smc.beta == True:
            pass

    def test_user_info_improve(self):
        tele = '0830000000'

        u = user_info_improve(tele)
        u.user_info_improve()

    def test_user_view_reservation_info(self):
        v = user_view_reservation_info
        v.view_reservation_info()

    def test_user_topup(self):
        money = 50

        t = user_balance_topup(money)
        t.topup()

class Admin_functin_test(unittest.TestCase):
    def test_admin_login(self):
        adm_name = 'zheng'
        adm_password = '123456'
        smc = system_management_controller(adm_name, adm_password, False, False)
        smc.adm_login_judgement()
        if smc.gamma == True:
            pass

    def test_admin_view_user_account(self):
        v = administrator_view_user_account
        v.view_user_account()

    def test_admin_modify_user_acc_changelvl(self):
        cmd = '2'
        name = 'Jelly'
        new_lvl = '2'

        m = administrator_modify_user_acc(cmd, name, new_lvl)
        m.modify_user_acc()

    def test_admin_modify_user_acc_delete(self):

        cmd = '1'
        name = 'Jelly'

        m = administrator_modify_user_acc(cmd, name, None)
        m.modify_user_acc()









