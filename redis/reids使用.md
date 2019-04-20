redis
    :是一个开源的，内存数据库，它可以用作数据库，缓存和消息中间件，它支持多种类型的数据结构，如字符串，哈希，列表，集合，有序集合等
    
 redis-cli -h <homename> -p <port>   远程连接redis数据库
 
 redis中
    select 1  切换到db1,默认在db0
    keys *    查看所有redis键
    type “键”  查看键的数据类型
    flushdb    清空当前db
    flushall   清空所有db（慎用）
 列表
    lpush mylist a b c d
    lpush mylist a b c d   #插入数据
    lrange mylist 0 -1    #是从左往又插，所以后插入的在上面
    llen mylist            #返回mylist的长度
 
 set  #集合没有顺序，不重复
    sadd myset a b c d  #往set添加数据
    smembers myset       #获取myset中所有的元素
    scard myset         #scard 获取数量
 zset 有序集合
    zadd myzset 10 a 11 b 12 c
    zadd myzset 10 a 15 b 20 d
    zrange myzset 0 -1 withscores
    zrange myzset 0 -1
    zcard myset
    
    zadd向zset中添加一个值和分数，如果存在值，就更新分数，分数可以相同，
    zrange遍历myzset
    zcard返回zset中元素的数量
    
    