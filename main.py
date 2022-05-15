from mysql.connector import connect, Error
from getpass import getpass
from commands_db import *
import os
#from standart_connect_args import CONNECT_KWARGS
from connect_args import *


def dump(database, connect_kwargs):
    os.popen(f"mysqldump -u {connect_kwargs['user']} -p {database} > {database}/{database}_dump.sql")


if __name__ == '__main__':
    try:
        CONNECT_KWARGS = set_conntect_args()
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
                try:
                    os.mkdir(select_db)
                    dump(select_db, CONNECT_KWARGS)
                except FileExistsError:
                    os.rmdir(select_db)
                    os.mkdir(select_db)
                    dump(select_db, CONNECT_KWARGS)
    except Error as e:
        print(e, 'haaha')
