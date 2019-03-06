#权重
goods = [{'name':'good1','price':200,'sales':100,'starts':5,'comments':400},
         {'name':'good2','price':366,'sales':80,'starts':5,'comments':520},
         {'name':'good3','price':130,'sales':100,'starts':5,'comments':50},
         {'name':'good4','price':300,'sales':66,'starts':5,'comments':120},
         {'name':'good5','price':899,'sales':77,'starts':5, 'comments':2000}]
#print(goods)
#用sorted排序
#权重100 价格权重是40% ，销量权重是17%,星级权重是13%,评论权重是30%
def my_sorted(arg):
    price = arg['price']
    sales = arg['sales']
    starts = arg['starts']
    comments = arg['comments']
    date = price*0.4+sales*0.17+starts*0.13+comments*0.3
    return date
print(sorted(goods,key = my_sorted))

#用lambda
r = sorted(goods,key=lambda x :x['price']*0.4+ x['sales']*0.17+x['starts']*0.13+x['comments']*0.3,reverse=True )
print(r)