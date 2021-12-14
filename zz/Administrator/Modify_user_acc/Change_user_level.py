from Data.Daolmpl.Modify_user_acc_Daolmpl import modify_user_acc_daolmpl
from DesignPattern.Template import template

class change_user_level(template):
    def __init__(self):
        pass

    def operate_datebase(self, name, new_lvl):
        muad = modify_user_acc_daolmpl(None, None, None, None, None, None, None, None, None)
        muad.change_user_lvl(name, new_lvl)
        cursor = muad.conn.cursor()
        cursor.execute(muad.query6)
        cursor.execute(muad.query7)
        cursor.execute(muad.query8)
        muad.conn.commit()