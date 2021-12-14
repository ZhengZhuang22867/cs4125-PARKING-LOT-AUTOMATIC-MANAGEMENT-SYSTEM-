from DesignPattern.Factory import Factory


class system_management_controller:
    def __init__(self, name, password, beta, gamma):
        self.name = name
        self.password = password
        self.beta = None
        self.gamma = None

    def user_login_judgement(self):
        f = Factory()
        l = f.getUser_login(self.name, self.password)
        l.user_login()
        if l.deter == True:
            print("Username or password does not exist! Please enter again!")
            self.beta = True#同理设置一个deter进行判断


    def adm_login_judgement(self):
        f = Factory()
        ll = f.getAdministrator_login(self.name, self.password)
        ll.adm_login()
        if ll.deter == True:
            print("Username or password does not exist! Please enter again!")
            self.gamma = True

    def user_register(self, car_num):
        f = Factory()
        r = f.getRegister(self.name, self.password, car_num)
        r.get_useracc()
        r.insert_useracc()