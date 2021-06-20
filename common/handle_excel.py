# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 15:14
# @Author  : chron
# @FileName: handle_excel.py
# @Software: PyCharm
# @E-mail  : chron@foxmil.com

import json

import openpyxl
from common.project_path import DATA_DIR

"""测试用例数据的封装"""


class Excel(object):

    excel_path = DATA_DIR

    def __init__(self, sheet_name, file_path=excel_path) -> str:
        self.book = openpyxl.load_workbook(file_path)
        self.sheet = self.book[sheet_name]

    def read_tile(self):
        """
        :return: 获取表头信息
        """
        tile = []
        for i in list(self.sheet.rows)[0]:
            tile.append(i.value)
        return tile

    def read_all_data(self):
        """
        :return: 按行读取所有测试数据
        """
        all_data = []

        tile = self.read_tile()

        for item in list(self.sheet.rows)[1:]:
            values = []
            for i in item:
                values.append(i.value)
            response = dict(zip(tile, values))
            try:
                response['request_data'] = json.loads(response['request_data'])
            except json.JSONDecodeError:
                pass
            except TypeError:
                pass

            all_data.append(response)
        self.book.close()
        return all_data

    def read_one_data(self, row) -> int:
        """
        row:传入读取Excel中id的行数
        return:返回指定行数数据
        """
        return self.read_all_data()[row - 1]


if __name__ == '__main__':
    excle = Excel('播放')
    cases = excle.read_all_data()
    # print(cases[4]["request_data"]
    print(excle.read_one_data(5))
