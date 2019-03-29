import threading
import time

loop = [4,2]

class ThreadFunc():
    def __init__(self,name):
        self.name=name
    def loop(self,nloop,nsec):
        '''
        :param nloop:  loop函数的名称
        :param nsec: 系统休眠时间
        :return:
        '''
        print('start loop',nloop,'at',time.ctime())
        time.sleep(nsec)
        print('done loop',nloop,'at',time.ctime())
def main():
    print('staring at:',time.ctime())
    # ThreadFunc("loop").loop 跟一下两个式子相等：
    # t = ThreadFunc("loop")
    # t.loop
    # 以下t1 和  t2的定义方式相等
    t = ThreadFunc("loop")
    t1=threading.Thread(target=t.loop,args=('LOOP1',4))
    t2 = threading.Thread(target=ThreadFunc('loop').loop,args=('LOOP2',2))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('all done at:',time.ctime())


if __name__ == '__main__':
    main()