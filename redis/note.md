安装：

1.获取redis资源

　　wget http://download.redis.io/releases/redis-4.0.8.tar.gz

2.解压

　　tar xzvf redis-4.0.8.tar.gz

3.安装

　　cd redis-4.0.8

　　make

　　cd src

　　make install PREFIX=/usr/local/redis

4.移动配置文件到安装目录下

　　cd ../

　　mkdir /usr/local/redis/etc

　　mv redis.conf /usr/local/redis/etc

 5.配置redis为后台启动

　　vi /usr/local/redis/etc/redis.conf //将daemonize no 改成daemonize yes

6.将redis加入到开机启动

　　vi /etc/rc.local //在里面添加内容：/usr/local/redis/bin/redis-server /usr/local/redis/etc/redis.conf (意思就是开机调用这段开启redis的命令)

7.开启redis

　　/usr/local/redis/bin/redis-server /usr/local/redis/etc/redis.conf 

卸载redis：

　　　　rm -rf /usr/local/redis //删除安装目录

　　　　rm -rf /usr/bin/redis-* //删除所有redis相关命令脚本

　　　　rm -rf /root/download/redis-4.0.4 //删除redis解压文件夹



8-启动redis:
两种方式：
redis-server &
加上`&`号使redis以后台程序方式运行
或者是

redis-server


9-检测后台进程是否存在
ps -ef |grep redis
10-检测6379端口是否在监听
netstat -lntp | grep 6379

原因: Redis已经启动

解决: 关掉Redis,重启即可

redis-cli shutdown
redis-server
然后你就能看到Redis愉快的运行了.

使用redis-cli客户端检测连接是否正常
redis-cli
127.0.0.1:6379> keys *
(empty list or set)
127.0.0.1:6379> set key "hello world"
OK
127.0.0.1:6379> get key
"hello world"
停止redis:
使用客户端

redis-cli shutdown
因为Redis可以妥善处理SIGTERM信号，所以直接kill -9也是可以的

kill -9 PID


#启动redis服务端
$ src/redis-server
 
 
#启动redis客户端
$ src/redis-cli



Redis客户端常见操作
Redis是key-value数据库，支持五种数据类型：string（字符串），hash（哈希），list（列表），set（集合）及zset(sorted set：有序集合)。

当value是string类型，命令包括set get setnx incr del 等。
> set server:name "fido"  // 设置键值
OK
> get server:name  // 获取键值
"fido"
> setnx connections 10   // set if not exists
OK
> incr connections   // 原子性增加values值
(integer) 11
> incr connections
(integer) 12
> del connections  // 删除key
(integer) 1
> incr connections
(integer) 1



当value是list类型，命令包括rpush lpush llen lrange lpop rpop del 等。


> rpush friends "Alice"   // 在末尾追加
(integer) 1
> rpush friends "Bob"
(integer) 2
> lpush friends "Sam"    // 插入到开头
(integer) 3
 
> lrange friends 0 -1     // 返回列表的子集，类似切片操作
1) "Sam"
2) "Alice"
3) "Bob"
> lrange friends 0 1
1) "Sam"
2) "Alice"
> lrange friends 1 2
1) "Alice"
2) "Bob"
 
> llen friends   // 返回列表长度
(integer) 3
> lpop friends   // 删除并返回列表第一个元素
"Sam"
> rpop friends   // 删除并返回列表最后一个元素
"Bob"
> lrange friends 0 -1
1) "Alice"
 
> del friends    // 删除key
(integer) 1     // 1表示成功，0表示失败



当value是set类型，命令包括sadd srem sismember smembers sunion del等。
> sadd superpowers "flight"     // 添加元素
(integer) 1
> sadd superpowers "x-ray vision"
(integer) 1
> sadd superpowers "reflexes"
(integer) 1
> srem superpowers "reflexes"   // 删除元素
1
 
> sismember superpowers "flight"   // 测试元素是否在集合中
(integer) 1
> sismember superpowers "reflexes"
(integer) 0
> smembers superpowers    // 返回集合中所有元素
1) "x-ray vision"
2) "flight"
 
