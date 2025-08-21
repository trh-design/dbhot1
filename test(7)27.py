#!/usr/bin/python3

import os, sys
 
ret = os.access("/tmp/foo.txt", os.F_OK)
print("F_OK - 返回值 %s"% ret)

ret = os.access("/tmp/foo.txt", os.R_OK)
print("F_OK - 返回值 %s"% ret)

ret = os.access("/tmp/foo/txt", os.W_OK)
print("W_ok - 返回值 %s", ret)

ret = os.access("/tmp/foo/txt", os.X_OK)
print("X_OK - 返回值 %s", ret)

import os

os.replace('google.txt', 'runoob.txt')

import os

os.chroot("/tmp")

print("修改根目录成功!!")