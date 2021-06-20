# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 21:04
# @Author  : chron
# @FileName: main.py
# @Software: PyCharm
# @E-mail  : chron@foxmil.com

import pytest
import os

if __name__ == '__main__':
    pytest.main(['-s','-v',
                 "--alluredir", "./allure-results",
                 # 运行失败的用例可以重新运行2次，第一次和第二次的间隔时间为5秒钟
                 "--reruns" ,"2" ,"--reruns-delay"," 5"
                 ])

os.system(r"allure generate --clean allure-results -o allure-report")
os.system(r"allure serve  allure-results")
