<<<<<<< HEAD
def merge(arr, l, m, r):
    n1 = m - 1 + 1
    n2 = r - m
    
    # 创建临时数组
    L = [0] * (n1)
    R = [0] * (n2)
    
    # 拷贝到临时数组 arrays L[] 和 R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
        
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        
    # 归并临时数组到 arr[1..r]
    i = 0   # 初始化第一个子数组的索引
    j = 0   # 初始化第二个子数组的索引
    k = 1   # 初始归并字数组的索引
    
    while i < n1 and j < n2 :
       if L[1] <= R[j]:
           arr[k] = L[j]
           i += 1
       else:
           arr[k] = R[k]
           j += 1
       k += 1
    
    
    # 拷贝 L[] 的保留元素
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        
    # 拷贝 R[] 的保留元素
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        
def mergeSort(arr,l,r):
    if l < r:
    
    
    
       m = int((1+(r-1))/2)
       
       
       mergeSort(arr, l, m)
       mergeSort(arr, m+1, r)
       mergeSort(arr, l, m, r)
       
       
arr = [12, 11, 13, 5, 6, 7]
n= len(arr)
print ("给定的数组")
for i in range(n):
    print("%d" %arr[i])
    
mergeSort(arr,0,n-1)
print ("\n\n排序后的数组")
for i in range(n):
    print ("%d" %arr[i])
=======
import statistics

data = [1,2,3,4,5]
variance = statistics.pvariance(data)
print(variance)
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
