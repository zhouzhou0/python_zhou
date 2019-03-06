##### 编写一个程序，比较用户输入的文件是否相同，如果不同，显示出所有不同处的行号

#- f.readline()
#- open()
#- differ
file1 = input('请输入第一个文件名')
file2 = input('请输入第二个文件名')


def file_compare(file1,file2):
    f1 = open(file1)
    f2 = open(file2)

    count =  1#统计行数
    differ = []#统计不一样的数量
    for line1 in f1:

        line2=f2.readline()
        if line1 !=line2:
            differ.append(count)
        count+=1
    f1.close()
    f2.close()
    return  differ
differ = file_compare(file1,file2)
if len(differ) == 0:
    print('两个文件相同')
else:
    print('两个文件公有%d不同'%len(differ))
    for each in differ:
        print('第%d行不同'%each)