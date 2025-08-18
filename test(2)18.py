<<<<<<< HEAD
def leftRotate(arr, d, n):
    for i in range(gcd(d,n)):
        
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
        
def printArray(arr, size):
    for i in range(size):
        print ("%d" % arr[i], end="")
        
def gcd(a, b):
    if b == 0:
        return a;
    else:
        return gcd(b, a%b)
    
arr = [1,2,3,4,5,6,7]
leftRotate(arr, 2, 7)
printArray(arr, 7)
=======
import yfinance as yf 

# 获取股票数据
symbol = "600519.SS"
start_data = "2022-01-01"
end_data = "2023-01-01"

data =yf.download(symbol, start=start_data, end=end_data)
print(data.head())
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
