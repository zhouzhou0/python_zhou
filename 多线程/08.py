import time
import threading
def loop1():
    # ctime得到当前的时间
    print('start loop 1 at:',time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(6)
    print('end loop 1 at :',time.ctime())

def loop2():
    print('start loop 2 at:',time.ctime())
    time.sleep(1)
    print('end loop 2 at :',time.ctime())

def loop3():
    print('start loop3 at:',time.ctime())
    time.sleep(5)
    print('end loop3 at:',time.ctime())

def main():
    print('starting at :',time.ctime())
    t1=threading.Thread(target=loop1,args=())
    t1.setName('THR_1')
    t1.start()

    t2=threading.Thread(target=loop2,args=())
    t2.setName('THR_2')
    t2.start()

    t3=threading.Thread(target=loop3,args=())
    t3.setName('THR_3')
    t3.start()

    time.sleep(3)
    # enumerate 得到正在运行的子线程  即子线程1和子线程3
    for thr in threading.enumerate():
        # getName得到线程的名字
        print('正在运行的线程是：{0}'.format(thr.getName()))
    print('正在运行的线程数量是{0}'.format(threading.activeCount()))
    print('all done at:',time.ctime())

if __name__ == '__main__':
    # 一定要有while语句
    # 因为启动多线程后本程序就作为主线程存在
    # 如果主线程执行完毕，则子线程可能也需要终止
    main()
    while True:
        time.sleep(2)