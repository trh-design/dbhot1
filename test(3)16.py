<<<<<<< HEAD
# Filnema : test.py 
# author by : ww.runoob.com


# Python 检测用户输入的数字是否为阿姆斯特朗数
num = int(input("请输入一个数字: "))

# 初始化变量 sum
sum = 0
# 指数
n = len(str(num))

# 检测
temp = num 
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10
    
# 输出结果
if num == sum:
    print(num,"是阿姆斯特朗数")
else:
    print(num,"不是阿姆斯特朗数")
=======
import hashlib

md5_hash = hashlib.md5(b'RUNOOB')
print(md5_hash.hexdigest())
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
