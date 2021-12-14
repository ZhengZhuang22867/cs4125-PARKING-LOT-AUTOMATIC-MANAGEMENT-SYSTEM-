from DesignPattern.Observer import observer
from Data.Daolmpl.Level_update_Daolmpl import level_update_daolmpl
from Data.Database import database


class user_level_update(observer):
    def __init__(self, name):
        self.name = name

    def update(self):
        d = database()
        lud = level_update_daolmpl(self.name, None, None, None, None, None, None)
        lud.get_total_parking_time()

        cursor = lud.conn.cursor()
        cursor.execute(lud.query)
        lud.conn.commit()

        # Store the found data into R and return it as an array
        result = cursor.fetchall()
        for i in result:
            tt = i[0]
            # 返回的用户总停车时间 tt 是string类型

        # The default level is 0. After 50 hours, the level is 1. After 200 hours, the level is 2
        new_lvl = 0
        if 50 <= tt < 200:
            new_lvl = 1
        elif tt >= 200:
            new_lvl = 2

        lud2 = level_update_daolmpl(self.name, None, None, None, None, None, new_lvl)
        lud2.change_user_level()

        cursor = lud2.conn.cursor()
        cursor.execute(lud2.query2)
        cursor.execute(lud2.query3)
        cursor.execute(lud2.query4)
        lud2.conn.commit()
        d.close_conn()

    def show_new_user_level(self):
        d = database()

        lud3 = level_update_daolmpl(self.name, None, None, None, None, None, None)
        lud3.show_new_user_level()

        cursor = lud3.conn.cursor()
        cursor.execute(lud3.query5)
        lud3.conn.commit()

        # Store the found data into R and return it as an array
        result1 = cursor.fetchall()
        for i in result1:
            lvl = i[0]
            # The returned user level LVL is of type string

        print("Your new user level is:", lvl)

        d.close_conn()



