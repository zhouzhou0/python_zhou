import requests
from lxml import etree
import csv

class qiubaiSpdier:
    def __init__(self):
        self.url_temp='https://www.qiushibaike.com/text/page/{}/'
        self.headers={'User-Agent':'"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"'}
    def get_url_list(self):
        return [self.url_temp.format(i)  for i in range (1,14)]

    def parse_url(self,url):
        print(url)
        response=requests.get(url,headers=self.headers)
        return response.content.decode()
    def get_content_list(self,html_str):#提取数据
        html=  etree.HTML(html_str)
        div_list=html.xpath("//div[@id='content-left']/div")#分组
        content_list=[]
        for div in div_list:
            item={}
            item["content"]=div.xpath('.//div[@class="content"]/span/text()')
            item['autor_gender']=div.xpath('.//div[contains(@class,"articleGender")]/@class')
            item['autor_gender']=item['autor_gender'][0].split(" ")[-1].replace('Icon','') if len(item['autor_gender'])>0 else None
            item['autor_age']=div.xpath('.//div[contains(@class,"articleGender")]/text()')
            item['autor_img']=div.xpath('.//div[class="author clearfix"]//img/@src')
            item['autor_img']=item['autor_img'][0] if len(item['autor_img'])>0 else None
            item["stats_sove"]=div.xpath('.//div[@class="stats"]/i/text()')
            item["stats_sove"]=item["stats_sove"][0] if len(item["stats_sove"])>0 else None
            content_list.append(item)
        return content_list
    def save_content_list(self,contenr_list):#保存
        for i in contenr_list:
            print(i)

    def run(self): #实现主逻辑
        #1.url_list
        url_list = self.get_url_list()
        #2.遍历，发送请求，获取响应
        for url in url_list:
            html_str= self.parse_url(url)

        #3.提取数据
            content_list=self.get_content_list(html_str)


        #4.保存
            self.save_content_list(content_list)

if __name__ == '__main__':
    qiubai=qiubaiSpdier()
    qiubai.run()