import multiprocessing
import time

class ClockProcess(multiprocessing.Process):
    '''
    两个函数比较重要
    1.init
    2.run
    '''
    def __init__(self,interval):
        super().__init__()
        self.interval=interval

    def run(self):
        while True:
            print('the time is %s'%time.ctime())
            time.sleep(self.interval)

if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
    while True:
        print('sleep.....')
        time.sleep(3)