# -*- coding: utf-8 -*-

"""
正则匹配数据
"""


import re


class Matching(object):

    def get_all_data(self, data, startswith, endswith):
        """
        data:匹配的数据
        startswith:开头的关键字
        endswith:结尾的关键字
        return:返回中间匹配的数据
        """
        re_data = f'(?<={startswith}).*?(?={endswith})'

        return re.findall( re_data,data)


data= """

data= '<link rel="stylesheet" href="plugins/screen-diff/styles.css">'
data= '<link rel="stylesheet" href="plugins/screen-diff/styles.css">'
data= '<link rel="stylesheet" href="plugins/screen-diff/styles.css">'


"""

print(Matching().get_all_data(data,"link","="))