> sadd birdpowers "pecking"
(integer) 1
> sadd birdpowers "flight"
(integer) 1
> sunion superpowers birdpowers    // 合并多个set，返回合并后的元素列表
1) "x-ray vision"
2) "flight"
3) "pecking"
 
> del superpowers   // 删除key

(integer) 1



当value是zset类型，命令包括 zadd zrange del等，注意给value一个编号用于排序。
> zadd hacker 1940 "Alan Kay"     // 给value指定一个编号，比如以年份1940作为编号
(integer) 1
> zadd hacker 1906 "Grace Hopper"
(integer) 1
> zadd hacker 1953 "Richard Stallman"
(integer) 1
> zadd hacker 1965 "Yukihiro Matsumoto"
(integer) 1
> zadd hacker 1916 "Claude Shannon"
(integer) 1
> zadd hacker 1969 "Linux Torvalds"
(integer) 1
> zadd hacker 1957 "Sophie Wilson"
(integer) 1
> zadd hacker 1912 "Alan Turing"
(integer) 1
 
> zrange hacker 2 4    // 切片返回有序集合中元素
1) "Claude Shannon"
2) "Alan Kay"
3) "Richard Stallman"
 
> del hacker    // 删除key

(integer) 1



当value是hash类型，hash类型可以理解为字典，需要给value指定一个field用于映射，命令包括hset hmset hget hgetall hdel hincrby del 等。


> hset user:1000 name "John Smith"   // 给value指定一个field，比如name
(integer) 1
> hset user:1000 email "john.smith@example.com"
(integer) 1
> hset user:1000 password "s3cret"
(integer) 1
> hgetall user:1000   // 获得hash表中所有成员，包括field和value
1) "name"
2) "John Smith"
3) "email"
4) "john.smith@example.com"
5) "password"
6) "s3cret"
 
> hmset user:1001 name "Mary Jones" password "hidden" email
"mjones@example.com"   // 设置多个field和value
OK
> hget user:1001 name   // 根据field获取value
"Mary Jones"
  
> hset user:1000 visits 10    // field可以映射到数字值
(integer) 1
> hincrby user:1000 visits 1    // 原子性增加value的值，增加1
(integer) 11
> hincrby user:1000 visits 10    // 增加10
(integer) 21
> hdel user:1000 visits      // 删除field及其value
(integer) 1
> hincrby user:1000 visits 1
(integer) 1
 
> del user:1000     // 删除key

(integer) 1



设置和查看key的生命周期，key过期会被自动删除，命令包括expire ttl 等。
> set resource:lock "Redis Demo"
OK
> expire resource:lock 120   // 设置生命周期为120s
(integer) 1
> ttl resource:lock   // 查看当前生命周期还剩多少时间
(integer) 109
> ttl resource:lock   // 120s后查看，返回-2表示已过期或不存在
(integer) -2
 
> set resource:lock "Redis Demo 2"
OK
> ttl resource:lock    // 返回-1表示永不过期
(integer) -1



查看linux上面是否有安装redis,redis启动
1、检测是否有安装redis-cli和redis-server;
[root@localhost bin]# whereis redis-cli
redis-cli: /usr/bin/redis-cli
 
[root@localhost bin]# whereis redis-server
redis-server: /usr/bin/redis-server


Linux系统下设置redis的密码
Linux系统下设置redis的密码：

1、进入redis操作的命令行

运行命令：redis-cli



2、查看现有的redis密码(可选操作，可以没有)

运行命令：config get requirepass如果没有设置过密码的话运行结果会如下图所示





3、设置redis密码

运行命令：config set requirepass ****(****为你要设置的密码)，设置成功的话会返回‘OK’字样



4、重启redis服务

ctrl+C退出当前的命令行模式后运行命令：

redis-cli -h 127.0.0.1 -p 6379 -a ****（****为你心设置的密码）

