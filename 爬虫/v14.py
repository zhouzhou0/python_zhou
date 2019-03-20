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





if __name__ == '__main__':
    '''
    执行玩login之后，会得到授权之后的cookie
    我们尝试把cookie打印出来
    
    '''
    login()
    print(cookie)
    for item in cookie:
        print(type(item))
        print(item)
        for i in dir(item):
            print(i)