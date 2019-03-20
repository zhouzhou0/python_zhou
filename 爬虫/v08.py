'''
 HTTPError
'''
from urllib import error,request
if __name__ == '__main__':
    url="http://www.sipo.gov.cn/ww"
    try:
        req = request.Request(url)
        rsq=request.urlopen(req)
        html = rsq.read().decode()
        print(html)
    except error.HTTPError as e:
        print('HTTPError....{}'.format(e.reason))
        print('HTTPError...{}'.format(e))

    except error.URLError as e:
        print('URLError....{}'.format(e.reason))
        print('URLError....{}'.format(e))

    except Exception as e:
        print(e)