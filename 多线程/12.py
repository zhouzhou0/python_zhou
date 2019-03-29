import threading

sum=0
loopsum=1000000

lock=threading.Lock()

def myadd():
    global sum,loopsum
    for i in range(1,loopsum):
         #上锁，申请锁
            lock.acquire()
            sum +=1
            #释放锁
            lock.release()

def myminu():
    global sum,loopsun
    for i  in range(1,loopsum):
        lock.acquire()
        sum-=1
        lock.release()

if __name__=='__main__':
    # 开始多线程的实例，看执行结果是否一样
    print('start...{}'.format(sum))
    t1 = threading.Thread(target=myadd, args=())
    t2 = threading.Thread(target=myminu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('done...{0}'.format(sum))