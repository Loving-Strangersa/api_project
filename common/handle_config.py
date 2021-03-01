# -*- coding: utf-8 -*-
from configparser import ConfigParser
from common.project_path import CONFIG_DIR


class Config(ConfigParser):
    """
    读取config.ini数据
    """

    def __init__(self, file_path):
        super().__init__()
        self.read(file_path, encoding="utf8")


conf = Config(file_path=CONFIG_DIR)

if __name__ == "__main__":
    a = conf.get("log", "name")
    print(a)
