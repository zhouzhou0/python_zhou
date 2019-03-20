'''
URL Error 的使用
'''
from urllib import error,request
if __name__ == '__main__':
    url="http://www.baiasdsadsadu.com"
    try:
        req = request.Request(url)
        rsq=request.urlopen(req)
        html = rsq.read().decode()
        print(html)
    except error.URLError as e:
        print(e.reason)
        print(e)
    except Exception as e:
        print(e)