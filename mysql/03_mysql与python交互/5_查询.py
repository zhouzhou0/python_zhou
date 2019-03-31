from pymysql import connect

def main():
    #创建connection
    conn= connect(host='localhost',port=3306,user='root',password='123456',database='jing_dong',
                  charset='utf8')


    cursor=conn.cursor()
    print(cursor.execute("select * from goods;"))  #查出来数据的行数
    # for i in range(20):
    #     print(cursor.fetchone())  #fetchone 一次查一条数据

    line_content=cursor.fetchone()
    print((line_content)[1])
    # for i in line_content:
    #     print(i)

    lines_content=cursor.fetchmany(5)
    print(lines_content)
    for temp in lines_content:
        print(temp)
    # print(cursor.fetchmany(3))  #fetchmany()跟参数 要显示多少条数据，出来的元组里面嵌元组
    # print(cursor.fetchall()) #把剩下的数据都打印出来


    cursor.close()
    conn.close()




if __name__ == '__main__':
    main()