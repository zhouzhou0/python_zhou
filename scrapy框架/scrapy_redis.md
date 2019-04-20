
###SCRAPY_REDIS

Scrapy_redis ： Redis-based components for Scrapy.

Github地址：https://github.com/rmax/scrapy-redis

Scrapy_redis在scrapy的基础上实现了更多，更强大的功能，具体体现在：reqeust去重，爬虫持久化，和轻松实现分布式

#Scrapy_redis之domz
#setting

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  >>>指定那个去重方法给request对象去重

SCHEDULER = "scrapy_redis.scheduler.Scheduler"     >>>指定scheduler队列

SCHEDULER_PERSIST = True   >>>队列内容是否持久保存，为False的时候关闭redis的时候清空redis

ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,   >>scrapy_redis实现的items保存到redis的pipeline
}

REDIS_URL="redis://127.0.0.1:6379"  >>指定redis的地址

redis地址也可以这么写
#REDIS_HOST=“192.168.207.134”
#REDIS_PORT=6379


#我们尝试在setting中关闭redispipeline
结果变化：requests有变化(变多或者变少或者不变)
dupefilter 变多
items 不变
变化结果分析：redispipeline中仅仅实现了item数据存储到redis的过程，我们可以新建一个pipeline，让数据存储到任意地方


#scrapy_redis如何生成指纹的？
import hashlib
In [3]: f = hashlib.sha1()

In [4]: f.update("哈哈哈哈".edcode())

In [10]: f.hexdigest()
Out[10]: 'ef9cf2a891eaaa71d63d217c898063ee56aaac23'


### request对象什么时候入队
- dont_filter = True ,构造请求的时候，把dont_filter置为True，该url会被反复抓取（url地址对应的内容会更新的情况）
- 一个全新的url地址被抓到的时候，构造request请求
- url地址在start_urls中的时候，会入队，不管之前是否请求过
  - 构造start_url地址的请求时候，dont_filter = True

```python
def enqueue_request(self, request):
    if not request.dont_filter and self.df.request_seen(request):
        # dont_filter=False Ture  True request指纹已经存在  #不会入队
        # dont_filter=False Ture  False  request指纹已经存在 全新的url  #会入队
        # dont_filter=Ture False  #会入队
        self.df.log(request, self.spider)
        return False
    self.queue.push(request) #入队
    return True
```

### scrapy_redis去重方法
- 使用sha1加密request得到指纹
- 把指纹存在redis的集合中
- 下一次新来一个request，同样的方式生成指纹，判断指纹是否存在reids的集合中

### 生成指纹
```python
fp = hashlib.sha1()
fp.update(to_bytes(request.method))  #请求方法
fp.update(to_bytes(canonicalize_url(request.url))) #url
fp.update(request.body or b'')  #请求体
return fp.hexdigest()
```
### 判断数据是否存在redis的集合中，不存在插入
```python
added = self.server.sadd(self.key, fp)
return added != 0
```

