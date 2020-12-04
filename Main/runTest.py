# -*- coding:utf-8 -*-
# _author_ = 'zdq'


import time
from selenium import webdriver

urlView = 'http://qtsntest.bytdev.com:8080/user/login'
urlControl = 'http://qtsntest.bytdev.com:8080/user/login'
userName = 'admin'
userPwd = '123456'

try:
    option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=option)
    # browser = webdriver.Firefox()
    # 设置浏览器最大加载时间
    driver.set_page_load_timeout(8)

    driver.get(urlControl)

    driver.find_element_by_id('userName').send_keys(userName)
    driver.find_element_by_id('password').send_keys(userPwd)
    a = driver.find_element_by_class_name('submit___Q43EO').click()

    time.sleep(1)
    search_window = driver.current_window_handle  # 此行代码用来定位当前页面

    driver.find_element_by_xpath('//*[@title="泉头"]/preceding-sibling::span[1]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@title="业务空间"]').click()
    time.sleep(0.5)
    aa = driver.find_element_by_css_selector(".ant-table-row.ant-table-row-level-0")
    # driver.find_element_by_css_selector(".ant-btn.ant-btn-primary").click()

    print('')

except Exception as e:
    print(e)
    print('Please press enter key to exit ...')
