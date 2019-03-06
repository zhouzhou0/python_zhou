# 打开后，从第五个字节开始读取


#打开读写指针在0处，即文件的开头
with open (r'test1.txt','r') as f :
   #seek移动单位是字节
    f.seek(3,0)
    c = f.read()
    print(c)


# 关于读取文件的练习
# 打开文件，三个字符一组读出内容，然后显示在屏幕上
# 每读一次，休息一秒钟
import time
with  open(r'test1.txt','r') as f :
    m = f.read(3)
    while m :
        print(m)
        time.sleep(1)
        m = f.read(3)


##
