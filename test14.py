# -*- coding : UTF-8 -*-

# Filename : test.py  
# author : www.runoob.com

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}*{}={}\t'.format(j, i, j * i), end='')
        print()