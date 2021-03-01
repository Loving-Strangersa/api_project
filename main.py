import unittest
from common.project_path import REPORTS_DIR, TEST_CASES_DIR
from BeautifulReport import BeautifulReport

# 收集用例
s = unittest.TestLoader().discover(TEST_CASES_DIR)

# 生成报告
br = BeautifulReport(s)
# br.report('test', TIME + '_report.html', REPORTS_DIR)
br.report(description="播放接口测试用例",filename="report",log_path=REPORTS_DIR)