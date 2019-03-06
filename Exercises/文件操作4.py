#### 编写一个程序，实现“全部替换”的功能

#- 打开一个文件
#- 把文件中 xxx这样的字符串，替换成 sss
#- open 打开文件
#- realine 读取文件内容
#- replace 替换
file_name = input('输入文件名')
rep_word = input('输入你要替换的字符')
new_word = input('输入替换的新字符')
def file_repacle(file_name,rep_word,new_word):
    f = open(file_name)
    content = []
    for each_line in f:
        if rep_word in each_line:
            each_line=each_line.replace(rep_word,new_word)
        content.append(each_line)
    decide = input('您确定要执行替换功能？输入YES/NOT')
    decide=decide.upper()

    if decide == 'YES':
        f_write = open(file_name,'w')
        f_write.write(''.join(content))
        f_write.close()
file_repacle(file_name,rep_word,new_word)

