# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 17:57
# @Author  : chron
# @FileName: handle_excel.py
# @Software: PyCharm
# @E-mail  : chron@foxmil.com
import pymysql
from common.handle_config import conf


class HandleDB(object):

    def __init__(self):
        self.connect = pymysql.connect(
            host=conf.get("mysql", "host"),
            port=conf.getint("mysql", "port"),
            user=conf.get("mysql", "user"),
            passwd=conf.get("mysql", "password"),
            database=conf.get("mysql", "database"),
            charset='utf8'
        )

        # 创建游标，返回字典数据
        self.cur = self.connect.cursor(pymysql.cursors.DictCursor)

    def get_one_data(self, sql) -> str:
        """
        :param sql:sql语句
        :return:获取一条数据
        """
        # 更新事务保持数据的一致性
        self.connect.commit()
        # 执行sql
        sql = str(sql)
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_all_data(self, sql) -> str:
        """
        :param sql:sql语句
        :return:获取所有数据 [{},{}...]
        """
        self.connect.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_sql(self, sql) -> str:
        """
        :param sql:
        :return:返回sql查询成功的记录数目
        """
        self.connect.commit()
        return self.cur.execute(sql)

    def updata(self, sql) -> str:
        """
        对数据库进行增删改
        :param sql:
        :return:
        """
        self.connect.commit()
        self.cur.execute(sql)
        self.connect.commit()

    def close(self):
        self.cur.close()
        self.connect.close()


if __name__ == '__main__':
    s = HandleDB()
    a = s.get_all_data("select name from help_category;")
    print(a)

