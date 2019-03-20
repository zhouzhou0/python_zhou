'''
i:cat  输入的单词

ts:1552705291999
   1552706026.2169974  *1000

salt:15527131775339  时间戳
     1552706026.2169974  *10000

        r = "" + (new Date).getTime(),
        i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,

sign:n.md5("fanyideskweb"+e+i+"1L5ja}w$puC.v_Kz3@yYn"

sign:d33d65f852fa6044f1078b0d96729c81    sign:n.md5("fanyideskweb"+e+i+"1L5ja}w$puC.v_Kz3@yYn"
ts:  1552656892001



i:job
from:AUTO
to:AUTO
smartresult:dict
client:fanyideskweb
salt:15527052919992
sign:33ea6e9908c9e692dbee36b245bd60db
ts:1552705291999
bv:b8d026a0af60f03f29c5b4cc06dd949d
doctype:json
version:2.1
keyfrom:fanyi.web
action:FY_BY_REALTlME
typoResult:false
'''

from urllib import request,parse,error
import time
import random
import hashlib
import json


def get_md5(value):
    md5=hashlib.md5()
    md5.update(bytes(value,encoding='utf-8'))
    sign=md5.hexdigest()
    return sign



def yd_fanyi(key):
    base_url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    s=int(int(time.time()*10000)+random.randint(1,10))
    t = int((time.time()*1000))
    gg="fanyideskweb"+key+str(s)+"1L5ja}w$puC.v_Kz3@yYn"



    data ={
        'i':key,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'fanyideskweb',
        'salt':s,
        'sign':get_md5(gg),
        'ts':t,
        'bv':'b8d026a0af60f03f29c5b4cc06dd949d',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTlME',
        'typoResult':'false'

    }
    data=parse.urlencode(data)
    headers={
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Content-Length': len(data),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'YOUDAO_MOBILE_ACCESS_TYPE=1; OUTFOX_SEARCH_USER_ID=93458734@10.16',
        'Host': 'fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'

    }
    data=data.encode()
    req=request.Request(base_url,data=bytes(data),headers=headers)
    response=request.urlopen(req)

    content=response.read().decode()
    print(content)


if __name__ == '__main__':
    key = input("请输入您要翻译的内容")
    yd_fanyi(key)