# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 19:20
# @Author  : chron
# @FileName: headle_read_yaml.py
# @Software: PyCharm
# @E-mail  : chron@foxmil.com

import yaml

with open('123.yaml', encoding='utf8') as f:
    data = yaml.load(f, yaml.FullLoader)
