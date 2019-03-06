#编写一个程序，接受用户输入的内容，并且保存为新的文件

#如果用户单独输入 :w  表示文件保存退出
file_name = input('请输入文件名称')
def file_write(file_name):
    f = open(file_name,'w')
    print('请输入内容，当你单独输入:w时候，保存退出')
    while True:
        wrie_someing =input()
        if wrie_someing == ':w':
            break#### 编写一个程序，比较用户输入的文件是否相同，如果不同，显示出所有不同处的行号


        else:
            #向文件中写入用户输入的内容
            f.write('%s\n'%wrie_someing)
    f.close()
file_write(file_name)

