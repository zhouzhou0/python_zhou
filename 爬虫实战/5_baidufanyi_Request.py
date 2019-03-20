import json
from urllib import request,parse

# 使用request.Request

while True:
    baseurl = 'https://fanyi.baidu.com/sug'
    kw = input('请输入要翻译的词语')
    data={
        'kw':kw
    }
    data=parse.urlencode(data).encode()

    # 我们需要构造一个请求头，请求头部应该至少包含传入的数据长度
    # request需要传入的请求是dict格式
    headers={
        #因为我们使用的是post请求，至少应该包含Content-Length字段
        'Content-Length':len(data)

    }
    # 构建一个Request的实例
    req = request.Request(url=baseurl,data=data,headers=headers)
    # 一万已经构造了一个Request的请求实例,则所有的请求信息都可以封装Request

    # 有了headers data url 就可以尝试发出请求
    rsp =request.urlopen(req)
    json_data=rsp.read().decode()

    print(json_data)

    # json字符串转换为字典
    json_data=json.loads(json_data)
    print(json_data)

    for item in json_data['data']:
        print(item['k'],item['v'])