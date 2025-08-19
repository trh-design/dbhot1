# 类装饰器
import time

class timer():
    
    def __init__(self, func):
        self.func = func
        
    def __call__(self):
        star_time = time.time()
        self.func()
        end_time = time.time()
        total = end_time - star_time
        print("函数运行时间: ", total)
        
@timer
def fun():
    time.sleep(2)
    
fun()