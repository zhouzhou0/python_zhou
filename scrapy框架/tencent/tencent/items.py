# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    job = scrapy.Field()
    cate = scrapy.Field()
    need_num = scrapy.Field()
    city = scrapy.Field()


# class MyspiderItem(scrapy.Item):
#            # define the fields for your item here like:
#     name = scrapy.Field()
#
# class MyspiderItem2(scrapy.Item):
#            # define the fields for your item here like:
#     name = scrapy.Field()
#
# class MyspiderItem3(scrapy.Item):
#            # define the fields for your item here like:
#     name = scrapy.Field()