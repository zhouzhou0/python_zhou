'''

http://www.langlang2017.com/index.html

http://www.langlang2017.com/route.html

http://www.langlang2017.com/FAQ.html

Method:GET
'''
from urllib import request
import random


def spider(url):
    user_agent_list = ["Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Mobile Safari/537.36"]
    # 随机获取useragent
    user_agent = random.choice(user_agent_list)
    #print(user_agent_list)
    #构建headers头部信息
    headers = {'User-Agent':user_agent}
#     构建request对象
    req = request.Request(url=url,headers=headers)
    print(type(req))
    response = request.urlopen(req)
    html = response.read().decode()
    print(html)

    # 构建文件名
    name = url.split('/')

    fileName = 'PC_'+name[-1]

    print(fileName)

    with open(fileName,'w',encoding='utf-8') as f :
        f.write(html)

if __name__ == '__main__':
    url_list=[
        'http://www.langlang2017.com/index.html',
        'http://www.langlang2017.com/route.html',
        'http://www.langlang2017.com/FAQ.html',

    ]
    for url in url_list:
        spider(url)
