with open(r'test.txt','r') as f :
    pass
    #下面语句块开始对文件f进行操作
    #在本模块中不需要在使用close关闭文件f


    #按行读取内容
    strline = f.readline()
    #此机构保证能够完整读取文件直到结束
    while strline:
        print(strline)#只要strline不为空，就打印
        strline = f.readline()  #再读取一行,一次循环

print('*'*60)

# list能用打开的文件作为参数，把文件内每一行内容作为一个元素
with open(r'test.txt','r') as f:
    # 以打开的文件f作为参数，创建列表
    l = list(f)
    for line in l :
        print(line)

print('*'*60)

#read是按字符读取文件内容
#允许输入参数决定读取几个字符，如果没有制定，从当前位置读取到结尾
#否则，从当前位置读取指定个数字符
with open(r'test.txt','r') as f:
    strChar = f.read()
    print(len(strChar))
    print(strChar)
print('*'*30)
with open(r'test.txt', 'r') as f:
    c = f.read(1)
    while c :
        print(c,end='')
        c = f.read(1)
##