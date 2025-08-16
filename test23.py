# Filename : test.py  
# author by : www.runoob.com  

# 用户输入字符
c = input("请输入一个字符: ")

# 用户输入 ASCII 码， 并将输入的数字转为整型
a = int(input("请输入一个 ASCII 码: "))

print( c + " 的ASCII码为", ord(c))
print( a , " 对应的字符为", chr(a))