import requests
from lxml import etree
import threading
from queue import Queue


class qiubaiSpdier:
    def __init__(self):
        self.url_temp='https://www.qiushibaike.com/text/page/{}/'
        self.headers={'User-Agent':'"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"'}
        self.url_queue=Queue()
        self.html_queue=Queue()
        self.content_queue=Queue()
    def get_url_list(self):
        # return [self.url_temp.format(i)  for i in range (1,14)]
        for i in range(1,14):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self):
        while True:#让线程反复的循环
            url=self.url_queue.get()
            print(url)
            response=requests.get(url,headers=self.headers)
            self.html_queue.put(response.content.decode())
            self.url_queue.task_done()

    def get_content_list(self):#提取数据
        while True:
            html_str=self.html_queue.get()
            html=  etree.HTML(html_str)
            div_list=html.xpath("//div[@id='content-left']/div")#分组
            content_list=[]
            for div in div_list:
                item={}
                item["content"]=div.xpath('.//div[@class="content"]/span/text()')
                item['autor_gender']=div.xpath('.//div[contains(@class,"articleGender")]/@class')
                item['autor_gender']=item['autor_gender'][0].split(" ")[-1].replace('Icon','') if len(item['autor_gender'])>0 else None
                item['autor_age']=div.xpath('.//div[contains(@class,"articleGender")]/text()')
                item['autor_img']=div.xpath('.//div[class="author clearfix"]//img/@src')
                item['autor_img']=item['autor_img'][0] if len(item['autor_img'])>0 else None
                item["stats_sove"]=div.xpath('.//div[@class="stats"]/i/text()')
                item["stats_sove"]=item["stats_sove"][0] if len(item["stats_sove"])>0 else None
                content_list.append(item)

            self.content_queue.put(content_list)
            self.html_queue.task_done()
        # return content_list
    def save_content_list(self):#保存
        while True:
            content_list=self.content_queue.get()
            for i in content_list:
                print(i)
            self.content_queue.task_done()

    def run(self): #实现主逻辑
        thread_list=[]
        #1.url_list
        t_url=threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)

        #2.遍历，发送请求，获取响应
        for i in range(20): #用20个线程来发送请求
            t_parse=threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)


        #3.提取数据
        for i in range(20):
           t_html= threading.Thread(target=self.get_content_list)
           thread_list.append(t_html)


        #4.保存
        t_save=threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)
        for t in thread_list:
            t.setDaemon(True)# 把子线程设置为守护线程，该线程不重要，主线程结束，子线程结束
            t.start()
        for q in [self.url_queue,self.html_queue,self.content_queue]:
            q.join()#让主线程等待阻塞，等待队列任务完成之后在完成
        print('主线程结束')

if __name__ == '__main__':
    qiubai=qiubaiSpdier()
    qiubai.run()