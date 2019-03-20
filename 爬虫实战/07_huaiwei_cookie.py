'''
urllib
模拟登入华为官网
url='https://www.huawei.com/en/accounts/LoginPost'
method=post

userName:shuaibin-zhou
pwd:T+uv4U+jEmiEX3TFBIggxEHqp1ZkhfDEk/pMnNRx4ZftU4BZtlax+MzUed8blmnH1ilO9kGec/pb21kcYXZOYcxAp+2xuFSF5yGRJhNf7FqbSfVX2ARN8rqsQ9GwLuEXt0nrRiyr3ukrKhigL/xDgsYpXXqzGOvRrRI51TrfERs=
languages:zh
fromsite:www.huawei.com
authMethod:password
'''



from urllib import request,parse
from http import cookiejar


url='https://www.huawei.com/en/accounts/LoginPost'
# 生成cookie对象
cookie=cookiejar.CookieJar()

# 生成cookie管理器
cookie_handler=request.HTTPCookieProcessor(cookie)
#生成http请求管理器
http_handler=request.HTTPHandler()
#生成https请求管理器
https_handler=request.HTTPSHandler()

#构建发起请求管理器
opener=request.build_opener(cookie_handler,http_handler,https_handler)


def login(url):
    data={
        'userName':'shuaibin-zhou',
        'pwd':'zhou@123.',
        'languages':'zh',
        'fromsite':'www.huawei.com',
        'authMethod':'password',
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'}
    data=parse.urlencode(data)
    # data数据类型为bytes
    req=request.Request(url,data=bytes(data,encoding='utf-8'))
    content=opener.open(req)
    content=content.read().decode('utf-8')
    print(content)



if __name__ == '__main__':
    url = 'https://www.huawei.com/en/accounts/LoginPost'
    login(url)
