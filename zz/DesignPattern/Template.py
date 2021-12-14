# 作用于管理员修改用户账户信息，一个是删除用户账户，另一个是改变用户等级

from Administrator.View_user_account.Administrator_view_user_account import administrator_view_user_account
from Data.Daolmpl.Modify_user_acc_Daolmpl import modify_user_acc_daolmpl
from Data.Database import database


class template:
    def __init__(self):
        pass

    # This method is called directly by two subclasses without overwriting it 这个方法两个子类直接调用不用重写
    def view_user_acc(self):
        avua = administrator_view_user_account()
        avua.view_user_account()

    # This method is called directly by two subclasses without overwriting it 这个方法两个子类直接调用不用重写
    def connnect_to_databse(self):
        d = database()
        muad = modify_user_acc_daolmpl(None, None, None, None, None, None, None, None, None)
        muad.connect_to_databse()

        cursor = muad.conn.cursor()
        cursor.execute(muad.query)
        muad.conn.commit()

    # This method needs to be overridden by two subclasses themselves 这个方法需要两个子类自己重写
    def operate_datebase(self):
        raise NotImplementedError
