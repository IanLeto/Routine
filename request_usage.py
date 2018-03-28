import requests
import json

response = requests.get('http://www.runoob.com/')

url_str = 'http://httpbin.org/'
res = requests.get(url_str)
# print(type(response))    # <class 'requests.models.Response'>
# print(response.status_code)  # 200
# print(response.text)     # 网页源码
# print(response.cookies)  # cookies (有更好的方法)
# requests.post('http://httpbin.org/post'
# response = requests.get(str+'get')
# print(response.text)
# 带参数的请求
# response = requests.get(str+'get'+'?name=gakki&age=24')
# print(response.text)
# # 带参数的请求奇摩鸡的写法
# data = {
#     'name': 'Gal',
#     'age': 30
# }
# response = requests.get(str+'get', params=data)
# print(response.text)
# # 解析json
#
# response = requests.get(str+'get')
# print(type(response.text))
# print(response.json())
# print(json.loads(response.text))
# print(type(response.json()))
# # 下载图片
#
# # response = requests.get('https://github.com/favicon.ico')
# # with open('favicon.icon', 'wb') as f:
# #     f.write(response.content)
# #     f.close()
#
# # 加入header 如果不加入header 返回错误500
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
# }
# response = requests.get('https://www.zhihu.com/explore', headers=headers)
# print(response.text)
#
# # post 请求 与get 基本相同
#

import requests

jianshu_url = 'http://www.jianshu.com'
res = requests.get(jianshu_url)
# exit() if not res.status_code == 200 else print('request successfully')
# # 如果请求code 为200 则请求成功
exit() if not res.status_code == requests.codes.ok else print(
    'request successfully')  # 换种写法

# 测试404
'''
    文件上传
'''

files = {
    'file': '我是文件'
}
res = requests.post(url_str + 'post', files)
print(res.text)
'''
    获取cookie
    比urllib 奇摩鸡多的
'''

res = requests.get(jianshu_url)
print(res.cookies)
print(list(map(print, res.cookies)))

'''
    会话维持
    cookie用来做会话维持的(不是能提取验证码????)
    模拟登陆
'''
# 输出结果为"cookies": {}
# 我们发送了两次请求,这两次请求是毫无关联相互独立的,所以cookie设置毫无意义
requests.get(url_str + 'cookies/set/number/123')
res = requests.get(url_str + 'cookies')
print(res.text)

'''
    维持该会话
    通过session发送两个请求
'''

s = requests.Session()
s.get(url_str + 'cookies/set/number/123')
res = s.get(url_str + 'cookies')
print(res.text)
# "cookies": {
#     "number": "123"
#   }
# res = requests.get('https://www.12306.cn') # 直接请求12306 会报异常(证书不合法)
# res = requests.get('https://www.12306.cn', verify=False)  仍然会报异常,但是至少状态码为200
# 消除证书错误
from requests.packages import urllib3
urllib3.disable_warnings()
res = requests.get('https://www.12306.cn', verify=False)
print(res.status_code)

