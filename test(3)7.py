<<<<<<< HEAD
# -*- coding: UTF-8 -*-

# Filename : test.py 
# author by : www.runoob.com

a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长:'))

# 计算半周长
s = (a+b+c)/2

# 计算面积
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('三角形面积为 %0.2f' %area)
=======
# 导入 math 包
import math

# 输出 9 的 3 次方
print (math.pow(9,3))
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
