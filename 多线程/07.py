import time
import threading

def fun():
    print('start fun')
    time.sleep(2)
    print('edn fun')
print('main thread')
t1 = threading.Thread(target=fun,args=())

#守护线程 线程会在主线程结束的时候自动退出
t1.setDaemon(True)
# 或t1.deamon=Ture

t1.start()
time.sleep(1)
print('main thread end')