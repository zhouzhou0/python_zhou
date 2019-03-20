from urllib import request
import random

#代理
proxy_list=[
    {'https':'111.197.238.158:9999'},
    # {'http':'116.209.54.203:9999'},
    # {'http':'112.85.171.120:9999'}
]

proxy=random.choice(proxy_list)

# 创建代理管理器
proxy_handler=request.ProxyHandler(proxy)

# 创建网络请求对象opener
opener=request.build_opener(proxy_handler)

headers = {
'User-Agent':'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19'}

url='http://www.langlang2017.com'
req = request.Request(url,headers=headers)
response=opener.open(req)
content=response.read().decode()
print(content)
