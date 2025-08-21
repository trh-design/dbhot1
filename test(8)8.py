import os

current_dir = os.getcwdb()

files = os.listdir(current_dir)
print("目录下的文件:", files)

import glob
glob.glob('*.py')

import sys
print(sys.argv)