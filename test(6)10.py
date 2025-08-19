# 装饰器
import time 

def timer(fun):
    print("我是老六")
    
    def wrapper():
        strat_time = time.time()
        fun()
        end_time = time.time()
        print("函数运行时间为:{}".format(end_time-strat_time))
        
    return wrapper

#@timer和@fun=time(fun)等效
@timer                              
def fun():
    time.sleep(2)
    
if __name__ == '__main__':
    fun()