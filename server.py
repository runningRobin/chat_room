#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import threading


con = threading.Condition()

host = raw_input('input the server ip address:')
port = 8888
data = ''

s = socket.socket()
print 'Socket created'
s.bind((host, port))
s.listen(5)

print 'Socket new listening'


def NotifyAll(sss):
    global data
    if con.acquire(): #获取锁
        data = sss
        con.notifyAll() #表示当前线程放弃对资源的占用 通知其他线程从wait方法执行
        con.release() #释放锁


def threadOut(conn, nick):
    global data
    while True:
        if con.acquire():
            con.wait()
            if data:
                try:
                    conn.send(data)
                    con.release()
                except:
                    con.release()
                    return


def threadIn(conn, nick):
    while True:
        try:
            temp = conn.recv(1024)
            if not temp:
                conn.close()
                return
            NotifyAll(temp)
            print data
        except:
            NotifyAll(nick + 'error')
            print data
            return


while True:
    conn, addr = s.accept()
    print 'Connected with' + addr[0] + ':' + str(addr[1])
    nick = conn.recv(1024)
    NotifyAll('Welcome ' + nick + ' to the room!!!')
    print data
    conn.send(data)
    threading.Thread(target=threadOut, args=(conn, nick)).start()
    threading.Thread(target=threadIn, args=(conn, nick)).start()