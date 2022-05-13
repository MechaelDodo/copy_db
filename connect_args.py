from getpass import getpass

def set_conntect_args():
    HOST = input('Host (default "localhost"): ')
    USER = input('Username: ')
    PASSWORD = input('Password: ')      # it is not safe
    CONNECT_KWARGS = {'host': HOST, 'user': USER, 'password': PASSWORD}
    return CONNECT_KWARGS