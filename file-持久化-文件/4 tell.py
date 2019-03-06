# tell函数： 用来显示文件读写指针的当前位置
with open(r'test1.txt','r') as f :
    m = f.read(3)
    pos = f.tell()
    while m:
        print(pos)
        print(m)

        pos = f.tell()
        m = f.read(3)

        #tell 的返回数字的单位是byte
        #read是以字符为单位##