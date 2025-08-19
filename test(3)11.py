<<<<<<< HEAD
# -*- coding : UTF-8 -*-

# Filename : test.py 
# author by : www.runoob.com

# 用户输入

x = input('输入x值: ')
y = input('输入y值: ')

# 创建临时变量，并交换
temp = x
x = y
y = temp 

print('交换后x的值为: {}'.format(x))
print('交换后y的值为: {}'.format(y))
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
