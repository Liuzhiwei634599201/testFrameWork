# 存放自定义的工具类的文件
# 安装pymysql，parameterized，requests

# 读取登录数据的函数
def read_login_data(filename):
    # 打开从外部传入的登录数据文件
    with open(filename, 'r', encoding='utf-8') as f:
        # 把数据加载成json格式
        # 如果需要使用json加载数据时，需要先导入json
        import json
        # 加载成json格式
        login_data_list = json.load(f)
        # 定义存储数据的空列表
        result_list = []
        # 遍历加载数据
        for login_data in login_data_list:
            print(login_data)
            # 取出login_data字典中的数据
            casename = login_data.get("casename")
            mobile = login_data.get("mobile")
            password = login_data.get("password")
            success = login_data.get("success")
            code = login_data.get("code")
            # 以元组的形式存放在result_list当中（这是parameterized工具的要求）
            result_list.append((casename, mobile, password, success, code))
    print(result_list)
    return result_list


if __name__ == '__main__':
    # 调试读取登录数据的函数
    read_login_data("./data/login.json")
