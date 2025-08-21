def wapper(func):
    def inner(*args, **kwargs):
        count=0
        while count<5:
            func(*args, **kwargs)
            count+=1
    return inner
@wapper
def func():
    print("执行")
func