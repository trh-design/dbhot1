lis = [{ "name" : "Taobao", "age" : 100},
{ "name" : "Runoob", "age" : 7},
{ "name" : "Google", "age" : 100},
{ "name" : "Wiki", "age" : 200}]

# 通过 age 升序排序
print ("列表通过 age 升序排序: ")
print (sorted(lis, key = lambda i : i['age']))

print ("\r")

# 先按 age 排序, 再按 name 升序
print ("列表通过 age 和 name 排序: ")
print (sorted(lis, key = lambda i :(i['age'], i['name'])))

print ("\r")

# 按 age 降序排序
print ("列表通过 age 降序排序")
print (sorted(lis, key = lambda i : i['age'],reverse=True))