test_dict = {"Runoob" : 1, "Google" : 2, "Taobao" : 3, "Zhihu" : 4}

# 输出原始的字典
print ("字典移除前 : " + str(test_dict))

# 使用 pop 移除 Zhihu
remove_value = test_dict.pop('Zhihu')

# 输出移除后的字典
print ("字典移除后 : " + str(test_dict))

print ("移除的 key 对应的 value 为 : " +str(remove_value))

print ('\r')

# 使用 pop() 移除没有的 key 不会发生异常，我们可以自定义提示信息
remove_value = test_dict.pop('Baidu', '没有该键(key)')

# 输出移除后的字典
print ("字典移除后 : " + str(test_dict))
print ("移除的值为 : " + str(remove_value))