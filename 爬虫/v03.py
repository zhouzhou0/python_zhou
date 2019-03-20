import urllib
import chardet

if __name__ == '__main__':
    url = 'https://www.zhaopin.com/'
    rsp = urllib.request.urlopen(url)

    print(type(rsp))
    print(rsp)

    print('geturl---{}'.format(rsp.geturl()))
    print('info---{}'.format(rsp.info()))
    print('getcode---{}'.format(rsp.getcode()))
    # html = rsp.read()
    #
    # # 利用利用chardet自动检测
    # cs = chardet.detect(html)
    # print(type(cs))
    # print(cs)
    # # 使用get取值保证不会出错
    #
    # html = html.decode()
    # print(html)