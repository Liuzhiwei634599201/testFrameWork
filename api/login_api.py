
# 编写封装登录的类
import requests


class LoginApi:

    def login(self, mobile, password):
        # 定义一个jsonData变量，里面存放登录请求体的数据
        jsonData = {"mobile": mobile, "password": password}
        print(jsonData)
        # 使用requests模块发送登录接口请求
        result = requests.post(url="http://182.92.81.159/api/sys/login",
                               json=jsonData)
        return result

# 我们观察封装的登录函数
# 大家可以发现，我们的json格式的请求体数据json={"mobile": "13800000002", "password": "123456"}
# 是固定的写法，数据都写死了，不管是谁调用，都是返回登录用户138000000002的数据结果
# 那么如果我希望能够自定义登录的数据呢？

# main的作用是防止在导入这个文件时，运行代码
if __name__ == '__main__':
    login_api = LoginApi()
    login_api.login("3","4")
    print("这是在LoginApi中打印的提示信息")
