'''
https://tieba.baidu.com/f?ie=utf-8&kw=%E9%87%91%E5%BA%B8&fr=search&pn=0&

https://tieba.baidu.com/f?kw=%E9%87%91%E5%BA%B8&ie=utf-8&pn=50

https://tieba.baidu.com/f?kw=%E9%87%91%E5%BA%B8&ie=utf-8&pn=100



'''

from urllib import parse
from urllib import request

# k={'kw':'金庸'}
# u=parse.urlencode(k)
# print(u)
url = 'https://tieba.baidu.com/f?'
name= input('请输入贴吧名称:')
page = int(input('请输入贴吧页数'))

for i in range(page):
    qs={
        'kw':name,
        'pn':50*i

    }
    qs_date = parse.urlencode(qs)
    url = url + qs_date
    print(url)
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Mobile Safari/537.36'}

    req = request.Request(url=url,headers=headers)
    response = request.urlopen(req)

    html = response.read().decode()
    print(html)

    with open(name+'第'+str(i+1)+'页'+'.html','w',encoding='utf-8') as f :
        f.write(html)

