from urllib import request,parse
if __name__ == '__main__':

    url='http://www.baidu.com/s?'
    wd = input('输入查找信息')
    #要想使用date，需要使用字典结构
    qs = {
        "wd":wd
    }
    print(qs)
#     使用url编码
    qs = parse.urlencode(qs)
    ful_url = url+qs
    print(ful_url)
    rsp=request.urlopen(ful_url)
    html=rsp.read()
    html=html.decode()
    print(html)
