import urllib.request

response = urllib.request.urlopen('https://www.zhihu.com/')
print(response.read().decode('utf-8'))