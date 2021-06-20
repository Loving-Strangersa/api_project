# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 21:06
# @Author  : chron
# @FileName: get_img_data.py
# @Software: PyCharm
# @E-mail  : chron@foxmil.com
# 导入easyocr
import easyocr
# 创建reader对象
reader = easyocr.Reader(['ch_sim','en'])
# 读取图像
result = reader.readtext('https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp7.itc.cn%2Fimages01%2F20210505%2F5cbfc67100854e0e808d397ff1b7c585.jpeg&refer=http%3A%2F%2Fp7.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1626716458&t=4f2992c451b476092f7f0dfc0bc03af6')
# 结果

for i in result:
    print(i[1])
