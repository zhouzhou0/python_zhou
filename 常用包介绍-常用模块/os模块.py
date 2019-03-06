import os
# getcwd()获取当前的工作目录
# 格式os.getcwd()
# 返回值：当前工作目录的字符串
# 当前工作目录就是程序在进行文件相关操作，默认查找文件的目录

coco= os.getcwd()
print(coco)

# chdir() 改变当前的工作目录
# change directory
#  格式：os.chdir（路径）
#  返回值：无
os.chdir('/home/tlxy')
coco=os.getcwd()
print(coco)

#listdir() 获取一个目录中所有子目录和文件的名称列表
#格式 ：os.listdir(路径)
#返回值：所有子目录和文件名称的列表
kd = os.listdir()
print(kd)

#makedirs() 递归创建文件夹
#格式 ：os.makedirs('递归路径')
#返回值：无
# 递归路径：多个文件夹层层包含的路径就是递归路径 如a/b/c
#rst = os.makedirs('cici')
#print(rst)

#system() 运行系统shell命令
#格式：os.system(系统命令)
# 返回值：打开一个shell或者终端界面
#一般推荐用subprocess代替

#ls 是列出当前文件和文件夹的系统命令
mm= os.system('ls')
print(mm)

#在当前目录下面创建一个coco.haha的文件
kk = os.system('touch coco.haha')
print(kk)
print(">"*30)
#getenv()获取指定的系统的环境变量值
#相应的还有putenv 把环境变量放进去
# 格式 ：os.getenv('环境变量名')
#返回值 ：指定环境变量名对应的值

m = os.getenv('PATH')
print(m)

#exti()退出当前程序
# 格式 ： exit()
#返回值：无

# 值部分
#- os.curdir: curretn dir ，当前目录
#- os.pardir: parent dir ,父亲目录
#- os.sep : 当前系统的路径分隔符
        #windows :"\"
        #linux : "/"

#- os.linesep: 当前系统的换行符号
        # windows : "\r\n"
        #unix,linux,macos:"\n"

#- os.name : 当前系统名称
    #- windows : nt
    #- unix,linux,macos: "posix"

print(os.curdir)
print(os.pardir)
print(os.sep)
print(os.linesep)

#在路径相关的操作中，不要手动拼写地址，因为手动拼写的路径可能不具有移植性
path = "/home/tlxy" + "/" + "coco"
print(path)

#linux 操作系统的名称是posix
print(os.name)

#abspath() 将路径转化为绝对路径
#abselute()绝对
# 格式：os.path.abspath('路径')
#返回值 ：路径的绝对路径形式
    #linux:
        # . 点号，代表当前目录
        #.. 双点，代表父目录

import os.path as op
absp = op.abspath('.')
print(absp)

#basename() 获取路径中的文件名部分
# 格式 ： os.path.basename('路径')
#返回值：文件名字符串
bn = op .basename('/home/tlxy')
print(bn)
#bn = op.basename('/home/tlxy/coco.haha')
bn = op.basename('/home/tlxy')
print(bn)

#join()将多个路径拼合成一个路径
#格式 ： os.path.join(路径1，路径2)
#返回值 ： 组合之后的新路径字符串
bd = "/home/tlxy"
fn = "coco.haha"
p = op.join(bd,fn)
print(p)


# split() 将路径切割为文件夹部分和当前文件部分
#  格式:os.path.split（'路径'）
#  返回值：路径和文件名组成的元组
t = op.split("/home/tlxy/coco.haha")
print(t)

d,p=op.split("/home/tlxy/coco.haha")
print(d,  p)


#isdir() 检测是否是目录
# 格式 ：os.path.isdir('路径')
# 返回值： 布尔值
rr=op.isdir("/home/tlxy")
print(rr)
dd=op.isdir("/home/tlxy/coco.haha")#这是一个文件
print(dd)

#exists()检测文件或者目录是否存在
#  格式：os.path.exists('路径')
#  返回值:布尔值

print(op.exists("/home"))
print(op.exists("/home/tlxy/haha"))
#####