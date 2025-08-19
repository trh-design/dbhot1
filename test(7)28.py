import os, sys

path = "/tmp"

retval = os.getcwd()
print("当前工作目录为: %s" % retval)

os.chdir( path )

retval = os.getcwd()

print("目录修改成功 %s" % retval)

import os

os.replace('google.txt', 'runoob.txt')