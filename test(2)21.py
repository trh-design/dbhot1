<<<<<<< HEAD
def swapList(newList):
    size = len(newList)
    
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    
    return newList

newList = [1, 2, 3]

print(swapList(newList))
=======
import statistics

data = [10,20,30,40]
interval = 10
median = statistics.median_grouped(data, interval)
print(median)
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
