from pymysql import connect

#创建连接对象
conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong',
               charset='utf8')

cs1=conn.cursor()
# print(cs1)
cs1.execute("insert into goods_cates (name) VALUE ('硬盘-new');")

cs1.execute("insert into goods_cates (name) VALUE ('硬盘2-new');")

cs1.execute("insert into goods_cates (name) VALUE ('硬盘3-new');")

conn.commit()  #在进行增删改的时候必须commit()，才会生效 不然数据不会进去

cs1.execute("insert into goods_cates (name) VALUE ('硬盘4-new');")

#自增长的主键id让他一直增长，不要去修改它
conn.rollback() #撤销之前增删改的内容