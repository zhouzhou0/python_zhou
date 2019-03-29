import time
import threading

# 1. 类需要继承自threading.Thread
class Mythread(threading.Thread):
    def __init__(self,arg):
        # 必须要有super
        super(Mythread, self).__init__()
        self.arg=arg
    def run(self):
        time.sleep(2)
        print('args for this class are {}'.format(self.arg))
for i in range(5):
    t = Mythread(i)
    t.start()
    #等待多线程执行完成
    t.join()
print('main thread is done')