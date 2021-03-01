import pymysql
from common.handle_config import conf

"""
1、连接数据库
2、获取一条数据
3、获取所有数据
4、关闭数据库连接
"""


class HandleDB(object):

    def __init__(self):
        self.connect = pymysql.connect(
            host=conf.get("mysql", "host"),
            port=conf.getint("mysql", "port"),
            user=conf.get("mysql", "user"),
            passwd=conf.get("mysql", "passwd"),
            database=conf.get("mysql", "database"),
            charset='utf8'
        )

        # 创建游标，返回字典数据
        self.cur = self.connect.cursor(pymysql.cursors.DictCursor)

    def get_one_data(self, sql):
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

    def get_all_data(self, sql):
        """
        :param sql:sql语句
        :return:获取所有数据 [{},{}...]
        """
        self.connect.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_sql(self, sql):
        """
        :param sql:
        :return:返回sql查询成功的记录数目
        """
        self.connect.commit()
        return self.cur.execute(sql)

    def updata(self, sql):
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



    # s = s.get_sql("select * from member limit 3 ")
    # print('获取sql查询结果条数:{}'.format(s))
    # s = s.get_one_data("select * from member ")
    # print("获取一条查询结果{}".format(s))
    # s = s.get_all_data("select * from member limit 3 ")
    # print('获取所有sql查询到的数据{}'.format(s))

    # s.get_one_data(select * from member)
