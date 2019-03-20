from urllib import request
'''
使用urllib.request 请求一个网页内容，并把他内容打印出
'''

if __name__ == '__main__':
    url='https://www.51job.com/'
    # 打开相应的url并把相应页面作为返回
    res=request.urlopen(url)

    # 读取出来的内容是bytes
    html=res.read()
    print(type(html))
    # 需要解码
    html=html.decode('gbk')
    print(html)
