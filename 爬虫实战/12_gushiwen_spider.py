import requests
import re

def parse_page(url):
    headers={'User-Agent':"Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"}
    # proxies =     {'https': '111.197.238.158:9999'}


    response=requests.get(url,headers=headers)
    # print(response.text)
    text=response.text
    titles=re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)#DOTALL表示.匹配所有的字符 /n
    # print(titles)
    dynasties=re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    # print(dynasty)
    authors=re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    # print(poem)
    contens=re.findall(r'<div class="contson" .*?>(.*?)</div>',text,re.DOTALL)
    shi=[]
    for content in contens:
        # print(content)
        s=re.sub(r'<.*?>',"",content,re.DOTALL)
        # print(s.strip())
        shi.append(s)
    #a[1],2] b[3,4] c=zip(a,b) >>> c=[{1:3},{2:4}]
    #value=[1,2,3]  a,b,c=value  >>>a=1 b=2 c=3
    poems=[]
    for value in zip(titles,dynasties,authors,contens):
        title,dynasty,author,content=value
        poem={
            'title':title,
            'dynasty':dynasty,
            'content':content,

        }
        poems.append(poem)
    for poem in poems:
        print(poem)
        print('*'*60)


def main():
    for i in range(1,2):
        url='https://www.gushiwen.org/default_{0}.aspx'.format(i)

        # url='https://www.gushiwen.org/default_1.aspx'
        parse_page(url)



if __name__ == '__main__':
    main()