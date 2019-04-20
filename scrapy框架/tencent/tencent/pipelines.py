# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from tencent.items import TencentItem

client = MongoClient('127.0.0.1', 27017)

collection=client['tencent']['hr']
class TencentPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,TencentItem):
            collection.insert(dict(item))
            print(item)
        return item


