#coding:utf-8
import socket
import time

SSID = 'your wifi SSID'
PASSWD = 'your wifi passwd'
usrkey = "<key>kEy*************</key>"

def connectWifi():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(SSID,PASSWD)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def doConnect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connectMsg = socket.getaddrinfo('www.rykj.xyz', 443)[0][4]
        client.connect(connectMsg)
    except:
        pass
    return client

client = doConnect()
client.send(usrkey.encode('utf-8'))
print('[+] connect succesfull')
while True:
    try:
        userMsgs = input()
        msg = "<text>"+userMsgs +"</text>"+usrkey
        if len(msg) == 0:
            continue
        client.send(msg.encode('utf-8'))
        data = client.recv(1024).decode('utf-8')
        print('from server:',data)
    except socket.error:
        print('socket.error doConnect')
        time.sleep(2)
        client = doConnect()
print('[+]  connect close...')
client.close()
