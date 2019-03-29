import threading

sum = 0
loopsum=1000000

def myadd():
    global sum,loopsum
    for i in range(1,loopsum):
        sum+=1

def myminu():
    global sum,loopsum
    for i in range(1,loopsum):
        sum-=1
if __name__ == '__main__':
    print('start...{0}'.format(sum))

    # 开始多线程的实例，看执行结果是否一样
    t1=threading.Thread(target=myadd,args=())
    t2=threading.Thread(target=myminu,args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('done...{0}'.format(sum))