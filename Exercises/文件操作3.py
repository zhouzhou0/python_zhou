#### 编写一个程序，当用户输入文件名和行数的时候，将该文件的前N行内容打印到屏幕上

#input 去接收一个文件名
#input 去接收一个行数

'''
file_name = input(r'请输入您要打开的文件')
line = input(r'你想要显示前几行')
def file_view(file_name,line):
    print('\n文件%s的前%s内容如下：'%(file_name,line))
    f = open(file_name)
    for i in range(int(line)):
        print(f.readline())
    f.close()
file_view(file_name,line)
'''


#### 我们在上一道题的基础上，增加一点功能，使用户可以随意的输入需要显示的行数

#- [12:42]
#- [:]
#- [:9]

#用以上的形式来表示我们想要打印的起始和结束的行数
file_name = input('请输入文件名')
line_num = input('请输入你要显示的行数，格式为[1:9]或者为 [:]')
def print_line(file_name,line_num):
    f = open(file_name)
    begin,end = line_num.split(':')
    if begin =='' :
        begin='1'
    if end == '':
        end = '-1'
    begin = int(begin)-1
    end = int(end)

    line = end - begin
    #消耗掉begin之前的函数    也可以用seek
    for i in range (begin):
        f.readline() #读取了，但不打出来
    if line < 0:
        print(f.read())
    else:
        for j in range (line):
            print(f.readline())
    f.close()
print_line(file_name,line_num)
