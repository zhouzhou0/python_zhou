import requests
from lxml import etree
import os,time
import random
headers_list=['Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
         'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
         'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
          ]
UserAgent=random.choice(headers_list)
# def down(url):
#     headers={'User-Agent':UserAgent}
#     res=requests.get(base_url,headers)
#     html=etree.HTML(res.text)
#     return html
#
# @down    #优化 可以选择函数装饰器
def mz_spider(base_url,headers):
    res=requests.get(base_url,headers)
    html=etree.HTML(res.text)
    # 获取详情页信息
    # img_src=html.xpath('//div[@class="footer"]/a/@href')
    img_src = html.xpath('//div[@class="postlist"]/ul/li/a/@href')
    for img_url in img_src:
        # print(img_url)
        img_parse(img_url)

def img_parse(img_url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'
    }
    res =requests.get(img_url,headers)
    html = etree.HTML(res.text)
    #获取标题
    title=html.xpath('//div[@class="content"]/h2/text()')[0]
    # print(title)
    page_num =html.xpath('//div[@class="pagenavi"]/a/span/text()')[-2]
    print(page_num)

    #拼接图片详情页地址
    for num in range(1,int(page_num)+1):
        img_src =img_url+"/"+str(num)
        download_img(img_src,title)
        # print(img_src)



#下载图片
def download_img(img_src,title):
    res=requests.get(img_src)
    html=etree.HTML(res.text)

    #获取图片地址
    img_url=html.xpath('//div[@class="main-image"]/p/a/img/@src')[0]

    #下载路径
    root_dir= 'mz_img'
    img_name=img_url.split('/')[-1]
    title= title.replace(' ','')

    root_dir=root_dir+"//"+title
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)
    res = requests.get(img_url,headers=headers)

    with open(root_dir+"//"+img_name,'wb') as f :
        f.write(res.content)
        f.close()
        print(title+'~'+img_name+'文件保存成功')




if __name__ == '__main__':
    headers={'User-Agent':'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
             'Referer':'http://www.mzitu.com'
             }
    for i in range(1,10):
        base_url="https://www.mzitu.com/page/{}/".format(str(i))
        mz_spider(base_url,headers)
        time.sleep(1)
