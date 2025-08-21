<<<<<<< HEAD
# -*- coding: UTF-8 -*-

# Filename : test.py  
# auther by : www.runoob.com

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    
    
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass
    
    return False

# 测试字符串和数字
print(is_number('foo'))      # False
print(is_number('1'))        # True
print(is_number('1.3'))      # True
print(is_number('-1.37'))    # True
print(is_number('1e3'))      # True
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
