from Data.Daolmpl.Modify_user_acc_Daolmpl import modify_user_acc_daolmpl
from DesignPattern.Template import template


class delete_user_acc(template):
    def __init__(self):
        pass

    def operate_datebase(self, name):
        muad = modify_user_acc_daolmpl(None, None, None, None, None, None, None, None, None)
        muad.delete_user_acc(name)
        cursor = muad.conn.cursor()
        cursor.execute(muad.query2)
        cursor.execute(muad.query3)
        cursor.execute(muad.query4)
        cursor.execute(muad.query5)
        muad.conn.commit()
