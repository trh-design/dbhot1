#!/usr/bin/python3

import os, stat

path = "/tmp/foo/txt"

flags = stat.SF_NOUNLINK
retval = os.chflags( path, flags )
print("返回值: %s" % retval)

