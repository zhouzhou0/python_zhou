import time
import threading
def loop1(in1):
    print('start loop1 at :',time.ctime())
    print('我是参数in1',in1)
    time.sleep(4)
    print('end time at :',time.ctime())

def loop2(in1, in2):
    # ctime 得到当前时间
    print('Start loop 2 at :', time.ctime())
    # 把参数in 和 in2打印出来，代表使用
    print("我是参数 " ,in1 , "和参数  ", in2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print(' End loop 2 at:', time.ctime())

def main():
    print('start time at:',time.ctime())
    # 生成threading.Thread 实例
    t = threading.Thread(target=loop1,args=('小王',))
    t.start()

    t2=threading.Thread(target=loop2,args=('小明','小红'))
    t2.start()
    # 等待多线程执行完成
    t.join()
    t2.join()
    print('all ead at:',time.ctime())
if __name__ == '__main__':
    # 一定要有while语句
    # 因为启动多线程后本程序就作为主线程存在
    # 如果主线程执行完毕，则子线程可能也需要终止
    main()
    while True:
        time.sleep(2)
