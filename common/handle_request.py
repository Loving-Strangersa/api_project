# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 14:43
# @Author  : chron
# @FileName: handle_excel.py
# @Software: PyCharm
# @E-mail  : chron@foxmil.com
import json
import requests
from common.handle_logger import logger
from common.handle_config import conf
import allure

"""
封装发送接口模块
"""


def __hand_header(token):
    """
    处理请求头，加上项目中必带的请求头。如果有token则返回token
    :param token:
    :return:
    """

    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" \
         " AppleWebKit/537.36 (KHTML, like Gecko)" \
         " Chrome/88.0.4324.182 Safari/537.36"

    header = {'User-Agent': ua}
    if token:
        header['token'] = '{}'.format(token)
        return header
    return header


def __get_url(url):
    """
    拼接接口url的处理
    :param url:
    :return:
    """
    base_url = conf.get('server', 'base_url')
    # 判断读取Excel中api_url是否以/开头(防呆处理)
    if url.startswith:
        return base_url + url
    else:
        return base_url + '/' + url


def __get_json_data(data):
    """
    如果Excel中request_data是字典是则返回字典对象
    :param data:
    :return:
    """
    # 对判断进行捕获异常，如果不是字典格式运行json.loads,出现错误进行捕获异常,执行except
    try:
        if data is not None and isinstance(data, str):
            return json.loads(data)
    except BaseException:
        return data


def send_request(method, url, data=None, token=None):
    headers = __hand_header(token)
    url = __get_url(url)
    data = __get_json_data(data)

    # 配合proxies，开启fiddler抓包
    if method.upper() == 'GET':
        # verify 是否验证服务器的SSL证书
        # proxies 开启代理调试
        response = requests.get(
            url,
            params=data,
            headers=headers,
            verify=False,
            proxies=None)

    elif method.upper() == 'POST':
        response = requests.post(
            url,
            json=data,
            headers=headers,
            verify=False,
            proxies=None)

    logger.info('响应状态码为:{}'.format(response.status_code))
    # 不是json数据则报错,待优化
    logger.info('响应内容为:{}'.format(response.json()))

    debug = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}

    # allure
    allure.attach(str(url), "请求地址", allure.attachment_type.TEXT)
    allure.attach(f"{headers}", "请求头", allure.attachment_type.TEXT)
    allure.attach(f"{method}", "请求方法", allure.attachment_type.TEXT)
    allure.attach(str(data), "请求参数", allure.attachment_type.TEXT)
    allure.attach(str(response.status_code), "反回状态码",
                  allure.attachment_type.TEXT)
    allure.attach(response.text, "响应结果", allure.attachment_type.TEXT)

    return response


def send_session(method, url, data=None, token=None):
    headers = __hand_header(token)
    url = __get_url(url)
    data = __get_json_data(data)

    logger.info('请求头为:{}'.format(headers))
    logger.info('请求类型为:{}'.format(method))
    logger.info('请求url为{}'.format(url))
    logger.info('请求数据为:{}'.format(data))

    debug = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
    s = requests.Session()
    if method.upper() == 'GET':
        # verify 是否验证服务器的SSL证书
        # proxies 开启代理调试
        response = s.post(
            url,
            params=data,
            headers=headers,
            verify=False,
            proxies=None)
    elif method.upper() == 'POST':
        response = s.post(
            url,
            json=data,
            headers=headers,
            verify=False,
            proxies=None)
    else:
        logger.error("待增加请求方法")
        raise EOFError
    logger.info('响应状态码为:{}'.format(response.status_code))
    # 不是json数据则报错,待优化
    logger.info('响应内容为:{}'.format(response.json()))
    return response


if __name__ == '__main__':

    send_request(method="get", url="/playurl/v3/play/playurl",
                 data="contId=661543514&ott=true&rateType=&ott=false")
    send_session(method="get", url="/playurl/v3/play/playurl",
                 data="contId=661543514&ott=true&rateType=&ott=false")
