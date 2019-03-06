import shutil

# copy() 复制文件
#  格式：shutil.copy("来源路径"，"目标路径")
#  返回值：返回目标路径
# 拷贝的同时，可以给文件重命名


rst= shutil.copy("/home/tlxy/coco.haha","/home/tlxy/haha.haha")#复制之后并重命名
print(rst)

# copy2() 复制文件，保留元数据（文件信息）
#  格式：shutil.copy2(来源路径，目标路径)
#  返回值：返回目标路径
#  注意：copy和copy2的唯一区别在于copy2复制文件时尽量保留元数据

# copyfile()将一个文件中的内容复制到另外一个文件当中
#  格式：shutil.copyfile（'源路径','目标路径')
#  返回值：无
mm=shutil.copyfile("/home/tlxy/coco.haha","/home/tlxy/haha.haha")
print(mm)


# move() 移动文件/文件夹
#  格式：shutil.move(源路径，目标路径)
#  返回值：目标路径！
#bb= shutil.move("/home/tlxy/qaq","/home/tlxy/cici")
#print(bb)


# make_archive() 归档操作
#  格式:shutil.make_archive('归档之后的目录和文件名','后缀','需要归档的文件夹')
#  返回值：归档之后的地址
#help(make_archive) 查看可用的后缀名
oo= shutil.make_archive("/home/tlxy/ooo","zip","/home/tlxy/cici")
print(oo)

#unpack_archive()解包操作
#格式:shutil.unpack_archive("归档文件地址","解包后的地址")
# 返回值：解包之后的地址


