#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import threading


outString = ''
nick = ''
inString = ''


def client_send(sock):
    global outString
    while True:
        outString = raw_input()
        outString = nick + ':' + outString
        sock.send(outString)


def client_accept(sock):
    global inString
    while True:
        try:
            inString = sock.recv(1024)
            if not inString:
                break
            if outString != inString:
                print inString
        except:
            break


nick = raw_input('input your nickname:')
ip = raw_input('input the server ip address:')
port = 8888
sock = socket.socket() #创建套接字
sock.connect((ip, port)) #连接

sock.send(nick) #发送用户名到服务器

th_send = threading.Thread(target=client_send, args=(sock,))
th_send.start()
th_accept = threading.Thread(target=client_accept, args=(sock,))
th_accept.start()