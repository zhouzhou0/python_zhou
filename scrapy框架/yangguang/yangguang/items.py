# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


import scrapy


class YangguangItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    title = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    complainant = scrapy.Field()
    time = scrapy.Field()
    content=scrapy.Field()
    content_img = scrapy.Field()
    content_url = scrapy.Field()



