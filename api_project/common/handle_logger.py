# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 17:21
# @Author  : chron
# @FileName: my_logger.py
# @Software: PyCharm
# @E-mail  : chron@foxmil.com


import logging
import os
from common.handle_config import conf
from common.project_path import LOG_DIR, TIME


class MyLogger(logging.Logger):

    def __init__(self, file=None):
        """
        :param name: 日志文件名称
        :param level: 日志收集等级
        :param file:是否生成本地文件
        """
        # 初始化日志收集器名字、输出级别
        super().__init__(conf.get('log', 'name'), conf.get('log', 'level'))

        # 日志格式 日期、收集器名字、模块名、行数、输出日志级别、信息
        f = '%(asctime)s - %(name)s - [%(filename)s --> line:%(lineno)d] - %(levelname)s:%(message)s'
        formatter = logging.Formatter(f)

        # 控制台渠道
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        self.addHandler(console)

        if file:
            console2 = logging.FileHandler(file, encoding='utf8')
            console2.setFormatter(formatter)
            self.addHandler(console2)


# 是否需要写入文件
if conf.getboolean('log', 'file_ok'):
    file = os.path.join(LOG_DIR, TIME + conf.get('log', 'file_name'))
else:
    pass

logger = MyLogger(file)

if __name__ == '__main__':
    logger.info('hhh')
