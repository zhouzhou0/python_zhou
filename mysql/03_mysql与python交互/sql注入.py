from pymysql import connect


#sql注入 输入 'or 1=1 or'1  (引号也要输入)即可显示所有数据

class JD(object):
    def __init__(self):
        #创建connect连接
        self.conn=connect(host='localhost',port=3306,user='root',password='123456',database='jing_dong',charset='utf8')
        #获得cursor对象
        self.cursor=self.conn.cursor()
    def __del__(self):
        # 关闭cursor对象
        # 关闭连接
        self.cursor.close()
        self.conn.close()

    def execute_sql(self,sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        sql='select * from goods'
        self.execute_sql(sql)

    def show_cates(self):
        sql = 'select name from goods_cates;'
        self.execute_sql(sql)

    def show_brands(self):
        sql = 'select name from goods_brands;'
        self.execute_sql(sql)

    def add_brands(self):
        item_name=input('输入新商品分类的名称')

        sql='insert into goods_brands (name) values("%s")'%item_name
        self.cursor.execute(sql)
        self.conn.commit()

    def get_info_by_name(self):
        find_name=input('请输入要查询的商品的名字')
        sql="select * from goods where name='%s';"%find_name
        print('---->%s<-----'%sql)
        self.execute_sql(sql)
    @staticmethod
    def print_menu():
        print("...京东商城")
        print('1.所有的商品')
        print('2.所有商品分类')
        print('3.所有商品品牌分类')
        print('4.添加一个商品')
        print('5.根据名字查询一个商品')
        num = int(input('请输入功能对应的序号：(输入999退出查询)'))
        return num

    def run(self):
        while True:
            num=self.print_menu()
            if num ==1:
                #查询所有商品
                self.show_all_items()
            elif num==2:
                #查询所有商品分类
                self.show_cates()

            elif num==3:
                #显示品牌分类
                self.show_brands()
            elif num==4:
                #添加品牌分类
                self.add_brands()
            elif num==5:
                #根据名字查询商品
                self.get_info_by_name()

            elif num==999:
                print('O(∩_∩)O谢谢您的使用')
                break

            else:
                print('输入有误,重新输入......')


def main():
    #1.创建一个京东商城对象
    jd=JD()
    #2. 调用这个对象的run方法，让其运行
    jd.run()

if __name__ == '__main__':
    main()