#write案例
#1. 向文件中追加内容
#   a代表最佳方式打开
with open(r'test1.txt','a') as f :

    #\n为换行符
    f.write('生活还有诗和远方，\n life is very very nice')

# 可以直接写入行， 用writelines
# writelines表示写入很多行，参数可以是list格式
with open(r'test.txt','a') as f :
    f.writelines('biu biu biu ')

# w 表示覆盖之前的内容
l = [ 'coco','everyday','work']
with open (r'test.txt','w') as f :
    f.writelines(l)
##