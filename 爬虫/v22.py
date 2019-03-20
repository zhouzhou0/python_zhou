'''
使用headers和params
研究返回结果
'''
# 完整的url是下面url加上参数构成
url='https://www.baidu.com/s?'

import requests



kw={
    'wd':'王八蛋',
}
headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

rsp=requests.get(url,params=kw,headers=headers)
print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code) #请求返回码