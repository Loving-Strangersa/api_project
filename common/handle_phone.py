# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 06:45
# @Author  : chron
# @FileName: handle_excel.py
# @Software: PyCharm
# @E-mail  : chron@foxmil.com

import random
from common.handle_db import HandleDB

"""
生产手机号模块，动态校验数据库，手机号未注册则反回
"""


def __get_phone():
    """
    1生成手机号
    :return:
    """

    phone_start = str(
        random.choice([133, 149, 153, 173, 177, 180, 181, 189, 199, 130, 131, 132, 145, 155, 156, 166, 171, 175,
                       176, 185, 186, 166, 134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 172, 178,
                       182, 183,
                       184, 187, 188, 198]))
    str_end = ''.join(random.sample('0123456789', 8))
    phone = phone_start + str_end
    return phone


def new_phone():
    db = HandleDB()
    while True:

        phone = __get_phone()
        # 校验数据库
        count = db.get_sql("select * from member where mobile_phone={}".format(phone))
        if count == 0:
            db.close()
            return phone


if __name__ == '__main__':
    print(new_phone())
