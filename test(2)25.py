<<<<<<< HEAD
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1       # left = 2*i + 1
    r = 2 * i + 2       # right = 2*i + 2
    
    if l < n and arr[i] < arr[l]:
        largest = 1
        
    if r < n and arr[largest] < arr[r]:
        largest = r
        
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]   #交换
        
        heapify(arr, n, largest)
        
def heapSort(arr):
    n = len(arr)
    
    # Build a maxheap
    for i in range(n, -1, -1):
        heapify(arr, n, i)
        
    # 一个个交换元素
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[1]   # 交换
        heapify(arr, i, 0)
        
arr= [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("排序后")
for i in range(n):
    print ("%d" %arr[i])
=======
import statistics

data = [1,2,3,4,5]
variance = statistics.variance(data)
print(variance)
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
