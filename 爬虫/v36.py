'''

通过webdriver操作百度进行查找

'''
from selenium import webdriver
import time

#通过keys模拟键盘
from selenium.webdriver.common.keys import Keys
#操作那个浏览器就对那个浏览器建一个实例
#自动按照环境变量查找相依的浏览器
driver=webdriver.PhantomJS()

#如果浏览器没有在相应的环境变量中，需要指定浏览器的位置

driver.get("http://www.baidu.com")

print("Title:{}".format(driver.title))