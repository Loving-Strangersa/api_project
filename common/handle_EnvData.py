# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 11:26
# @Author  : chron
# @FileName: handle_excel.py
# @Software: PyCharm
# @E-mail  : chron@foxmil.com
"""关联接口"""


class EnvData(object):
    data = 1


def clear_data():
    # 清理Envdata中设置的属性
    values = dict(EnvData.__dict__.items())
    for key, value in values.items():
        if key.startswith("__"):
            pass
        else:
            delattr(EnvData, key)


setattr(EnvData, "name", "haha")
if __name__ == '__main__':
    print(EnvData.name)
