import pandas as pd
from Data.Daolmpl.Space_reservation_Daolmpl import space_reservation_daolmpl
from Data.Database import database
from UI.Ui_controller import ui_controller
from User.ParkingSpaceState.Space_state_Occupied import space_state_occupied


class user_space_reservation:
    def __init__(self, name):
        self.name = name

    def space_reservation(self):
        u = ui_controller()
        u.space_reservation_interface()
        cmd = int(input("Please enter the instruction number："))

        while True:

            if cmd == 1:# Motor
                #
                d = database()

                sso = space_state_occupied(self.name)
                sso.getOccupied()
                print("Appointment successful!")
                d.close_conn()
                break

            elif cmd == 2:# Car
                d = database()

                sso1 = space_state_occupied(self.name)
                sso1.getOccupied1()

                print("Appointment successful!")
                d.close_conn()
                break

            # Truck
            elif cmd == 3:
                d = database()

                sso2 = space_state_occupied(self.name)
                sso2.getOccupied2()

                print("Appointment successful!")
                d.close_conn()
                break

            # Govern
            elif cmd == 4:
                d = database()

                sso3 = space_state_occupied(self.name)
                sso3.getOccupied3()

                print("Appointment successful!")
                d.close_conn()
                break

            elif cmd == 5:
                break





