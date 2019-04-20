# 安装 pip install scrapy
- scrapy框架介绍
    官网    - https://doc.scrapy.org/en/latest/
    中文文档 - http://scrapy-chs.readthedocs.io/zh_CN/latest/index.html
    
    - scrapy概述
    - 包含各个部件
        - ScrapyEngine：总指挥 负责数据和信号的在不同模块间的传递 神经中枢，大脑，核心、
        
        - Scheduler调度器：一个队列，存放引擎发来的request请求，调度器需要处理，然后交换引擎
        
        - Downloader下载器：把引擎发来的requests发出请求，得到response，把响应返回给引擎
        
        - Spider爬虫： 负责把下载器得到的网页/结果进行分解，分解成数据+链接
        
        - ItemPipeline管道： 详细处理Item
        
        - DownloaderMiddleware下载中间件： 自定义下载的功能扩展组件
        
        - SpiderMiddleware爬虫中间件：对spider进行功能扩展
    Scrapy入门
    1.创建一个scrapy项目
        scrapy startproject myspider
    2.生成一个爬虫
        scrapy genspider itcast "itcast.cn"  #itcast爬虫名 "itcast.cn"允许爬取的范围
    3.提取数据
        完善spider 使用xpath等方法
    4.保存数据
        pipline中保存数据
    
    完成pipeline代码后需要在色他听中设置开启        
    
### scrapy的数据流程
- 调取器---》request对象---》引擎---》下载中间件---》下载器
- 下载器发送请求，获取响应---》response---》下载中间件---》引擎---》爬虫中间件---》spider
- spider提取数据--- 》引擎---》pipeline
- spider提取的url地址---》构造request对象---》爬虫中渐渐---》引擎---》调度器


### scrapy的使用流程
- 创建项目 scrapy startproject 项目名
- 创建爬虫 scrapy genspider spider_name allow_domain
- 完善爬虫
  - start_url,response --> parse
  - 数据yield 通过传递给管道
  - 能够yield 的数据类型，dict，request，Item，None
- 管道
  - 开启管道
    - 开启管道，键:位置，值：距离引擎的远近，越小越近，说句越先经过

### logging 模块的使用
- scrapy
  - settings中设置LOG_LEVEL=“WARNING” #只会显示warning和warning以上等级的日志
  - settings中设置LOG_FILE="./a.log"  #设置日志保存的位置，设置会后终端不会显示日志内容
  - import logging,实例化logger的方式在任何文件中使用logger输出内容

- 普通项目中
  - import logging
  - logging.basicConfig(...) #设置日志输出的样式，格式
  - 实例化一个`logger=logging.getLogger(__name__)`
  - 在任何py文件中调用logger即可
        # from log_a import logger
        
  #如何实现翻页请求？？？
       1.找到下一页的url地址
       2.构造一个关于下一页url地址requests请求传给调度器
  >>>> scrapy.Request 能构造一个requests，同时指定提取数据打callback函数
  
  # scrapy.Request知识点
        scrapy.Request(url[,callback,method='GET',headers,body,cookies,meta,dont_filter=False])
        #注 ：一般文档中方括号中打参数表示可选择参数
        scrapy.Request常用参数：
            callback:指定传入url交给哪个解析函数去处理
            meta：实现在不同的解析函数中传递数据，meta默认会携带部分，比如下载延迟，请求深度等
            dont_filter：让scrapy的去重不会过滤当前url，scrapy默认有url去重的功能，对需要重复请求的url由重要用途
                比如百度贴吧，数据会更新，这时候我们就需要把dont_filter改为True
  
  在setting中可以设置User_Agent
  
  item的使用
    在items.py
        class MyspiderItem(scrapy.Item):   >scrapy.Item一个字典
             # define the fields for your item here like:
             name=scrapy.Field()   >scrapy.Field()一个字典
             name=scrapy.Field()
             name=scrapy.Field()
             name=scrapy.Field()
    在spider中
            from  myspider.items import  MyspiderItem
            item=MyspiderItem()  >>>实例化一个自定义的item
                                    item的操作和字典一样
        我们可以把定义的MyspiderItem理解为一个字典
        
        在获取数据的时候，使用不同的item来存放不同的数据
        在把数据交给pipeline的时候，可以通过isinstance(item,Myspderitem)来判断数据是属于哪个item，进行不同的数据（item）处理
        
        但是，把数据传入mongo只能为字典，而其实MyspiderItem也不是一个字典
        要把传进来的item转换为字典形式  dict(item)
        
        如果在爬虫中使用的键在 items.py中没有，就会报错
        
   ### scrapy数据流程
- 调度器---》request---》引擎---》下载中间件---》下载器
- 下载器发送请求，获取resposne，---》response--->下载中间件---》引擎---》爬虫中间件---》spider
- spider 提取数据---》引擎---》pipeline
- spider 提取url地址--》构造request---》爬虫中间件---》引擎---》调度器

