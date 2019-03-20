'''
访问一个网站
更改自己的UserAgent进行伪装

User-Agent
'''
from urllib import request,error
if __name__ == '__main__':

    url='http://www.baidu.com'
    # try:
    #     headers={}
    #     headers['User-Agent'] = "Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
    #     req=request.Request(url,headers=headers)
    #

    # 第二种：使用add_header
    try:
        req =request.Request(url)
        req.add_header("User-Agent","Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
        #正常访问
        rsp =request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except error.HTTPError as e :
        print(e)
    except Exception as e :
        print(e)