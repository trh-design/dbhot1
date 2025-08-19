<<<<<<< HEAD
def countSort(arr):
    
    output = [0 for i in range(256)]
    
    count = [0 for i in range(256)]
    
    ans = ["" for _ in arr]
    
    for i in arr:
        count[ord(i)] += 1
        
    for i in range(256):
        count[i] += count[i-1]
        
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
        
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

arr = "wwwrunoobcom"
ans = countSort(arr)
print ( "字符数组排序 %s" %("".join(ans)) )
=======
import statistics

data = [1,2,3,4,5,6,7,8,9,10]
quantiles = statistics.quantiles(data, n=4, method='inclusive')
print(quantiles)
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
