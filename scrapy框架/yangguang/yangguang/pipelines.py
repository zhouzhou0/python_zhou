# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
import re



class YangguangPipeline(object):
    def open_spider(self,spider):
        spider.hello = "world"
        client = MongoClient('127.0.0.1', 27017)
        self.collection = client['yangguang']['yg']

    def process_item(self, item, spider):
        spider.settings.get("MONGO_HOST")
        item['content']=self.process_content(item['content'])
        print(item)
        self.collection.insert(dict(item))
        return item

    def process_content(self,content):
        content=[re.sub("[(\\xa0)\s(\\xa3)(//r//n)]","",i) for i in content]
        content=[i for  i in content if len(i)>0] #去除列表中的空字符串
        return content
