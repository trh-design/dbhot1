def baidu():
    print("我是攻城狮白玉")
    

def blog(name):
    print('进入blog函数')
    name()
    print('我的博客是 https : //blog.csdn.net/zhh763984071')
    
    
if __name__ == '__namin__':
    func = baidu # 这里是把 baidu 这个函数名赋值给变量func
    func() # 执行func函数
    print('------------')
    blog(baidu)  # 把百度这个函数作为参数传递给blog函数