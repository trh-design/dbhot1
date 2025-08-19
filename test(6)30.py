#!/usr/bin/python3

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
else:
    print("没有循环数据！")
print("完成循环！")



a = 1000
if a % 400 == 0:
    print("是")
elif a % 100 == 0:
    print("不是")
elif a % 4 == 0:
    print("是")
else:
    print("不是")


for i in range(100):
    if i % 2 != 0:
        print(i)