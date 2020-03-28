# 执行测试套件的入口，我们会把运行测试套件代码放在这里编写，并生成测试报告

# 导包
import unittest

import app
from scripts.test_ihrm_login import TestIHRMLogin
from HTMLTestRunner_PY3 import HTMLTestRunner
import time

# 创建测试套件
suite = unittest.TestSuite()
# 添加测试用例到测试套件
suite.addTest(unittest.makeSuite(TestIHRMLogin))
# 使用runner来运行测试套件
# 定义测试报告的文件名称
reportname = app.BASE_DIR + "/report/ihrm.html"

with open(reportname, 'wb') as f:
    # 初始化runner
    runner = HTMLTestRunner(f, verbosity=2, title="IHRM报告", description="这是一个比较美观的报告")
    # 利用runner来运行测试套件生成测试报告
    runner.run(suite)
