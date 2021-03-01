# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 15:14
# @Author  : chron
# @FileName: handle_excel.py
# @Software: PyCharm
# @E-mail  : chron@foxmil.com
# import json
# import os
import openpyxl
from common.project_path import DATA_DIR

'''
测试用例数据的封装
'''


class Excel(object):
    # 测试用例路径
    excel_path = DATA_DIR + r'\api_cases.xlsx'

    def __init__(self, sheet_name, file_path=excel_path):
        self.wb = openpyxl.load_workbook(file_path)
        self.sh = self.wb[sheet_name]

    def read_tile(self):
        """
        :return: 获取表头信息
        """
        tiles = []
        for tile in list(self.sh.rows)[0]:
            tiles.append(tile.value)
        return tiles

    def read_all_datas(self):
        """
        :return: 按行读取所有测试数据
        """
        all_datas = []  # 所有测试用例数据

        tiles = self.read_tile()

        for item in list(self.sh.rows)[1:]:  # 遍历用例行
            # 获取数据
            values = []
            for vle in item:  # 获取每一行的值
                values.append(vle.value)
            res = dict(zip(tiles, values))  # 每一行的数据打包成字典
            # 将请求数据从json字符串转换为字典对象
            # res['request_data'] = json.loads(res['request_data'])
            all_datas.append(res)
        return all_datas

    def coles_file(self):
        self.wb.close()


if __name__ == '__main__':
    excle = Excel('注册')
    cases = excle.read_all_datas()
    excle.coles_file()
    for case in cases:
        print(type(case))
        print(case)
