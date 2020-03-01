关注 如易科技公众平台
===
 ## 环境配置

 ### python安装教程
> 建议使用python3安装好后升级pip工具。
> #### [python安装教程](https://www.runoob.com/python3/python3-install.html)

### 安装esptool.py
> esptool是乐鑫提供的用于刷写固件的python工具包。

```pip install adafruit-ampy esptool```

## 快速入门
 
 #### Windows 
```setup.bash 端口号```
 
#### Linux
```./setup.sh 端口号```
#### 刷写过程中请将IO0引脚拉低，当出现connect....____.....时请迅速重启芯片即可完成烧写

## 修改配置文件
* ##### 将config.txt放入SD卡。
* ##### 修改SSID、PASSWD为自己连接热点名和密码。
* ##### 修改Key标签为公众号获得的key。
* ##### 修改ＩＤ标签为对应的服务。
```０：发送图片到微信；１：人脸定位，最多定位五个人脸;```
* ##### 通过串口以115200的波特率发送数据picserver触发服务。
