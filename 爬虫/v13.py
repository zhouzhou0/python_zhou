from urllib import request,parse
from http import cookiejar


#创建cookiejar实例
cookie=cookiejar.CookieJar()
#生成cookie的管理器
cookie_handler=request.HTTPCookieProcessor(cookie)
#创建一个http请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

#创建请求管理器
opener=request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    '''
    负责初次登入
    需要用户输入用户名和密码，来获取cookie凭证
    :return:
    '''
    # 此url需要从登入form的action中查找
    url='http://www.renren.com/PLogin.do'

    # 次需要从登入from的两个对应的input中提取name属性
    data={
        "email":'18950180694',
        "password":"123456"
    }

    # 把数据进行编码
    data=parse.urlencode(data)

    req =request.Request(url,data.encode())
    # 使用opener发起请求
    rsp=opener.open(req)

def getHomepage():
    url = 'http://www.renren.com/970089509/profile'

    # 如果已经执行了login函数，则opener自动已经包含相应的cookie值
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open('COOKIE.html','w') as f :
        f.write(html)
if __name__ == '__main__':
    login()
    getHomepage()