### scrapy如何发送请求，能够携带什么参数
- scrapy.Request(url,callback,meta,dont_filter)
- dont_filter=True 表示请求过的url地址还会继续被请求


### scrapy如何把数据从一个解析函数传递到另一个，为什么需要这样做
- meta是个字典类型，meta = {"item":item}
- response.meta["item"]


### scrapy中Item是什么，如何使用
- Item 类，继承自scarpy.Item,name=scrapy.Field()
- Item 定义那些字段我们需要抓取
- 使用和字典一样
- 在mongodb中插入数据的时候 dict(item)

### pipeline中open_spider和close_spider是什么
- open_spdier 爬虫开启执行一次，只有一次
- close_spider 爬虫关闭的时候执行一次，只有一次


# scrapy-shell
- https://segmentfault.com/a/1190000013199636?utm_source=tag-newest
- shell 
- 启动
	- Linux： ctr+T,打开终端，然后输入scrapy shell "url:xxxx"
	- windows: scrapy shell "url:xxx"
	- 启动后自动下载指定url的网页
	- 下载完成后，url的内容保存在response的变量中，如果需要，我们需要调用response
- response
	- 爬取到的内容保存在response中给
	- response.body是网页的代码
	- resposne.headers是返回的http的头信息
	- response.xpath（）允许使用xpath语法选择内容
	- response.css()允许使用css语法选区内容
	
	- selector
	- 选择器，允许用户使用选择器来选择自己想要的内容
	- response.selector.xpath: response.xpath是selector.xpath的快捷方式
	- response.selector.css: response.css是他的快捷方式
	- selector.extract:把节点的内容用unicode形式返回
	- selector.re:允许用户通过正则选区内容
	
	
- settings
    在spider中，settings能够通过self.settings的方式来访问
- pipeline
import json
class JspmWriterPipeline(object):
    def open_spider(self,spider): #在爬虫开始的时候执行一次，仅仅执行一次
        self.file=open(spider.setting.get("SAVE_FILE","./temp.json"),'w')
    
    def close_spider(self,spider): #在爬虫关闭打时候执行一次仅仅执行一次
        self.file.close()
    
    def process_item(self,item,spider):
        line=json.dumps(dict(item))+"\n"
        self.file.write(line)
        return item  #不returnitem的情况下，另外一个权重比较低的pipeline就获取不到item
    
    
# scrapy中crawlspider
    回头看：
      之前的代码中，我们有很大一部分时间在寻找下一页的url地址或者是内容的url地址上面，这个过程能更简单一些么？

思路：
       1、从response中提取所有的a标签对应的url地址
	 2、自动的构造自己requests请求，发送给引擎

上面的功能可以做的更好：
       满足某个条件的url地址，我们才发送给引擎，同时能够指定callback函数

### crawlspider的使用 
- 常见爬虫 scrapy genspider -t crawl 爬虫名 allow_domain
- 指定start_url，对应的响应会进过rules提取url地址
- 完善rules，添加Rule ` Rule(LinkExtractor(allow=r'/web/site0/tab5240/info\d+\.htm'), callback='parse_item'),`

- 注意点:
  - url地址不完整，crawlspider会自动补充完整之后在请求
  - parse函数不能定义，他有特殊的功能需要实现
  - callback：连接提取器提取出来的url地址对应的响应交给他处理
  - follow：连接提取器提取出来的url地址对应的响应是否继续被rules来过滤


rules = (
    Rule(LinkExtractor(allow=r'type=4&page=\d+'), callback="parse_pages", follow=True),
)
在Rule规则 之后加个逗号，重新运行scrapy 爬虫，错误解决。。
 
   1.用命令创建一个crawlspider的模板 scrapy genspider -t crawl <爬虫名> <allowed_domains>
   2.crawlspider中不能再有以parse为名字打数据提取方法，这个方法被crawlspider用来实现基础url提取等功能
   3.一个Rule对象接收很多参数，首先第一个包含url的LinkExtractor对象，
    常用的还有callback(制定满足规则的url解析函数的字符串)和follow(response中提取的链接是否需要跟进)
   4.不指定callback函数打请求，如果follow为True，满足该rule的url还会被请求
   5.如果多个Rule满足一个url，会从rules中选择第一个满足的进行操作
   
   LinkExtractor更多常见参数
        allow：满足括号中“正则表达式”的url会被提取，如果为空，则全部匹配(url会自动补充完整)
        deny：满足括号中“正则表达式”一定不会被提取（优先级高于allow）
        allow_domains:会被提取的链接的domains
        deny_domains:一定不会被提取链接的domains
        restrict_xpaths:使用xpath表达式，和allow共同作用过滤链接，级xpath满足范围内的url地址会被提取
   
   spider.Rules常见参数
    link_extractor:是一个Link Extractor对象，用于定义需要提取的链接
    callback：  从link_extractor中每获取到链接时，参数所指定的值作为回调函数
    follow：是一个布尔（boolean）值 ，指定了跟据该规则从response提取的链接是否需要跟进
            如果callback为None，follow默认设置为True，否则默认为False
    process_links:指定该spider中哪个的函数将会被调用，从link_extractor中获取到链接列表将会调用该函数，
                该方法主要用来过滤url
    process_request:指定该spider中哪个函数会被调用，该规则提取到每个request时都会调用该函数，用来过滤request

