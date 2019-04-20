# -*- coding: utf-8 -*-
import scrapy
import re

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/970089509/profile']

    def start_requests(self):
        cookies="anonymid=jukxe1o5-viwgrh; depovince=GW; _r01_=1; ick_login=aca2bd97-611e-4a23-83aa-9982bf889757; jebecookies=32a09154-7019-4eaa-87c3-f9707568fcfb|||||; ick=be80c6ef-5a61-4487-96d3-ba84fb2387e1; __utma=151146938.1572342231.1555488012.1555488012.1555488012.1; __utmc=151146938; __utmz=151146938.1555488012.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _de=5844E06203B625AD62AFBDE27DE0F4E4; p=ecd3815813b3f6fc1041c505e90f79d19; first_login_flag=1; ln_uact=18950180694; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=f0fee7204d55e402fff9e870d28709439; societyguester=f0fee7204d55e402fff9e870d28709439; id=970089509; xnsid=d5b03861; ver=7.0; loginfrom=null; JSESSIONID=abc1XBnInHK438WA8tQOw; jebe_key=20f5815e-65db-40c2-8cc1-13b094e63203%7C35fcce1db1210aee8746eadf9d02231a%7C1555488034798%7C1%7C1555488034287; wp_fold=0"
        cookies={i.split('=')[0]:i.split('=')[1] for i in cookies.split(';')}
        # headers={'Cookie':cookies}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
            # ,headers=headers cookie放入headers里面是不起效果的

        )

    def parse(self, response):
        name=re.findall('周同学',response.body.decode())
        print(name)
        yield scrapy.Request(
            "http://www.renren.com/970089509/profile?v=info_timeline",
            callback=self.parse_detail
        )
    def parse_detail(self,response):
        a = re.findall('周同学',response.body.decode())
        print(a)
