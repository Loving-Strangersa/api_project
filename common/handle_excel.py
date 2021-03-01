# -*- coding: utf-8 -*-
import json
import openpyxl
from common.project_path import DATA_DIR
from common.handle_logger import logger


class Excel(object):

    """读取测试用例数据,[{},{},{}...]"""

    excel_path = DATA_DIR

    def __init__(self, sheet_name, file_path=excel_path):
        self.boot = openpyxl.load_workbook(file_path)
        self.sheet = self.boot[sheet_name]

    def read_tile(self):
        """
        :return: 获取表头信息,list
        """
        title = []
        for i in list(self.sheet.rows)[0]:
            title.append(i.value)
        return title

    def read_all_data(self):
        """
        :return: [{}，{}，{}...]
        """
        all_data = []

        titles = self.read_tile()

        for item in list(self.sheet.rows)[1:]:
            # 获取每一行数据
            values = []
            for value in item:
                values.append(value.value)
            response = dict(zip(titles, values))
            try:
                response["response"] = json.loads(response["request_data"])
            except json.JSONDecodeError:
                logger.info(
                    "{}工作表，第{}条用例请求非json类型".format(
                        self.sheet.title,
                        response["id"]))
            all_data.append(response)

        return all_data

    def coles_file(self):
        """关闭excel释放内存"""
        self.boot.close()


if __name__ == '__main__':
    print(Excel("播放").read_all_data())
