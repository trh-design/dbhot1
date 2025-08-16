<<<<<<< HEAD
# -*- coding: UTF-8 -*-

# Filename : test.py 
# author by : www.runoob.com 

# 计算实数和复数平方根
# 导入复数数学模块

import cmath

num = int(input('请输入一个数字: '))
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))
=======
# 导入 math 包
import math

# 输出 1+x 以 e 为底的自然对数
print(math.log1p(2.7183))
print(math.log1p(2))
print(math.log1p(1))
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
