<<<<<<< HEAD
def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr,n)
def leftRotatebyOne(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
    
    
def printArray(arr,size):
    for i in range(size):
        print ("%d"%arr[i],end="")
        
arr = [1,2,3,4,5,6,7]
leftRotatebyOne(arr,2,7) 
printArray(arr,7)
=======
import hashlib

sha256_hash = hashlib.sha256()
sha256_hash.update(b'Hello,')
sha256_hash.update(b'RUNOOB!')
print(sha256_hash.hexdigest())
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
