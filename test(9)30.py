import requests


kw = {'s':'python教程'}

headers = {"User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebkit/537.36( KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

response = requests.get("https://www.runoob.com/", params = kw, headers = headers)

print(response.status_code)

print(response.encoding)

print(response.url)

print(response.text)

import requests

x = requests.get('https://www.runoob.com/try//ajax/demo_post.php')

print(x.text)

import requests

myobj = {'fname':'Runoob', 'lname':'Boy'}

x = requests.get('https://www.runoob.com/try/ajax/demo-post2.php', data = myobj)

print(x.text)