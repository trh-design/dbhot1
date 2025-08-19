#!/usr/bin/python3

# 打开文件
fo = open("runoob.txt", "wb")
print("文件名为: ", fo.name)

# 关闭文件
fo.close()

#!/usr/bin/python3

# 打开文件
fo = open("runoob.txt", "wb")
print("文件名为: ", fo.name)

# 刷新缓冲区
fo.flush()

# 关闭文件
fo.close()

#!/usr/bin/python3

# 打开文件
fo = open("runoob.txt", "wb")
print("文件名为: ", fo.name)

fid = fo.fileno()
print("文件描述为: ", fid)

# 关闭文件
fo.close()

#!/usr/bin/python3

# 打开文件
fo = open("runoob.txt", "wb")
print("文件名为: ", fo.name)

ret = fo.isatty()
print("返回值: ", ret)

# 关闭文件
fo.close()

#!/usr/bin/python3

# 打开文件
fo = open("runoob.txt", "r+")
print("文件名为: ", fo.name)

line = fo.read(10)
print("读取的字符串: %s" % (line))

# 关闭文件
fo.close()

#!/usr/bin/python3

# 打开文件
fo = open("runoob.txt", "r+")
print("文件名为: ", fo.name)

line = fo.readline()
print("读取第一行: %s" % (line))

line = fo.readline(5)
print("读取的字符串为: %s" % (line))

# 关闭文件
fo.close()