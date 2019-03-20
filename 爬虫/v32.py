from lxml import etree

html=etree.parse('./v30.html')
print(type(html))

rst = html.xpath('//book')
print(type(rst))
print(rst)

#xpath  的意识是 查找带有category属性值为sport的 book元素
rst=html.xpath('//book[@category="sport"]')
print(type(rst))
print(rst)

rst=html.xpath ('//book[@category="sport"]/year')
print(type(rst))
rst=rst[0]
print(type(rst))
print(rst.tag)
print(rst.text)