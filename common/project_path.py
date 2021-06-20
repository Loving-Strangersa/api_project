# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 09:13
# @Author  : chron
# @FileName: handle_excel.py
# @Software: PyCharm
# @E-mail  : chron@foxmil.com
import os
import time

# 项目路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 配置文件路径
CONFIG_DIR = os.path.join(BASE_DIR,"config.ini")

# Excel存放路径
DATA_DIR = os.path.join(BASE_DIR, 'case_data',"api_cases.xlsx")

# 测试报告输出路径
REPORTS_DIR = os.path.join(BASE_DIR, 'outputs\\report')

# 日志输出路径
LOG_DIR = os.path.join(BASE_DIR, 'outputs\\logs')

# 代码编写用例路径
TEST_CASES_DIR = os.path.join(BASE_DIR, 'test_cases')

# 生成时间戳
TIME = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

if __name__ == '__main__':
    print(BASE_DIR)
    print(CONFIG_DIR)
    print(LOG_DIR)
