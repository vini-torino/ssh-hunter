#!/usr/bin/python3
from socket import socket, AF_INET, SOCK_STREAM  
from sys import argv
from threading import Thread

try:
    host = argv[1] 
except IndexError:
    print( 'Usage: ssh-hunter <host>')

lucky = False 

def port_scanner(port):
    global host
    with socket(AF_INET, SOCK_STREAM)  as s:
        try:
            s.connect((host, port))
            openssh_server = s.recv(32).decode().lower().rstrip()
            if_lucky_exit(openssh_server, port)
        except:
          pass

def if_lucky_exit(openssh_server, port):
    global lucky
    if openssh_server and 'ssh' in openssh_server:
        print(f'ssh open: {port}\nversion: \'{openssh_server}\'')
        lucky = True


threads = []
port = 1
while not lucky and port <= 65535:
    t = Thread(target=port_scanner, args=(port, ))
    t.start()
    threads.append(t)
    port += 1

for thread in threads:
    thread.join()

