<<<<<<< HEAD
def shellSort(arr):
    
    n = len(arr)
    gap = int(n/2)
    
    while gap > 0:
        
        for i in range(gap,n):
            
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
            
arr = [ 12, 34, 54, 2, 3]

n = len(arr)
print ("排序前:")
for i in range(n):
    print(arr[i])
    
shellSort(arr)

print ("n\排序后:")
for i in range(n):
    print(arr[i])
=======
# -*- coding : UTF-8 -*-

# Filename : test.py  
# author by : www.runoob.com 

year = int(input("输入一个年份: "))
if (year % 4) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
           print("{0} 是闰年".format(year))    #整百年能被400整除的是闰年
        else:
           print("{0} 不是闰年".format(year))
    else:
        print("{0} 是闰年".format(year))       #非整百年能被4整除的是闰年
else:
    print("{0} 不是闰年".format(year))
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
