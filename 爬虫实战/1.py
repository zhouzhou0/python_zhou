# from urllib import request
#
# url = "http://www.baidu.com"
# resp=request.urlopen(url)
# print(resp)
# content = resp.read().decode('utf-8')
# print(content)

'''
w3c 资料简单爬取

url="http://www.w3school.com.cn/json/index.asp"

method:get
'''
# from urllib import request
# response = request.urlopen("http://www.w3school.com.cn/json/index.asp")
# content = response.read().decode('gb2312')
# print(content)

from urllib import request
from urllib import error

try:
    base_url = "http://www.w3school.com.cn/json/index.asp"
    response=request.urlopen(base_url)
    content = response.read().decode('gb2312')


except error.HTTPError as e:

    print(e)
except error.URLError as e:
    print('url错误异常')





