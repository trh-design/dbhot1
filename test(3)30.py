<<<<<<< HEAD
# Filename : test.py 
# author by : www.runoob.com

# 写文件
with open("test.txt", "wt") as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧! ")
    
# Read a file
with open("test.txt", "rt") as in_file:
    text = in_file.read()
    
print(text)
=======
# 导入 reqursts 包
import requests

# 发送请求
x = requests.get('https://www.runoob.com/try/ajax/json_deom.json')

# 返回 json 数据
print(x.json())
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
