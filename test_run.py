import unittest
import os
from datetime import datetime
from libs.HTMLTestRunnerNew import HTMLTestRunner
from scripts.handle_config import do_config
from scripts.constants import CASES_DIR,REPORTS_DIR,CONFIGS_DIR
from scripts.handle_user import generate_account_data


if not os.path.isfile(os.path.join(CONFIGS_DIR,"account.conf")):  # 如果三个账号不存在，则创建三个账号信息配置文件
    generate_account_data()



# report_path = "./reports/" + "report_" + f"{datetime.now():%Y%m%d%H%M%S}" + ".html"
report_path = REPORTS_DIR + "/"+ do_config.get_value("report","report_name")  + ".html"
with open(report_path,mode="wb") as one_file:
    one_suite = unittest.defaultTestLoader.discover(CASES_DIR)
    one_runner = HTMLTestRunner(stream=one_file,
                                verbosity = do_config.get_int("report","verbosity"),
                                title = do_config.get_value("report","title"),
                                description=do_config.get_value("report","description"),
                                tester= do_config.get_value("report","tester")    )
    one_runner.run(one_suite)





