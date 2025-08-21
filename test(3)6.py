<<<<<<< HEAD
# Filename : test.py
# author by : www.runoob.com

# 二次方程式 ax**2 + bx + c = 0
#a,b,c 用户提供， 为实数，a ≠ 0

# 导入 cmath(复杂数学运算)模块
import cmath

a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))

# 计算
d = (b**2) - (4*a*c)

# 两种方式求解
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('结果为 {0} 和 {1}'.format(sol1,sol2))
=======
# 导入 math 包
import math

# 初始化 n 
n = 7

# 初始化 k
k = 5

# 输出从 n 个项中选择 k 项的方式总数
print (math.perm(n,k))
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
