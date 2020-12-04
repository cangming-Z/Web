# -*- coding:utf-8 -*-
# _author_ = 'zdq'


import configparser
from os import path
from Utility import main_path
from selenium import webdriver
from Utility.logger import Logger
from Utility.db_helper import Database


log = Logger(logger="test_main").get_log()


# 获取项目根目录
filepath = main_path.get_obj_path()
config = configparser.ConfigParser()
filePath = path.sep.join([filepath, 'config', 'db.ini'])
config.read(filePath, encoding='utf-8')

project = 'WebAutoTest'

host = config[project]["host"]
port = eval(config[project]["port"])
user = config[project]["user"]
passwd = config[project]["passwd"]
db = config[project]["db"]
charset = config[project]["charset"]

mysql_db = Database(host, port, user, passwd, db, charset)
mysql_db.get_mysql_con_cursor()

sql_process = 'select * from custom_process where project_id = %s and process_id = %s ' % (1, 1)

sql_process_detail = 'select type,elements_msg,value from custom_process_detail ' \
                     'where project_id = %s and process_id = %s order by `index`' \
                     % (1, 1)
process_detail = mysql_db.db_rw(sql_process_detail)

option = webdriver.ChromeOptions()
# option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)
# browser = webdriver.Firefox()
# 设置浏览器最大加载时间
driver.set_page_load_timeout(8)
err_msg = None

for detail in process_detail:
    try:
        return_message = ''
        if detail[0] == '1':
            return_message = driver.get(detail[2])
        elif detail[0] == '2':
            return_message = driver.find_element_by_id(detail[1]).send_keys(detail[2])
        elif detail[0] == '3':
            return_message = driver.find_element_by_class_name(detail[1]).click()
    except Exception as e:
        log.error(e)
        err_msg = "%s出错，错误信息：%s" % (detail[0], e)

if err_msg is None:
    log.info('测试通过')

