<<<<<<< HEAD
#!/usr/bin/python3

# Filename : test.py 
# author by ： www.runoob.com

# 通过用户输入数字计算阶乘

# 获取用户输入的数字
num = int(input("请输入一个数字： "))
factorial = 1

# 查看数字是负数， 0 或负数
if num < 0:
    print("抱歉,负数没有阶乘")
elif num == 0:
    print("0 的阶乘为 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*1
        print("%d 的阶乘为 %d"%(num,factorial))
=======
# 导入 random 模块
import random

random.seed()
print ("使用默认种子生成随机数:",random.random())
print ("使用默认种子生成随机数:",random.random())

random.seed(10)
print ("使用整数 10 种子生成随机数:",random.random())
random.seed(10)
print ("使用整数 10 种子生成随机数:",random.random())

random.seed("hello",2)
print ("使用字符串种子生成随机数:",random.random())
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
