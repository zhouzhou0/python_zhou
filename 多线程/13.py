
#encoding=utf-8
import threading
import time

import queue

class producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            #qsize 返回queue的长度
            if queue.qsize() < 1000:
                for i in range(1000):
                    count+=1
                    msg='生成产品'+str(count)
                    # put是往queue放入一个值
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    #get是从queue中取出一个值
                    msg = self.name+'消费了'+queue.get()
                    print(msg)
            time.sleep(1)
if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(500):
        queue.put('初始产品'+str(i))
    for i in range(2):
        p = producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()
