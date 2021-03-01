# -*- coding: utf-8 -*-
# @Time    : 2021/1/24 21:19
# @Author  : chron
# @FileName: handle_EnvData.py
# @Software: PyCharm
# @E-mail  : chron@foxmil.com

"""
可以设置动态属性(环境变量)，做接口流程
"""


class EnvData(object):
    pass


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
