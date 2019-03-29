import requests
import random
import threading
from queue import Queue

from lxml import etree

class Spider():
    def __init__(self):
        self.url='http://dytt8.net/html/gndy/dyzz/list_23_{}.html'
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.detail_url = Queue()
        self.html_detail_queue = Queue()
        self.content_queue = Queue()
        self.BASE_DOMAIN='http://dytt8.net/'
        self.headers = {'User-Agent': '"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"'}

    def get_url_list(self):
        for i in range(1,14):
            self.url_queue.put(self.url.format(i))

    def parse_url(self):
        while True:
            url=self.url_queue.get()
            # print(url)
            response=requests.get(url,headers=self.headers)
            self.html_queue.put(response.text)
            self.url_queue.task_done()

    def get_detail_list(self):
        while True:
            html_str=self.html_queue.get()
            html=  etree.HTML(html_str)
            detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
            detail_urls = list(map(lambda url: self.BASE_DOMAIN + url, detail_urls))
            for detail_url in detail_urls:

                    self.detail_url.put(detail_url)
            self.html_queue.task_done()
    def get_content(self):
        while True:
            url=self.detail_url.get()
            # print(url)
            response = requests.get(url, headers=self.headers)
            self.html_detail_queue.put(response.content.decode('gbk'))
            self.detail_url.task_done()
    def get_contents(self):
        while True:
            content_list = []
            html_str=self.html_detail_queue.get()
            html = etree.HTML(html_str)
            title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
            Zooms = html.xpath("//div[@id='Zoom']//img/@src")
            poster = Zooms[0]
            screenshot = Zooms[1]
            movie = {'title': title, 'poster': poster, 'screenshot': screenshot}
            infos = html.xpath("//div[@id='Zoom']//text()")

            def parse_info(info, rule):
                return info.replace(rule, '').strip()  # strip去空格

            for index, info in enumerate(infos):
                if info.startswith("◎年　　代"):  # startswith以什么开头
                    info = parse_info(info, "◎年　　代")
                    # print(info)
                    movie['year'] = info
                elif info.startswith('◎产　　地'):
                    info = parse_info(info, '◎产　　地')
                    movie['country'] = info

                elif info.startswith('◎类　　别'):
                    info = parse_info(info, '◎类　　别')
                    movie['class'] = info
                elif info.startswith('◎豆瓣评分'):
                    info = parse_info(info, '◎豆瓣评分')
                    movie['score'] = info
                elif info.startswith('◎片　　长'):
                    info = parse_info(info, '◎片　　长')
                    movie['Running time'] = info
                elif info.startswith('◎导　　演'):
                    info = parse_info(info, '◎导　　演')
                    movie['director'] = info
                elif info.startswith('◎主　　演'):
                    info = parse_info(info, '◎主　　演')
                    actors = []
                    actors.append(info)
                    for x in range(index + 1, len(infos)):
                        actor = infos[x].strip()

                        if actor.startswith('◎'):
                            break
                        actors.append(actor)
                        # print(actor)
                    movie['actors'] = actors
                elif info.startswith('◎简　　介 '):
                    info = parse_info(info, '◎简　　介 ')
                    for x in range(index + 1, len(infos)):
                        profile = infos[x].strip()

                        if profile.startswith('【下载地址】'):
                            break
                        # print(profile)
                        movie['profile'] = profile
                    # content_list.append(movie)
            download_url = html.xpath("//td[@bgcolor='#fdfddf']//a/text()")[0]
            movie['download_url'] = download_url

            content_list.append(movie)
            self.content_queue.put(content_list)
            self.html_detail_queue.task_done()
    def save_content_list(self):#保存
        while True:
            content_list=self.content_queue.get()
            for i in content_list:
                print(i)
            self.content_queue.task_done()
    def run(self): #实现主逻辑
        thread_list = []
        t_url=threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)

        for i in range(10): #用20个线程来发送请求
            t_parse=threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)

        for i in range(30):
           t_html1= threading.Thread(target=self.get_detail_list)
           thread_list.append(t_html1)

        for i in range(30):
           t_html2= threading.Thread(target=self.get_content)
           thread_list.append(t_html2)

        for i in range(30):
           t_html3= threading.Thread(target=self.get_contents)
           thread_list.append(t_html3)
        t_save=threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)
        for t in thread_list:
            t.setDaemon(True)# 把子线程设置为守护线程，该线程不重要，主线程结束，子线程结束
            t.start()
        for q in [self.url_queue,self.html_queue,self.content_queue,self.detail_url,self.html_detail_queue,
                  self.content_queue]:
            q.join()#让主线程等待阻塞，等待队列任务完成之后在完成
        print('主线程结束')

if __name__ == '__main__':
    dytt=Spider()
    dytt.run()