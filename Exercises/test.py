file_name = input("请输入你要打开的文件名：")
rep_word = input("请输入你要替换的字符：")
new_word = input("请输入替换的新的字符串")

content = []
def file_replace(file_name, rep_word, new_word):
    f = open(file_name)

    global content

    for eachline in f:
        if rep_word in eachline:
            eachline = eachline.replace(rep_word, new_word)

        content.append(eachline)

    contentnt = content.append(eachline)
    decide = input("你确定要这样子做嘛？请输入 YES/NO")
    decide = decide.upper()

    if decide == 'YES':

        f_write = open(file_name, 'w')
        f_write.write("".join(content))
        f_write.close()


file_replace(file_name, rep_word, new_word)