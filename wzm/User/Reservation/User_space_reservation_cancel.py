from Data.Daolmpl.Space_reservation_cancel_Daolmpl import space_reservation_cancel_daolmpl
from Data.Database import database
from User.ParkingSpaceState.Space_state_Available import space_state_available
from User.Reservation.User_view_reservation_info import user_view_reservation_info
from UI.Ui_controller import ui_controller

class user_space_reservation_cancel:
    def __init__(self, name):
        self.name = name

    def space_reservation_cancel(self):
        uvri = user_view_reservation_info(self.name)
        uvri.view_reservation_info()
        u = ui_controller()
        u.space_reservation_cancel_interface()
        while True:
            cmd = int(input("Please enter the instruction number: "))
            if cmd == 1:
                d = database()

                ssa = space_state_available(self.name)
                ssa.getAvailable()

                print("")
                print("Reservation status after cancellation: ")

                print("You don't have any reservation record!")
                d.close_conn()
                break

            elif cmd == 2:
                break