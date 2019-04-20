# -*- coding: utf-8 -*-
import scrapy
from yangguang.items import YangguangItem
# import logging
from yangguang.settings import MONGO_HOST

# logger=logging.getLogger(__name__)

class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        # self.settings["MONGO_HOST"]
        # self.settings.get("MONGO_HOST","")
        #分组
        print(self.hello,"*"*100)
        item=YangguangItem()
        tr_list=response.xpath("//div[@class='greyframe']//table[2]//tr/td/table//tr")
        for tr in tr_list:
            item['id']=tr.xpath("./td[1]/text()").extract_first()
            item['title']=tr.xpath("./td[2]/a[2]/text()").extract_first()
            item['content_url']=tr.xpath("./td[2]/a[2]/@href").extract_first()
            item['city']=tr.xpath("./td[2]/a[3]/text()").extract_first()
            item['state']=tr.xpath("./td[3]/span/text()").extract_first()
            item['complainant']=tr.xpath("./td[4]/text()").extract_first()
            item['time']=tr.xpath("./td[5]/text()").extract_first()
            # logger.warning(item)
            # yield item
            yield scrapy.Request(
                item['content_url'],callback=self.parse_detail,
                meta={"item":item}
            )
        next_url=response.xpath("//a[text()='>']/@href").extract_first()

        if next_url != None:
            yield scrapy.Request(next_url,callback=self.parse)

    def parse_detail(self,response):#处理详情页
        item=response.meta['item']
        item['content']=response.xpath("//div[@class='wzy1']//td[@class='txt16_3']/text()").extract()
        item['content_img']=response.xpath("//div[@class='wzy1']//td[@class='txt16_3']//img/@src").extract()
        item['content_img']=["http://wz.sun0769.com"+ i for i in item['content_img']]
        # print(item)
        yield item



