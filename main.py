# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 21:04
# @Author  : chron
# @FileName: main.py
# @Software: PyCharm
# @E-mail  : chron@foxmil.com

import unittest
from common.project_path import REPORTS_DIR, TEST_CASES_DIR, TIME
from BeautifulReport import BeautifulReport

# 收集用例
s = unittest.TestLoader().discover(TEST_CASES_DIR)

# 生成报告
br = BeautifulReport(s)
br.report('test', TIME + '_report.html', REPORTS_DIR)
