from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#实例化driver
driver=webdriver.Chrome()
driver.get("https://www.douban.com/")


time.sleep(3)
# driver:driver.find_element_by_xpath("//div[class='account-body-tabs']//li[@class='account-tab-account on']").click()

driver.find_element_by_id('username').send_keys('18950180000')
driver.find_element_by_id('password').send_keys('000000')
time.sleep(5)

driver.find_element_by_class_name('btn btn-account').click()


#获取cookie
cookies = {i['name']:i['value'] for i in driver.get_cookies()}
print(cookies)
time.sleep(3)
driver.quit()