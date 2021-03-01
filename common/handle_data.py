# -*- coding: utf-8 -*-
# @Time    : 2021/1/24 0:01
# @Author  : chron
# @FileName: handle_data.py
# @Software: PyCharm
# @E-mail  : chron@foxmil.com
"""
替换Excel数据
"""
import json
import re
from common.handle_config import conf
from common.handle_EnvData import EnvData


def replace_mark_with_data(case, mark, read_data):
    """
    :param case: excel读取出来的一条数据，是个字典
    :param mark:数据当中的占位符，#key#
    :param read_data:要替换mark生成的真实数据
    :return:
    """
    for key, value in case.items():
        # 如果值不是空和值是字符串类型
        if value is not None and isinstance(value, str):
            case[key] = value.replace(mark, read_data)
    return case


def replace_by_data(data):
    """
    将字符串中，匹配#(.*?)#部分，替换真实的数据
    真实数据从配置文件的data区域，和环境变量Envdata的类属性
    :param data:字符串
    :return:替换之后的字符串
    """
    res = re.findall("#(.*?)#", data)  # 如果没有找到返回空列表

    # 标识符对应值来自:1、环境变量 2、配置文件
    if res:
        for item in res:
            # 得到标识符对应值
            try:
                vaule = conf.get('data', item)
            except:
                try:
                    vaule = getattr(EnvData, item)
                except:
                    continue
            # 替换原字符
            data = data.replace("#{}#".format(item), vaule)
    return data


def replace_case(case):
    """
    对Excel中读取的一条用例数据，做全部替换，包括url，request_data,expected,check_sql
    :param case:
    :return:
    """
    # 把case字典从Excel中读出一条用例，json对象
    case_str = json.dumps(case)
    # 替换
    new_case = replace_by_data(case_str)
    # 把字符串转为字典
    case_dict = json.loads(new_case)
    return case_dict


if __name__ == '__main__':
    # a = replace_mark_with_data({'1':'#phone#'},'#phone#','1234')
    # print(a)

    print('123hhh'.replace('1', '呀'))
    print(replace_case({'msg':100}))
