# 导入 reqursts 包
import requests

# 发送请求
x = requests.get('https://www.runoob.com/try/ajax/json_deom.json')

# 返回 json 数据
print(x.json())