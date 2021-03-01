# -*- coding: utf-8 -*-
# @Time    : 2021年2月24日17:11:08
# @Author  : chron
# @FileName: test_play
# @Software: PyCharm
# @E-mail  : chron@foxmil.com
import json
import os
import unittest
import jsonpath

import ddt

from common.handle_EnvData import clear_data
from common.handle_excel import Excel
from common.handle_logger import logger
from common.handle_request import send_request
from common.project_path import DATA_DIR

"""
请求播放接口
"""

# 读取Excel文件数据
s = Excel(file_path=os.path.join(DATA_DIR, "api_cases.xlsx"), sheet_name="播放")
cases = s.read_all_datas()
s.coles_file()


# 遍历数据
# for i in cases:
#     print(cases)

@ddt.ddt()
class play_test(unittest.TestCase):

    # 设置前置
    @classmethod
    def tearDown(self) -> None:
        logger.info("===== 开始测试 =====")
        # 清理EnvData类中可能设置的属性
        clear_data()

    # 设置后置
    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("===== 结束测试 =====")

    @ddt.data(*cases)
    def test_play(self, case):
        logger.info("用例开始执行,用例{}:{}".format(case["id"], case["title"]))

        # 数据替换,替换Excel中request_data中contId 正则表达式 (?<=contId=).*?(?=&)
        # case = replace_mark_with_data(cases,"#contId#","661543514")

        # 发起请求
        response = send_request(method=case["method"], url=case["api_url"], data=case["request_data"])

        # 将Excel的json转为dict
        expected = json.loads(case["expected"])
        logger.info("期望结果为{}".format(expected))

        # 读取Excel中的jsonpath
        check_jsonpath_contid = case["check_jsonpath_contId"]
        check_jsonpath_contname = case["check_jsonpath_contName"]
        logger.info("本次jsonpath请求contId为:{}，contName为{}".format(check_jsonpath_contid, check_jsonpath_contname))

        # 对code contId contName 进行断言
        try:
            self.assertEqual(response.json()["code"], expected["code"])
            self.assertEqual(jsonpath.jsonpath(response.json(), check_jsonpath_contid),
                             jsonpath.jsonpath(expected, check_jsonpath_contid))
            self.assertEqual(jsonpath.jsonpath(response.json(), check_jsonpath_contname),
                             jsonpath.jsonpath(expected, check_jsonpath_contname))
        except AssertionError:
            logger.info("断言失败")
            raise
