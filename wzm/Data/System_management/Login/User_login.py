from Data.System_management.Register.User_register import user_register

class user_login:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.deter = None

    def user_login(self):
        # Obtain the user name and password
        r = user_register
        result = r.get_useracc(self)

        ulist = []
        plist = []
        for item in result:
            ulist.append(item['user_name'])
            plist.append(item['user_password'])
        self.deter = True
        for i in range(len(ulist)):
            while True:
                if self.name == ulist[i] and self.password == plist[i]:
                    print("Login successful!")
                    self.deter = False
                    break
                else:
                    break


