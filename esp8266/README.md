关注 如易科技公众平台
===
 ## 环境配置

> ### python安装教程
>> 建议使用python3安装好后升级pip工具
>>> #### [python安装教程](https://www.runoob.com/python3/python3-install.html)

> ### 安装ampy
>> ampy用于向刷写了microPython固件的工具包
>>> #### [ampy安装教程](https://github.com/scientifichackers/ampy)

 ## 快速入门
 
> #### 获取代码
```git clone https://github.com/Vulcan-YJX/RYKJ.git```
> * #### 修改./RYKJ/esp8266/main.py
>> * ##### 修改SSID、PASSWD为自己连接热点名和密码。
>> * ##### 修改Key标签为公众号获得的key。
>> * ##### [刷写固件教程](https://mp.weixin.qq.com/s/ugy4Tf-XNJb_Zs9e56DNgA)
>> * ##### 修改Key标签为公众号获得的key。
>> * ##### 上传修改后的文件到eps8266
>>> ```ampy --port 设备端口号 put main.py           ```
>>> ```ampy --port 设备端口号 put boot.py```
>> * #### 下载控制端查看运行结果
>>> ```https://share.weiyun.com/5NNDGFs```
