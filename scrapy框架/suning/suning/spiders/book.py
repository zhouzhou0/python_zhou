# -*- coding: utf-8 -*-
import scrapy
import re
from copy import deepcopy

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/?safp=d488778a.error1.0.050951c125']

    def parse(self, response):
        #1.大分类
        menu_list=response.xpath("//div[@class='menu-list']//div[@class='menu-item']/dl")
        for dt in menu_list:
            item={}

            item["b_cate"]=dt.xpath("./dt//a/text()").extract_first()
            #小分类
            dd_list=dt.xpath(".//dd/a")
            for dd in dd_list:
                item["s_href"]=dd.xpath("./@href").extract_first()
                item['s_cate']=dd.xpath("./text()").extract_first()
                yield scrapy.Request(
                    item['s_href'],
                    callback=self.parse_book_list,
                    meta={"item":deepcopy(item)}
                )
                # print(item["s_href"])

    def parse_book_list(self,response):
        item=deepcopy(response.meta['item'])
        #图书列表页分组

        li_list=response.xpath("//div[@id='filter-results']//li")
        if item["s_href"]  not in ['https://list.suning.com/1-264008-0.html','https://list.suning.com/1-264006-0.html']:
            for li in li_list:
                # item['book_name']=li.xpath("//img/@alt").extract()
                item['book_url']=li.xpath("//div[@class='img-block']/a/@href").extract_first()
                # item['book_price']=li.xpath(".//em[@class='prive price ']/text()").extract_first()
                if item['book_url'] is not  None:
                    item['book_url']='https:'+item['book_url']
                    yield scrapy.Request(
                        item['book_url'],
                        callback=self.parse_book_detail,
                        meta={'item':deepcopy(item)}
                    )
            #翻页
        if item["s_href"] not in ['https://list.suning.com/1-264008-0.html',
                                      'https://list.suning.com/1-264006-0.html']:
            pageNumbers=int(re.findall(r'param.pageNumbers = "(.*?)";',response.body.decode())[0])
            currentPage=int(re.findall(r'param.currentPage = "(.*?)";',response.body.decode())[0])
                            # print(currentPage)
            if currentPage < pageNumbers:
                        if item['s_href'].split('.')[0] =='https://list':
                            ci=item['s_href'].split('-')[1]
                            currentPage+=1
                            next_url='https://list.suning.com/emall/showProductList.do?ci={}&pg=03&cp={}&il=0&iy=0&adNumber=0&n=1&ch=4&prune=0&sesab=ACBAAB&id=IDENTIFYING&cc=592'.format(ci,currentPage)
                            # print(ci)
                            # print(item['next_url'])
                            yield scrapy.Request(
                                 next_url,
                                    callback=self.parse_book_list,
                                     meta={'item': response.meta['item']}
                                    )



    def parse_book_detail(self,response):
        item=response.meta['item']
        item['book_price']=re.findall(r'"itemPrice":"(.*?)"',response.body.decode())[0]
        item['book_name']=response.xpath("//div[@class='proinfo-title']/h1/text()").extract_first()
        # item['book_name']=response.xpath("//ul[@class='bk-publish clearfix']//li[1]/text()").extract_first()
        item['book_name']=re.sub('[(\\r)(\\n)(\\t) ]','',item['book_name'])

        item['book_name']=item['book_name'] if len(item['book_name'])>0 else None
        item['author']=response.xpath("//ul[@class='bk-publish clearfix']//li[1]/text()").extract_first()
        item['author']=re.sub('[(\\r)(\\n)(\\t) ]','',item['author'])

        item['author']=item['author'] if len(item['author'])>0 else None

        # s = item['author'].encode()
        #
        # temp = s.decode('utf-8')
        #
        # pattern = "[\u4e00-\u9fa5]+"  # 中文正则表达式
        #
        # regex = re.compile(pattern)  # 生成正则对象 
        #
        # results = regex.findall(temp)
        # print(item['author'])
        item['publish']=response.xpath("//div[@class='proinfo-main']//li[@class='pb-item'][2]/text()").extract_first()
        if item['publish'] is not None:
            item['publish']=re.sub('[(\\r)(\\n)(\\t) ]','',item['publish'])
            item['publish'] = item['publish'] if len(item['publish']) > 0 else None
        item['book_img']=response.xpath("//div[@class='imgzoom-main']//img/@src").extract_first()
        item['book_img']='https:'+item['book_img']

        print(item)
        yield item
