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
import struct
import socket


key = 'kEyXXXXXXXXXXXXXXXX'     #替换成微信绑定key
path = './test.jpg'             #自己需要发送的图片路径

def encodeImg(Key,filePath,ID=0):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('39.106.101.197', 6999))
    img = cv2.imread(filePath)
    img = cv2.resize(img,(640,480))  # 此处仅支持640*480分辨率
    _, img_encode = cv2.imencode('.jpg',img)
    img_code = numpy.array(img_encode)
    img_data = img_code.tostring()
    sendMsgs = struct.pack("l", len(img_data))+str.encode(Key)+str.encode(str(ID))+img_data
    client.send(sendMsgs)
    rec = client.recv(1024).decode('utf-8')
    client.close()
    return rec

if __name__ == '__main__':
    print(encodeImg(key,path,0))




