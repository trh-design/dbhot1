<<<<<<< HEAD
# 导入 requests 包
import requests


kw = {'s':'python 教程'}
 
# 设置请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Geoko ) Chrome/54.0.2840.99 Safari/537.36"}

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("https://www.runoob.com/", params = kw,headers = headers)

# 查看响应状态码
print (response.status_code)

# 查看响应头部字符编码
print (response.url)

# 查看响应内容， respunse.test 返回的是Unicode格式的数据
print(response.text)
=======
# 导入 math 包
import math

# 检查数字是否为 NaN
print (math.isnan (56))
print (math.isnan (-45.34))
print (math.isnan (+45.34))
print (math.isnan (math.inf))
print (math.isnan (float("nan")))
print (math.isnan (float("inf")))
print (math.isnan (float("-inf")))
print (math.isnan (math.nan))
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
