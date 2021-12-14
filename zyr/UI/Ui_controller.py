class ui_controller:
    def __init__(self):
        pass

    # Main interface
    def main_interface(self):
        print('*************************************************************************')
        print("Please select the action you want to perform: ")
        print("")
        print("---------1.User login-----------------------")
        print("---------2.Administrator login--------------")
        print("---------3.User registration----------------")
        print("---------4.Quit-----------------------------")


    # User interface
    def user_interface(self, name):
        print('*************************************************************************')
        print("Welcome back!", name, ", what do you want to do?")
        print("")
        print("---------1.Parking space reservation--------")
        print("---------2.Cancel reservation---------------")
        print("---------3.Query reservation information----")
        print("---------4.Improve personal information-----")
        print("---------5.Account balance checking---------")
        print("---------6.Account balance top-up-----------")
        print("---------7.Pay the fare---------------------")
        print("---------8.Quit-----------------------------")


    # Parking space Reservation Interface
    def space_reservation_interface(self):
        print('*************************************************************************')
        print("What type of parking space do you want to reserve?")
        print("")
        print("---------1.Type Motor-----------------------")
        print("---------2.Type Car-------------------------")
        print("---------3.Type Truck-----------------------")
        print("---------4.Type Govern----------------------")
        print("---------5.Quit-----------------------------")


    # Cancel the parking reservation screen
    def space_reservation_cancel_interface(self):
        print("")
        print("Are you sure to cancel the appointment?")
        print("---------1.Yes------------------------")
        print("---------2.No-------------------------")


    # Administrator Operation Interface
    def adm_interface(self, name):
        print('*************************************************************************')
        print("Welcome back!", name, ", what do you want to do?")
        print("")
        print("---------1.View user account-----------------")
        print("---------2.Modify user information-----------")
        print("---------3.Modify parking status-------------")
        print("---------4.Quit------------------------------")

    # Modify the parking space status interface
    def modify_parking_status_interface(self):
        print("")
        print("Are you sure you want to change the status of the parking space to: 'Maintenance'?")
        print("---------1.Yes------------------------")
        print("---------2.No-------------------------")

    # Payment of parking fee confirmation interface
    def pay_fare_interface(self):
        print("")
        print("Are you sure to deduct this expense from your account balance?")
        print("---------1.Yes------------------------")
        print("---------2.No-------------------------")

    # The administrator modifies the user account interface
    def modify_user_acc_interface(self):
        print("")
        print("Please select the action you want to perform: ")
        print("")
        print("---------1.Delete user account--------")
        print("---------2.Change user level----------")
        print("---------3.Quit-----------------------")
        print("  More functions to be developed......")

