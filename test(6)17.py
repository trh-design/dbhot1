def wapper(func):
    def inner(*args,**kwargs):
        ret=func(*args,**kwargs)
        ret=print(ret+100)
        return ret                    
    return inner
@wapper
def func(number):
    return int(number)
func(100)
###结果：200