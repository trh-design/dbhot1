<<<<<<< HEAD
def main():
    fish = 1
    while True:
        totle,enough = fish, True
        for _ in range(5):
            if (totle - 1) % 5 == 0:
                totle = (totle - 1) // 5 * 4
            else:
                enouge = False
                break
        if enough:
            print(f'总共有{fish}条鱼')
            break
        fish +=1
        
        
if __name__ == '__main__':
    main()
=======
# 导入 random 模块
import random

random.seed()
print ("使用默认种子生成随机数:",random.random())
print ("使用默认种子生成随机数:",random.random())

random.seed(10)
print ("使用整数 10 种子生成随机数:",random.random())
random.seed(10)
print ("使用整数 10 种子生成随机数:",random.random())

random.seed("hello",2)
print ("使用字符串种子生成随机数:",random.random())
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
