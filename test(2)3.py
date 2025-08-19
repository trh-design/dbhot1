<<<<<<< HEAD
# 导入 requests 包
import requests

# 表单参数， 参数名为 fname 和 lname
myobj = {'fname': 'RUNOOB','lname': 'Boy'}

# 发送请求
x = requests.post('https://www.runoob.com/try/ajax.demo_post2.php', data = myobj)

# 返回网页内容
print(x.text)
=======
# 导入 math 包
import math

# 输出一个数字的自然对数
print(math.log(2.7183))
print(math.log(2))
print(math.log(1))
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
