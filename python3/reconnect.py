#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import time
import socket

def doConnect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :
        sock.connect(("39.106.101.197",443))
    except :
        pass
    return sock

def main():
    sockLocal = doConnect()
    usrkey = "<key>用户的KEY</key>"
    sockLocal.send(usrkey.encode('utf-8'))
    while True :
        try:
            msg = "<text>"+str(time.time())+"</text>"+usrkey
            sockLocal.send(msg.encode('utf-8'))
            print("send msg ok : ",msg)
            print("recv data :",sockLocal.recv(1024).decode('utf-8'))
        except socket.error:
            print("\r\nsocket error,do reconnect ")
            time.sleep(3)
            sockLocal = doConnect()
        time.sleep(3)


if __name__ == "__main__" :
    main()