- 完善spider
  - 1.start_url
  - 2.完善rules
    - 元组
    - Rule(LinkExtractor,callback，follow)
      - LinkExtractor 连接提取器，提取url
      - callback url的响应会交给该callback处理
      - follow= True url的响应会继续被Rule提取地址
  - 3.完善callback
(使用的场景：url地址的规律可以通过正则表示)

### crawlspider的使用的场景 
   url地址的规律可以通过正则或者xpath表示
   最终的页面有全部的数据的时候使用，如果没有，在callback中自动手动构造请求



下载中间件如何使用
- 定义类
- process_request 处理请求，不需要return
- process_response  处理响应，需要return request response
- settings中开启

    
# 下载中间件
    使用方法：
       编写一个Downloader Middlewares和我们编写一个pipeline一样，定义一个类，然后在setting中开启

   Downloader Middlewares默认的方法：
   process_request(self, request, spider)：
        当每个request通过下载中间件时，该方法被调用。
   process_response(self, request, response, spider)：
        当下载器完成http请求，传递响应给引擎的时候调用
        
   class RandomUserAgentMiddleware:
        def process_request(self,request,spider):
            ua=random.choice(spider.setting.get("USER_AGENTS_LIST"))
            request.headers['User-Agent']=ua
    
    
    
   class ProxyMiddleware:
        def process_request(self,request,spider):
            request.meta['proxy']="http://124.115.126.76:808"
                #添加代理，需要在request的meta信息中添加proxy字段
                #代理形式为：协议+ip地址+端口 
   
   
import random
import base64
   class RandomProxy(object):
         def process_request(self, request, spider):
             proxy = random.choice(PROXIES)
             if proxy['user_passwd'] is None:
             #  没有代理账户验证的代理使用方式
                request.meta['proxy'] = "http://" + proxy['ip_port']
             else:
             #  对账户密码进行 base64 编码转换
             base64_userpasswd = base64.b64encode(proxy['user_passwd'])
             #  对应到代理服务器的信令格式里
             request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd
             request.meta['proxy'] = "http://" + proxy['ip_port']
setting里面设置
                    PROXIES = [
                        {'ip_port': '111.8.60.9:8123', 'user_passwd': 'user1:pass1'},
                        {'ip_port': '101.71.27.120:80', 'user_passwd': 'user2:pass2'},
                        {'ip_port': '122.96.59.104:80', 'user_passwd': 'user3:pass3'},
                        {'ip_port': '122.224.249.122:8088', 'user_passwd': 'user4:pass4'},
                        ]


# scrapy模拟登陆
    为什么需要模拟登陆？
	获取cookie，能够爬取登陆后的页面

        回顾：
        requests是如何模拟登陆的？
            1、直接携带cookies请求页面
            2、找接口发送post请求存储cookie
        selenium是如何模拟登陆的？
            找到对应的input标签，输入文字点击登录
   scrapy模拟登陆之携带cookie
   
   # Disable cookies (enabled by default)
   #COOKIES_ENABLED = False   >>cookie在setting中默认是开启的
   
   COOKIES_DEBUG=True  在setting中添加该参数，可以看到cookie的传递情况
   
   [scrapy.downloadermiddlewares.cookies] DEBUG: Sending cookies to: 
    <GET http://www.renren.com/970089509/profile?v=info_timeline>
    
    携带cookies登    # headers={'Cookie':cookies}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
            # ,headers=headers cookie放入headers里面是不起效果的

        )
    
    模拟自动登录1
            post_data=dict(
            login='zhouzhou0',
        password='zhou1997.',
            authenticity_token=authenticity_token,
            utf8=utf8,
            commit=commit
        )
        yield scrapy.FormRequest(
            'https://github.com/session',
            formdata=post_data,
            callback=self.after_login
            
    模拟登入2 自动寻找form表单中的action
    如果对应的action有地址，使用FormRequest.from_response，自动提交到对应的action
       def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,#自动从response中寻找form表单
            formdata=dict(login="zhouzhou0",password="zhou1997."),
            callback=self.after_login

        )
    
