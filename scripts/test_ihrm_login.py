# 导包
import unittest
import requests
from parameterized import parameterized

import app
from utils import read_login_data

# 创建测试类
class TestIHRMLogin(unittest.TestCase):

    # 进行初始化
    def setUp(self):
        # 导入封装的login_api类
        from api.login_api import LoginApi
        # 实例化LoginApi类
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 定位登录数据文件的路径
    # "."代表当前python文件的目录，但是当前的目录是在script目录中，
    # 那么请求script目录中有没有data目录和data目录下的login.json文件
    # ".."代表当前目录的父级目录
    filename = app.BASE_DIR + "/data/login.json"
    # 使用parameterized进行参数化
    @parameterized.expand(read_login_data(filename))
    # 创建测试函数
    def test01_login(self,casename, mobile, password, success, code):
        # 使用封装的api接口完成登录操作
        result = self.login_api.login(mobile,password)
        # 打印登录结果
        print("登录的结果为：", result.json())
        # 对登录结果进行断言
        self.assertEqual(success, result.json().get("success"))
        self.assertEqual(code, result.json().get("code"))
