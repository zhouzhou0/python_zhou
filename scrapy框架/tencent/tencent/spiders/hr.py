# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?lid=&tid=&keywords=python']

    def parse(self, response):
        tr_list=response.xpath("//table[@class='tablelist']//tr")[1:-1]#取第二个到最后一个
        for tr in tr_list:
            item=TencentItem()
            item['job']=tr.xpath('./td/a/text()').extract_first()
            item['cate']=tr.xpath('./td[2]/text()').extract_first()
            item['need_num']=tr.xpath('./td[3]/text()').extract_first()

            item['city']=tr.xpath('./td[4]/text()').extract_first()
            yield item
        #找到下一页的url地址
        next_url=response.xpath("//a[@id='next']/@href").extract_first()
        if next_url !="javascript:;":
            next_url='https://hr.tencent.com/'+next_url
            yield scrapy.Request( #能构造一个requests，同时指定提取数据打callback函数
                next_url,
                callback=self.parse
                # callback = self.parse1
                #meta={"item":item}
            )
    # def parse1(self, response):
        # response.meta['item']