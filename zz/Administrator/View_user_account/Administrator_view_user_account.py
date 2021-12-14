import pandas as pd

from Data.Daolmpl.View_user_account_Daolmpl import view_user_account_daolmpl
from Data.Database import database
class administrator_view_user_account():
    def __init__(self):
        pass

    def view_user_account(self):

        # connect to database
        d = database()
        vuad = view_user_account_daolmpl(None, None)
        vuad.connect_to_database()

        #利用pandas直接获取数据
        #
        data = pd.read_sql(vuad.sql, vuad.conn)
        print(data)
        d.close_conn()



