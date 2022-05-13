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
                for db in cursor:
                    print(db[0])
    except Error as e:
        print(e)
