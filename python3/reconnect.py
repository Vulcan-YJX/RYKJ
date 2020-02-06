#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import time
import socket

key = 'kEyXXXXXXXXXXXXXXXX'     #替换成微信绑定key

def doConnect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :
        sock.connect(("www.rykj.xyz",443))
    except :
        pass
    return sock

def main():
    client = doConnect()
    usrkey = "<key>"+key+"</key>"
    client.send(usrkey.encode('utf-8'))
    while True :
        try:
            #通过获取系统时间来模拟用户的输入
            msg = "<text>"+str(time.time())+"</text>"+usrkey
            client.send(msg.encode('utf-8'))
            print("send msg ok : ",msg)
            print("recv data :",client.recv(1024).decode('utf-8'))
        except socket.error:
            print("\r\nsocket error,do reconnect ")
            time.sleep(3)
            sockLocal = doConnect()
        time.sleep(3)


if __name__ == "__main__" :
    main()
