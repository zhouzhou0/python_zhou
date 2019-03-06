# 常用模块
- calendar
- time
- datetime
- timeit
- os
- shutil
- zip
- math
- string
- 上述所有模块使用理论上都应该先导入，string是特例
- calendar，time，datetime的区别参考中文意思****
# calendar
- 跟日历相关的模块
# time模块
### 时间戳
        - 一个时间表示，根据不同语言，可以是整数或者浮点数
        - 是从1970年1月1日0时0分0秒到现在经历的秒数
        - 如果表示的时间是1970年以前或者太遥远的未来，可能出现异常
        - 32位操作系统能够支持到2038年
### UTC时间
    - UTC又称为世界协调时间，以英国的格林尼治天文所在地区的时间作为参考的时间，也叫做世界标准时间。
    - 中国时间是 UTC+8 东八区
  
### 夏令时
    - 夏令时就是在夏天的时候将时间调快一小时，本意是督促大家早睡早起节省蜡烛！ 每天变成25个小时，本质没变还是24小时
    
### 时间元组 
    - 一个包含时间内容的普通元组
    
        
        索引      内容    属性            值

        0       年       tm_year     2015
        1       月       tm_mon      1～12
        2       日       tm_mday     1～31
        3       时       tm_hour     0～23
        4       分       tm_min      0～59
        5       秒       tm_sec      0～61  60表示闰秒  61保留值
        6       周几     tm_wday     0～6
        7       第几天    tm_yday     1～366
        8       夏令时    tm_isdst    0，1，-1（表示夏令时）
    

 
 

# strftime:将时间元组转化为自定义的字符串格式
'''
格式  含义  备注
%a  本地（locale）简化星期名称    
%A  本地完整星期名称    
%b  本地简化月份名称    
%B  本地完整月份名称    
%c  本地相应的日期和时间表示    
%d  一个月中的第几天（01 - 31）   
%H  一天中的第几个小时（24 小时制，00 - 23）   
%I  一天中的第几个小时（12 小时制，01 - 12）   
%j  一年中的第几天（001 - 366）  
%m  月份（01 - 12） 
%M  分钟数（00 - 59）    
%p  本地 am 或者 pm 的相应符    注1
%S  秒（01 - 61）  注2
%U  一年中的星期数（00 - 53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第 0 周   注3
%w  一个星期中的第几天（0 - 6，0 是星期天） 注3
%W  和 %U 基本相同，不同的是 %W 以星期一为一个星期的开始  
%x  本地相应日期  
%X  本地相应时间  
%y  去掉世纪的年份（00 - 99）    
%Y  完整的年份   
%z  用 +HHMM 或 -HHMM 表示距离格林威治的时区偏移（H 代表十进制的小时数，M 代表十进制的分钟数）      
%%  %号本身
'''  


# datetime模块
- datetinme提供日期和时间的运算和表示

    # datetime常见属性
# datetime.date: 一个理想和的日期，提供year, month, day属性


# datetime.time: 提供一个理想和的时间， 居于hour， minute，sec，microsec等内容
# datetime.datetime: 提供日期跟时间的组合
# datetime.timedelta: 提供一个时间差，时间长度
    
