from mysql.connector import connect, Error
from getpass import getpass
from commands_db import *

from standart_connect_args import CONNECT_KWARGS
from connect_args import *


if __name__ == '__main__':
    try:
        #CONNECT_KWARGS = set_conntect_args()
        with connect(**CONNECT_KWARGS) as connection:
            with connection.cursor() as cursor:
                cursor.execute(SHOW_DATABASES)
                databases = []
                for i, db in enumerate(cursor, start=1):
                    databases.append(db[0])
                    print(i, db[0])
                select_db = int(input("Select the database which you want to copy:"))
                select_db = databases[select_db-1]
                print(select_db)
    except Error as e:
        print(e)
