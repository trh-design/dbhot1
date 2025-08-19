<<<<<<< HEAD
# 定义函数， arr 为数组，n 为数组长度可作为备用参数，这里没有用到
def _sum(arr, n):
    
    # 使用内置的 sum 函数计算
    return(sum(arr))

# 调用函数
arr=[]
# 数组元素
arr = [12,3,4,15]

# 计算数组元素的长度
n = len(arr)

ans = _sum(arr,n)

# 输出结果
print ('数组元素之和为', ans)
=======
#!/usr/bin/python3
import random

list = [20,16,10,5];
random.shuffle(list)
print ("随机排序列表 : ", list)

random.shuffle(list)
print ("随机排序列表 : ", list)
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
