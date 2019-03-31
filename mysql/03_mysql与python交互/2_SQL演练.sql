SQL演练
1. SQL语句的强化
查询类型cate_name为 '超极本' 的商品名称、价格
select name,price from goods where cate_name = '超级本';
显示商品的种类
select cate_name from goods group by cate_name;
求所有电脑产品的平均价格,并且保留两位小数
select round(avg(price),2) as avg_price from goods;
显示每种商品的平均价格
select cate_name,avg(price) from goods group by cate_name;
查询每种类型的商品中 最贵、最便宜、平均价、数量
select cate_name,max(price),min(price),avg(price),count(*) from goods group by cate_name;
查询所有价格大于平均价格的商品，并且按价格降序排序
select id,name,price from goods 
where price > (select round(avg(price),2) as avg_price from goods) 
order by price desc;

查询每种类型中最贵的电脑信息
select * from goods
inner join 
    (
        select
        cate_name, 
        max(price) as max_price, 
        min(price) as min_price, 
        avg(price) as avg_price, 
        count(*) from goods group by cate_name
    ) as goods_new_info 
on goods.cate_name=goods_new_info.cate_name and goods.price=goods_new_info.max_price;
2. 创建 "商品分类"" 表
-- 创建商品分类表

查询goods表中商品的种类
select cate_name from goods group by cate_name;
将分组结果写入到goods_cates数据表
insert into goods_cates (name) select cate_name from goods group by cate_name;
3. 同步表数据
通过goods_cates数据表来更新goods表
update goods as g inner join goods_cates as c on g.cate_name=c.name set g.cate_name=c.id;
4. 创建 "商品品牌表" 表
通过create...select来创建数据表并且同时写入记录,一步到位
-- select brand_name from goods group by brand_name;

-- 在创建数据表的时候一起插入数据
-- 注意: 需要对brand_name 用as起别名，否则name字段就没有值
create table goods_brands (
    id int unsigned primary key auto_increment,
    name varchar(40) not null) select brand_name as name from goods group by brand_name;
5. 同步数据
通过goods_brands数据表来更新goods数据表
update goods as g inner join goods_brands as b on g.brand_name=b.name set g.brand_name=b.id;
6. 修改表结构
查看 goods 的数据表结构,会发现 cate_name 和 brand_name对应的类型为 varchar 但是存储的都是数字
desc goods;
通过alter table语句修改表结构
alter table goods  
change cate_name cate_id int unsigned not null,
change brand_name brand_id int unsigned not null;
7. 外键
分别在 goods_cates 和 goods_brands表中插入记录
insert into goods_cates(name) values ('路由器'),('交换机'),('网卡');
insert into goods_brands(name) values ('海尔'),('清华同方'),('神舟');
在 goods 数据表中写入任意记录
insert into goods (name,cate_name,brand_name,price)
values('LaserJet Pro P1606dn 黑白激光打印机', 12, 4,'1849');
查询所有商品的详细信息 (通过内连接)
select g.id,g.name,c.name,b.name,g.price from goods as g
inner join goods_cates as c on g.cate_id=c.id
inner join goods_brands as b on g.brand_id=b.id;
查询所有商品的详细信息 (通过左连接)
select g.id,g.name,c.name,b.name,g.price from goods as g
left join goods_cates as c on g.cate_id=c.id
left join goods_brands as b on g.brand_id=b.id;
如何防止无效信息的插入,就是可以在插入前判断类型或者品牌名称是否存在呢? 可以使用之前讲过的外键来解决

外键约束:对数据的有效性进行验证

关键字: foreign key,只有 innodb数据库引擎 支持外键约束
对于已经存在的数据表 如何更新外键约束
-- 给brand_id 添加外键约束成功
alter table goods add foreign key (brand_id) references goods_brands(id);
-- 给cate_id 添加外键失败
-- 会出现1452错误
-- 错误原因:已经添加了一个不存在的cate_id值12,因此需要先删除
alter table goods add foreign key (cate_id) references goods_cates(id);
如何在创建数据表的时候就设置外键约束呢?

注意: goods 中的 cate_id 的类型一定要和 goods_cates 表中的 id 类型一致

create table goods(
    id int primary key auto_increment not null,
    name varchar(40) default '',
    price decimal(5,2),
    cate_id int unsigned,
    brand_id int unsigned,
    is_show bit default 1,
    is_saleoff bit default 0,
    foreign key(cate_id) references goods_cates(id),
    foreign key(brand_id) references goods_brands(id)
);
如何取消外键约束
-- 需要先获取外键约束名称,该名称系统会自动生成,可以通过查看表创建语句来获取名称
show create table goods;
-- 获取名称之后就可以根据名称来删除外键约束
alter table goods drop foreign key 外键名称;
在实际开发中,很少会使用到外键约束,会极大的降低表更新的效率