<<<<<<< HEAD
# Filename : test.py  
# author by : www.runoob.com

def recur_fibo(n):
    """递归函数
    输入斐波那契数列"""
    if n <=1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
    
    
# 获取用户输入
nterms = int(input("您要输出几项？"))

# 检查输入的数字是否正确
if nterms <= 0:
    print("输入正数")
else:
    print("斐波那契数列:")
    for i in range(nterms):
        print(recur_fibo(i))
=======
# -*- coding : UTF-8 -*-

# Filename : test.py 
# author : www.runoob.com

# Python 程序用于检测用户输入的数字是否为质数


# 用户输入数字
num = int(input("请输入一个数字: "))

# 质数大于 1
if num > 1:
    # 查看因子
    for i in range(2,num):
        if (num % i) == 0:
            print("num,不是质数")
            print(i,"乘于",num//i,"是",num)
            break
    else:
        print(num,"是质数")
        
# 如果输入的数字小于或等于 1 ，不是质数
else:
    print(num,"不是质数")
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
