"""
...........................
@time :2024/1/8 12:34
@Author :lwt
@Email :457477841@qq.com
@File :handle_log.py
@Software :PyCharm Community Edition
...........................

"""
import logging
import os
from scripts.handle_config import do_config
from scripts.constants import LOGS_DIR

class HandleLog:

    def __init__(self):

        self.case_logger = logging.getLogger(do_config.get_value("log","logger_name"))  # 创建日志收集器对象

        self.case_logger.setLevel(do_config.get_value("log","logger_level")) # 定义日志收集器对象收集日志的等级

        console_handle = logging.StreamHandler()  # 定义日志输出渠道 一个是控制台，一个是文件
        file_handle = logging.FileHandler(os.path.join(LOGS_DIR,do_config.get_value("log","log_name")),encoding="utf-8")

        console_handle.setLevel(do_config.get_value("log","console_handle_level")) # 定义输出渠道输出日志的等级
        file_handle.setLevel(do_config.get_value("log","file_handle_level"))

        simple_formatter = logging.Formatter(do_config.get_value("log","simple_formatter"))
        verbose_formatter = logging.Formatter(do_config.get_value("log","verbose_formatter"))
        console_handle.setFormatter(simple_formatter) # 定义各个输出渠道输出日志的格式
        file_handle.setFormatter(verbose_formatter)

        self.case_logger.addHandler(console_handle)  # 将日志收集器对象与各个输出渠道对接
        self.case_logger.addHandler(file_handle)

    def get_logger(self):
        return self.case_logger

do_log = HandleLog().get_logger()
if __name__ == '__main__':
    do_log = HandleLog().get_logger()
    do_log.debug("这是一个debug等级的日志信息")
    do_log.info("这是一个info等级的日志")
    do_log.warning("这是一个warning等级的日志")
    do_log.error("这是一个error等级的日志")
    do_log.critical("这是一个critical等级的日志")


