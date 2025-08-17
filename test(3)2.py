
# -*- coding: UTF-8 -*-

# Filename : test.py 
# author by : www.runoob.com

# 用户输入数字
num1 = input('输入第一个数字: ')
num2 = input('输入第二个数字: ')

# 求和
sum = float(num1) + float (num2)

# 显示计算结果
print('数字 {0} 和 {1} 相加结果为: {2}'.format(num1,num2,sum))

# 导入 math 包
import math 

# 计算不同数的自然对数伽玛值
print (math.lgamma(7))
print (math.lgamma(-4.2))
