import urllib.request
import urllib.error

myURL1 = urllib.request.urlopen("https://www.runoob.com/")
print(myURL1.getcode())

try:
    myURL2 = urllib.request.urlopen("https://www.runoob.com/no.html")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(404)