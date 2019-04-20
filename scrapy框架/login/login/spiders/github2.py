# -*- coding: utf-8 -*-
import scrapy

import re

class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,#自动从response中寻找form表单
            formdata=dict(login="zhouzhou0",password="****."),
            callback=self.after_login

        )

    def after_login(self,response):
        print(re.findall("zhouzhou0",response.body.decode()))