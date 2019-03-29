import ftplib
import os
import socket


HOST = "ftp.acc.umu.se"
DIR = "pub/conspiracy/ "
FILE = 'hemlig.html'

# 客户端链接远程主机上的FTP服务器
try:
    f = ftplib.FTP()
    #通过设置调试级别可以方便调试
    f.set_debuglevel(2)
    #链接主机地址
    f.connect(HOST)
except Exception as e:
    print(e)
    exit()

print("COnntected to host{}".format(HOST))


#2.客户端输入用户名密码（或者“anonymous”和电子邮件地址）
try:
    f.login()
except Exception as e:
    print(e)
    exit()

print("***Logged in as 'anonymous'")

# 3. 客户端和服务器进行各种文件传输和信息查询操作
try:
    f.cwd(DIR)
except Exception as e:
    print(e)
    exit()
print("*** Changed dir to {0}".format(DIR))

try:
    # 从FTP服务器上下载文件
    # 第一个参数是ftp命令
    # 第二个参数是回调函数
    # 此函数的意思是，执行RETR命令，下载文件到本地后，运行回调函数
    f.retrbinary('RETR {0}'.format(FILE), open(FILE, 'wb').write)
except Exception as e:
    print(e)
    exit()
# 4. 客户端从远程FTP服务器退出，结束传输
f.quit()