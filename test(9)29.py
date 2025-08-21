import requests

x = requests.get('https://www.runoob.com/')

print(x.status_code)

print(x.reason)

print(x.apparent_encoding)

import random
dir(random)

import random

random.seed()
print("使用默认种子生成随机数: ", random.random())
print("使用默认种子生成随机数: ", random.random())

random.seed(10)
print("使用整数 10 种子生成随机数：", random.random())
random.seed(10)
print("使用整数 10 种子生成随机数：", random.random())

random.seed("hello", 2)
print("使用字符串种子生成随机数：", random.random())

import requests

x = requests.get("https://www.runoob.com/try/ajax/json_demo.json")

print(x.json())