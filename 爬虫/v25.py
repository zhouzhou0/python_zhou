'''
search
'''

import re

s=r'\d+'
pattern = re.compile(s)
m =pattern.search("noe1two2three3four467")

print(m.group())


#参数表明搜查的起始范围
m =pattern.search("noe1two2three3four467",10,50)
print(m.group())
