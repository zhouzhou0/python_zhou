from urllib import request


if __name__ == '__main__':
    url='http://www.renren.com/970089509/profile'
    headers={
        'Cookie': 'anonymid=jtb5ue8z-7phymi; depovince=FJ; _r01_=1; ick_login=bc882067-49ae-493d-af25-f2f70733febf; ick=36020828-6a3f-484f-bffb-5c55d9c6561b; t=c91841307c95771e229951c3f61637b89; societyguester=c91841307c95771e229951c3f61637b89; id=970089509; xnsid=7a9ff196; XNESSESSIONID=e9a31e520b3c; WebOnLineNotice_970089509=1; JSESSIONID=abcFeoq9ESBuaepchyfMw; ver=7.0; loginfrom=null; jebe_key=20f5815e-65db-40c2-8cc1-13b094e63203%7C35fcce1db1210aee8746eadf9d02231a%7C1552720904590%7C1%7C1552720903816; wp_fold=0; jebecookies=88a51af5-39d1-4931-b2ae-fa47d47ecd37|||||'
    }

    req=request.Request(url,headers=headers)
    rsp=request.urlopen(req)
    html = rsp.read().decode()
    with open('COOKIE.html','w') as f :
        f.write(html)