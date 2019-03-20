'''
利用parse模块模拟post请求
分析百度=词典
1.打开F12
2. 输入girl，发现每敲一个字母都有请求
3.请求url是https://fanyi.baidu.com/sug
4.利用network-ALL-Herders查看发现FORMdata的值是kw：girl
5.检测返回的内容格式，发现返回的json格式，需要用到json包
'''
import json
import requests
from urllib import parse

'''
大致流程
1.利用data构造内容，然后urlopen打开
2.返回一个json格式的结果
3.结果就应该是girl的释义
'''
while True:
    baseurl = 'https://fanyi.baidu.com/sug'
    kw = input('请输入要翻译的词语')
    data={
        'kw':kw
    }
    # data=parse.urlencode(data).encode()

    # 我们需要构造一个请求头，请求头部应该至少包含传入的数据长度
    # request需要传入的请求是dict格式
    headers={
        #因为我们使用的是post请求，至少应该包含Content-Length字段
        'Content-Length':str(len(data))

    }
    # 有了headers data url 就可以尝试发出请求
    rsp =requests.post(baseurl,data=data,headers=headers)
    print(rsp.text)
    print(rsp.json())

    # print(json_data)

    # # json字符串转换为字典
    # json_data=json.loads(json_data)
    # print(json_data)


    # for item in json_data['data']:
        # print(item['k'],item['v'])