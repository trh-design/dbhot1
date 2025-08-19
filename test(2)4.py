<<<<<<< HEAD
#!/usr/bin/python3

# 输出指定范围内的素数

# take input from the user
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))

for num in range(lower,upper+1):
    # 素数大于 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
=======
# 导入 math 包
import math 

# 输出一个数字以 10 为底的自然对数
print(math.log10(2.7183))
print(math.log10(2))
print(math.log10(1))
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
