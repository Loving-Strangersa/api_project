# -*- coding: utf-8 -*-
import json
import re
from common.handle_config import conf
from common.handle_EnvData import EnvData

"""替换Excel数据"""


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
    res = re.findall("#(.*?)#", data)
    if res:
        for item in res:
            try:
                vaule = conf.get('data', item)
            except BaseException:
                try:
                    vaule = getattr(EnvData, item)
                except BaseException:
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
    case_str = json.dumps(case)
    new_case = replace_by_data(case_str)
    case_dict = json.loads(new_case)
    return case_dict


