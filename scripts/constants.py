"""
...........................
@time :2024/1/10 21:53
@Author :lwt
@Email :457477841@qq.com
@File :constants.py
@Software :PyCharm Community Edition
...........................

"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 动态获取根目录路径

CONFIGS_DIR = os.path.join(BASE_DIR,"configs") # 获取保存配置文件的目录的路径

CONFIGS_FILE_PATH = os.path.join(CONFIGS_DIR,"testcase.conf") # 获取保存配置文件的路径

DATAS_DIR =  os.path.join(BASE_DIR,"datas")  # 保存测试数据文件所属目录路径

# DATAS_FILE_PATH = os.path.join(CASES_DIR,"cases.xlsx")   测试用例文件名称从配置文件中读取  不要固定死

LOGS_DIR =  os.path.join(BASE_DIR,"logs") # 获取保存日志文件的目录的路径

# LOGS_FILE_PATH = os.path.join(LOGS_DIR ,"cases.log")   # 日志文件名称从配置文件读取 不要固定死

REPORTS_DIR = os.path.join(BASE_DIR,"reports")  # 获取保存测试报告的目录的路径

REPORTS_FILE_PATH = os.path.join(REPORTS_DIR ,"reports_")

CASES_DIR =  os.path.join(BASE_DIR,"cases") # 获取测试用例模块所属目录的路径

ACCOUNT_CONFIGS_PATH = os.path.join(CONFIGS_DIR,"account.conf")  # 存放借款人、投资人、管理员账户信息的配置文件

