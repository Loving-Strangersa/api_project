##  项目结构
- common 封装的公共类
- config 放置配置文件
- outputs 存放测试报告及日志
- report 存放测试报告
- test_cases 自己封装的测试用例类
- case_data 存放excel测试用例
- main.py 运行入口

## 编写测试用例步骤
- 1、设计测试用例
- 2、读取相关测试用例数据
    - handle_excel
- 3、定义一个测试类，继承unittest.TestCase
- 4、前置后置
    - 接入动态属性，接口关联
- 5、编写用例
    - def test_xxx():
    - 5.1 替换动态数据 - mark
    - 5.2 发送请求 
        - handle_request.send_request
    - 5.3 把期望结果，从字符串转换成字典对象
    - 5.4 断言期望的响应结果，及数据校验