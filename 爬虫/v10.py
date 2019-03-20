'''
使用代理访问
'''


from urllib import request,error

if __name__ == '__main__':
    url='http://www.baidu.com'


    # -使用代理 基本使用步骤：
    #     1. 设置代理地址
    proxy={'http':'119.180.133.8:8060'}
    #     2. 创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    #     3. 创建Opener
    opener = request.build_opener(proxy_handler)
    #     4. 安装Opener
    request.install_opener(opener)

    # 现在就可以访问url，使用代理服务器

    try:
        rsp = request.urlopen(url)
        html=rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.HTTPError as e:
        print(e)
    except Exception as  e :
        print(e)