#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import threading


host = raw_input('input the server ip address:')
port = 8888

s = socket.socket()
print 'Socket created'
s.bind((host, port))
s.listen(5)

print 'Socket new listening'


while True:
    conn, addr = s.accept()
    print 'Connected with' + addr[0] + ':' + str(addr[1])
    nick = s.recv(1024)