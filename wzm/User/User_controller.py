from User.AccountBalance.User_pay_fee import user_pay_fee
from User.Level_update.User_level_update import user_level_update
from User.Reservation.User_space_reservation import user_space_reservation
from User.Reservation.User_space_reservation_cancel import user_space_reservation_cancel
from User.Reservation.User_view_reservation_info import user_view_reservation_info
from User.Info_improve.User_info_improve import user_info_improve
from User.AccountBalance.User_balance_checking import user_balance_checking
from User.AccountBalance.User_balance_topup import user_balance_topup
from UI.Ui_controller import ui_controller

class user_controller:
    def __init__(self, name):
        self.name = name

    def user_controller(self):

        while True:
            u = ui_controller()
            u.user_interface(self.name)
            cmd = int(input("Please enter the instruction number："))


            if cmd == 1:
                sr = user_space_reservation(self.name)
                sr.space_reservation()
            elif cmd == 2:
                usrc = user_space_reservation_cancel(self.name)
                usrc.space_reservation_cancel()
            elif cmd == 3:
                uvri = user_view_reservation_info(self.name)
                uvri.view_reservation_info()
            elif cmd == 4:
                i = user_info_improve(self.name)
                i.user_info_improve()
            elif cmd == 5:#Account balance checking
                bc = user_balance_checking(self.name)
                bc.balance_checking()
            elif cmd == 6: #Account balance top-up
                bt = user_balance_topup(self.name)
                bt.topup()
            elif cmd == 7:#Pay the fare
                py = user_pay_fee(self.name)
                py.pay()
                ulu = user_level_update(self.name)
                ulu.update()
                ulu.show_new_user_level()
            elif cmd == 8:
                break


