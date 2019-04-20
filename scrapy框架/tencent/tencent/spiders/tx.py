# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TxSpider(CrawlSpider):
    name = 'tx'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']
    #第一个Rule实现详情页打解析，第二个Rule只实现翻页
    rules = (
        Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+&keywords=&tid=0&lid=0'), callback='parse_item',),
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+#a'),follow=True ),
    )

    def parse_item(self, response):
        item = {}
        item['title']=response.xpath("//td[@class='l2 bold size16']/text()").extract_first()
        item['acquire']=response.xpath("//div[text()='工作要求：']/../ul/li/text()").extract()
        print(item)
        return item
