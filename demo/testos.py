# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 4:12
# @Author  : chron
# @FileName: testos.py
# @Software: PyCharm
# @E-mail  : chron@foxmil.com

import os

x = 0
s = os.listdir(r"D:\api\common")
for i in s:
    py = i.split(".")
    if py[-1] == "py":
        x +=1
        print("序号",x,"---",i,"是python文件")