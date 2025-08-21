import time
print("time.altzone %d " % time.altzone)

import time
t = time.localtime()
print("time.asctime(t): %s " % time.asctime(t))

import time
print("time.ctime() : %s" % time.ctime())

import time
print("gmime :",time.gmtime(1455508609.34375))

import time
print("localtime(): ", time.localtime(145508609.34375))

import time

print("Start : %s" % time.ctime())
time.sleep(5)
print("End : %s" % time.ctime())

import time
struct_time = time.strptime("30 Nov 00", "%d %b %y")
print("返回元组: ", struct_time)

import time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

import time
print(time.time())