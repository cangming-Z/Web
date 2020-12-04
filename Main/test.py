# encoding:utf-8

import datetime
import os
import time

from past.builtins import raw_input
from selenium import webdriver
from Utility.main_path import get_object_path
from Utility.xls_r_w import read_xls


if __name__ == '__main__':
    try:
        option = webdriver.ChromeOptions()
        # option.add_argument('headless')
        browser = webdriver.Chrome(chrome_options=option)
        # browser = webdriver.Firefox()
        # 设置浏览器最大加载时间
        browser.set_page_load_timeout(8)
        object_path = get_object_path()

        xls_path = os.path.join(object_path, 'data', 'URLS.xls')

        while True:
            urls_xls = read_xls(xls_path, "Sheet1")
            for j in range(0, 3):
                for i in range(0, urls_xls.nrows):
                    url = urls_xls.cell(i, 0).value
                    try:
                        browser.get(url)
                        print("%s : %s" % (datetime.datetime.now(), urls_xls.cell(i, 1).value))
                    except Exception as TimeoutException:
                        print(TimeoutException)
                time.sleep(10)
            print("等待2分钟")
            time.sleep(60 * 2)
    except Exception as e:
        print(e)
        raw_input('Please press enter key to exit ...')
