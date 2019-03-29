'''
利用time来生成两个函数
顺序调用
计算总的运行时间
'''

import time
def loop1():
    # ctime得到当前的时间
    print('start loop 1 at:',time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('end loop 1 at :',time.ctime)

def loop2():
    print('start loop 2 at:',time.ctime())
    time.sleep(2)
    print('end loop 2 at :',time.ctime())
def main():
    print('starting at :',time.ctime())
    loop1()
    loop2()
    print('all done at:',time.ctime())
if __name__ == '__main__':

    main()

