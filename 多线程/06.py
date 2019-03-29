import time
import threading

def fun():
    print('start fun')
    time.sleep(2)
    print('edn fun')
print('main thread')
t1 = threading.Thread(target=fun,args=())
t1.start()
time.sleep(1)
print('main thread end')