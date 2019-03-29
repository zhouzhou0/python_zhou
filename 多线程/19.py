import multiprocessing
import time

def clock(inertval):
    while True:
        print('the time is %s'%time.ctime())
        time.sleep(inertval)

if __name__ == '__main__':
    p=multiprocessing.Process(target=clock,args=(5,))
    p.start()

