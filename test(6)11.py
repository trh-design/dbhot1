# 装饰器
import time
import functools

def timer(fun):
    @functools.wraps(fun)
    def wrapper():
        start_time = time.time()
        fun()
        end_time = time.time()
        print("函数运行时间为:{}".format(end_time-start_time))
        
    return wrapper

#@timer和fun=timer(fun)等效
@timer
def fun():
    time.sleep(2)
    
print(fun.__name__)