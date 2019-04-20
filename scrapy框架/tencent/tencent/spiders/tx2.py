# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import urllib


class Tx2Spider(CrawlSpider):
    name = 'tx2'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    #Rule实现翻页，和当前页面的解析
    rules = (
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+#a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        tr_list=response.xpath("//table[@class='tablelist']/tr")[1:-1]
        for tr in tr_list:
            item['title']=tr.xpath("./td[1]/a/text()").extract_first()
            item['href']=tr.xpath("./td[1]/a/@href").extract_first()
            item['href']=urllib.parse.urljoin(response.url,item['href'])
            yield scrapy.Request(
                item['href'],
                callback=self.parse_detail,
                meta={'item':item}
            )

    def parse_detail(self, response):
        item=response.meta['item']
        item['acquire']=response.xpath("//div[text()='工作要求：']/../ul/li/text()").extract()
        print(item)
        return item
