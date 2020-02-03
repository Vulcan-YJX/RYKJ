#!/usr/bin/env python3
#-*-coding:utf-8-*-
"""
如易科技 公众平台
author:vulcanyjx
功能描述：将制定路径的图片发送至服务器
参数：
Key（str）：用户绑定微信的唯一key
filePath(str)：发送图片的路径
ID(int)：不同的服务请求
        0——发送到微信默认返回ok
"""
import cv2
import numpy
import socket


key = 'kEyd52fb0d9eaf4d97a'     #替换成微信绑定key
path = './a.jpg'             #自己需要发送的图片路径


def staticLen(imageData):
    strLen = len(str(len(imageData)))
    if  strLen > 9:
        input("图片尺寸过大无法发送")
        return
    else:
        zeroBuf = ''
        for i in range(9-strLen):
            zeroBuf += '0'
        lenData = 'pic'+ zeroBuf + str(len(imageData)) + 'mark'
        return lenData.encode('utf-8')

def encodeImg(Key,filePath,ID=0):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('39.106.101.197', 6999))
    img = cv2.imread(filePath)
    img = cv2.resize(img,(640,480))  # 此处仅支持640*480分辨率
    _, img_encode= cv2.imencode('.jpg',img)
    img_code = numpy.array(img_encode)
    img_data = img_code.tostring()
    headMsgs = staticLen(img_data)
    sendMsgs = headMsgs+str.encode(Key)+str.encode(str(ID))+img_data
    client.send(sendMsgs)
    rec = client.recv(1024).decode('utf-8')
    client.close()
    return rec

if __name__ == '__main__':
    print(encodeImg(key,path,0))




