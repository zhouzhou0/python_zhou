import threading
import time

class mythread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        if mutex.acquire(1):
            num = num+1
            msg=self.name+' set num to'+str(num)
            print(msg)
            mutex.acquire()
            mutex.release()
            mutex.release()
num=0
mutex=threading.RLock()
def ttt():
    for i in range(5):
        t=mythread()
        t.start()
if __name__ == '__main__':
    ttt()