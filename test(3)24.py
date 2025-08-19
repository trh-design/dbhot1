<<<<<<< HEAD
# Filename : test.py   
# author by : www.runoob.com

# 定义一个函数
def hcf(x, y):
    """该函数返回两个数的最大公约数"""
    
    # 获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x
        
    for i in range(1,smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf


# 用户输入两个数字
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

print( num1,"和", num2, "的最大公约数为", hcf(num1, num2))
=======
import statistics

data = [1,2,3,4,5]
variance = statistics.pvariance(data)
print(variance)
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
