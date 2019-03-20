'''
安装lxml
'''

from lxml import etree


'''
用lxml 来解析html代码
'''

text='''
<div>
    <ul>
        <li class='item0'> <a href='0.html'>firstitem</a></li>
        <li class='item1'> <a href='0.html'>firstitem</a></li>
        <li class='item2'> <a href='0.html'>firstitem</a></li>
        <li class='item3'> <a href='0.html'>firstitem</a></li>
        <li class='item4'> <a href='0.html'>firstitem</a></li>
        <li class='item5'> <a href='0.html'>firstitem</a></li>
       
    </ul>
</div>
'''
# 利用etree.HTML 把字符串解析成HTML文档
html=etree.HTML(text)
s=etree.tostring(html)
print(s)
