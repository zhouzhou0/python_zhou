from urllib import request


if __name__ == '__main__':
    url='http://www.renren.com/970089509/profile'

    rsp = request.urlopen(url)


    html=rsp.read().decode()
    with open("rep.html","w") as f:
        f.write(html)