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