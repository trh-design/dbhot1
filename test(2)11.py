<<<<<<< HEAD
# Filename : test.py  
# author by : www.runoob.com

# 导入 datetime 模块
import datetime
def getYesterday():
    today=datetime.date.today() 
    oneday= datetime.timedelta(days=1)
    yesterday= today-oneday
    return yesterday

# 输出
print(getYesterday())
=======
# 导入 requests 包
import requests

# 发送请求
x = requests.get('https://www.runoob.com/')

# 返回 http 的状态码
print(x.status_code)

# 响应状态的描述
print(x.reason)

# 返回编码
print(x.apparent_encoding)
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
