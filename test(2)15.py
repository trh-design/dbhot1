<<<<<<< HEAD
# 定义立方和的函数
def sumOfSeries(n):
    sum = 0
    for i in range(1, n+1):
        sum +=i*i*i
        
    return sum


# 调用函数
n = 5
print(sumOfSeries(n))
=======

import hashlib

sha256_hash = hashlib.new('sha256')
sha256_hash.update(b'RUNOOB')
print(sha256_hash.hexdigest())
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
