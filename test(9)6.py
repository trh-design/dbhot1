import json

data1 = {
    'no' : 1,
    'name' : 'runoob',
    'url' : 'http//www.runoob.com'
}
json_str = json.dumps(data1)
print("Python 原始数据: ", repr(data1))
print("JSON 对象: ", json_str)

data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['name'])