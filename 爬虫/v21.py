import requests

url = 'http://www.baidu.com'
#两种请求方式
# 使用get
rsp=requests.get(url)
print(rsp.text)

# 使用resquest
rsp=requests.request('get',url)
print(rsp.text)