# datetime.datetime 模块
    - 提供比较好用的时间而已
    - 类定义
    
           class datetime.datetime(year, month, day[, hour
                    [, minute
                    [, second
                    [, microsecond
                    [, tzinfo]]]]])
          # The year, month and day arguments are required.
          MINYEAR <= year <= MAXYEAR
          1 <= month <= 12
          1 <= day <= n
          0 <= hour < 24
          0 <= minute < 60
          0 <= second < 60
          0 <= microsecond < 10**
    - 类方法
    
    `               
    datetime.today(): 返回当前本地datetime.随着 tzinfo None. datetime.fromtimestamp(time.time()).
    datetime.now([tz]): 返回当前本地日期和时间, 如果可选参数tz为None或没有详细说明,这个方法会像today().
    datetime.utcnow(): 返回当前的UTC日期和时间, 如果tzinfo None ,那么与now()类似.
    datetime.fromtimestamp(timestamp[, tz]): 根据时间戳返回本地的日期和时间.tz指定时区.
    datetime.utcfromtimestamp(timestamp): 根据时间戳返回 UTC datetime.
    datetime.fromordinal(ordinal): 根据Gregorian ordinal 返回datetime.
    datetime.combine(date, time): 根据date和time返回一个新的datetime.
    datetime.strptime(date_string, format): 根据date_string和format返回一个datetime.
    
    实例方法
    
    datetime.date(): 返回相同年月日的date对象.
    datetime.time(): 返回相同时分秒微秒的time对象.
    datetime.replace(kw): kw in [year, month, day, hour, minute, second, microsecond, tzinfo], 与date类似.
    类属性
    
    datetime.min: datetime(MINYEAR, 1, 1).
    datetime.max: datetime(MAXYEAR, 12, 31, 23, 59, 59, 999999).
    
    实例属性(read-only)
    
    datetime.year: 1 至 9999
    datetime.month: 1 至 12
    datetime.day: 1 至 n
    datetime.hour: In range(24). 0 至 23
    datetime.minute: In range(60).
    datetime.second: In range(60).
    datetime.microsecond: In range(1000000).    

# os-操作系统相关
    - 跟操作系统相关，主要是文件操作
    - 与系统相关的操作，主要包含在三个模块里
        - os， 操作系统目录相关
        - os.path, 系统路径相关操作
        - shutil， 高级文件操作，目录树的操作，文件赋值，删除，移动
        - 路径：
            - 绝对路径： 总是从根目录上开始
            - 相对路径： 基本以当前环境为开始的一个相对的地方
            #getcwd()获取当前的工作目录
            #格式os.getcwd()
            #返回值：当前工作目录的字符串
            #当前工作目录就是程序在进行文件相关操作，默认查找文件的目录 
            
            # chdir() 改变当前的工作目录
            # change directory
            #  格式：os.chdir（路径）
            #  返回值：无
        
            #listdir() 获取一个目录中所有子目录和文件的名称列表
            #格式 ：os.listdir(路径)
            #返回值：所有子目录和文件名称的列表
            
            #makedirs() 递归创建文件夹
            #格式 ：os.makedirs(递归路径)
            #返回值：无
            # 递归路径：多个文件夹层层包含的路径就是递归路径 如a/b/c
            
            #system() 运行系统shell命令
            #格式：os.system(系统命令)
            # 返回值：打开一个shell或者终端界面
            #一般推荐用subprocess代替
        
            #ls 是列出当前文件和文件夹的系统命令
            
            #getenv()获取指定的系统的环境变量值
            #相应的还有putenv 把环境变量放进去
            # 格式 ：os.getenv('环境变量名')
            #返回值 ：指定环境变量名对应的值
            
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
            
        # os.path 模块，跟路径相关的模块
        #abspath() 将路径转化为绝对路径
        #abselute()绝对
        # 格式：os.path.abspath('路径')
        #返回值 ：路径的绝对路径形式
            #linux:
                # . 点号，代表当前目录
                #.. 双点，代表父目录
        #basename() 获取路径中的文件名部分
        # 格式 ： os.path.basename('路径')
        #返回值：文件名字符串
        
        #join()将多个路径拼合成一个路径
        #格式 ： os.path.join(路径1，路径2)
        #返回值 ： 组合之后的新路径字符串
        
        # split() 将路径切割为文件夹部分和当前文件部分
        #  格式:os.path.split（'路径'）
        #  返回值：路径和文件名组成的元组
        
        #isdir() 检测是否是目录
        # 格式 ：os.path.isdir('路径')
        # 返回值： 布尔值
        
        #exists()检测文件或者目录是否存在
        #  格式：os.path.exists('路径')
        #  返回值:布尔值



# shutil 模块
        # copy() 复制文件
        #  格式：shutil.copy(来源路径，目标路径)
        #  返回值：返回目标路径
        # 拷贝的同时，可以给文件重命名
        
        # copy2() 复制文件，保留元数据（文件信息）
        #  格式：shutil.copy2(来源路径，目标路径)
        #  返回值：返回目标路径
        #  注意：copy和copy2的唯一区别在于copy2复制文件时尽量保留元数据
        
        # copyfile()将一个文件中的内容复制到另外一个文件当中
        #  格式：shutil.copyfile（'源路径','目标路径')
        #  返回值：无
        
        # move() 移动文件/文件夹
        #  格式：shutil.move(源路径，目标路径)
        #  返回值：目标路径！

    #归档和压缩
        - 归档： 把多个文件或者文件夹合并到一个文件当中
        - 压缩： 用算法把多个文件或者文件夹无损或者有损合并到一个文件当中
        
        # make_archive() 归档操作
        #  格式:shutil.make_archive('归档之后的目录和文件名','后缀','需要归档的文件夹')
        #  返回值：归档之后的地址
        #help(make_archive) 查看可用的后缀名
        
        #unpack_archive()解包操作
        #格式:shutil.unpack_archive("归档文件地址","解包后的地址")
        # 返回值：解包之后的地址
        
# zip - 压缩包
    - 模块名称叫 zipfile
    #zipfile.ZipFile(file[, mode[, compression[, allowZip64]]])
    # 创建一个ZipFile对象，表示一个zip文件。参数file表示文件的路径或类文件对象(file-like object)；参数mode指示打开zip文件的模式，默认值为’r’，表示读已经存在的zip文件，也可以为’w’或’a’，’w’表示新建一个zip文档或覆盖一个已经存在的zip文档，’a’表示将数据附加到一个现存的zip文档中。参数compression表示在写zip文档时使用的压缩方法，它的值可以是zipfile. ZIP_STORED 或zipfile. ZIP_DEFLATED。如果要操作的zip文件大小超过2G，应该将allowZip64设置为True。

    
    zf = zipfile.ZipFile("/home/tlxy/ooo.zip")
    # ZipFile.getinfo(name):
    #  获取zip文档内指定文件的信息。返回一个zipfile.ZipInfo对象，它包括文件的详细信息。将在下面 具体介绍该对象。
   
   
    # ZipFile.namelist()
    #  获取zip文档内所有文件的名称列表。
    
    # ZipFile.extractall([path[, members[, pwd]]])
    #  解压zip文档中的所有文件到当前目录。参数members的默认值为zip文档内的所有文件名称列表，也可以自己设置，

#random 随机数
    # random
        - 随机数
        - 所有的随机模块都是伪随机
    
    
    # choice() 随机返回序列中的某个值
    #  格式：random.choice(序列)
    #  返回值：序列中的某个值
    
    