from urllib.parse import urlparse

o = urlparse("https:/www.runoob.com/?s=python+%E%95%99%E7%A8%88")
print(o)

from urllib.parse import urlparse

o = urlparse("https://www.runoob/com/?s=python+%E%95%99%E7%A8%8B")
print(o.scheme)