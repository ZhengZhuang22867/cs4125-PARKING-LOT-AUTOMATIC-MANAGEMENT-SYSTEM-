from Data.Daolmpl.Info_improve_Daolmpl import info_improve_daolmpl
from Data.Database import database


class user_info_improve:
    def __init__(self, name):
        self.name = name

    def user_info_improve(self):
        #
        d = database()
        iid = info_improve_daolmpl(self.name, None, None, None, None)
        iid.connect_to_database()
        #
        cursor = iid.conn.cursor()
        cursor.execute(iid.sql)
        iid.conn.commit()

        tele = input("Please enter your telephone number: ")

        result = cursor.fetchall()
        result = [dict(zip([k[0] for k in cursor.description], row)) for row in result]
        ulist = []
        for item in result:
            ulist.append(item['user_name'])

        iid2 = info_improve_daolmpl(self.name, tele, None, None, None)
        iid2.database_operation()

        cursor = iid2.conn.cursor()
        cursor.execute(iid2.sql2)
        iid2.conn.commit()
        print("Information modified successfully!")

        d.close_conn()