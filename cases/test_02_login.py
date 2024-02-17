import unittest
import os
from libs.ddt import ddt,data
from scripts.handle_excel import HandleExcel
from scripts.handle_config import do_config
from scripts.handle_log import do_log
from scripts.constants import DATAS_DIR
from scripts.handle_context import HandleContext
from scripts.handle_request import HandleRequest

do_excel = HandleExcel(os.path.join(DATAS_DIR,do_config.get_value("file name","cases_file_name")),"login")
cases = do_excel.get_cases()


@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.do_request = HandleRequest()
        do_log.info("{:=^40s}".format("开始执行用例"))

    def tearDown(self):
        self.do_request.close()
        do_log.info("{:=^40s}".format("执行用例结束"))

    @data(*cases)
    def test_login(self,one_case):
        try:
            new_url = do_config.get_value("api","prefix") + one_case["url"]
            new_data = HandleContext.login_parametrize_replace(one_case["data"])
            method = one_case["method"]
            expected = one_case["expected"]
            actual  = self.do_request.to_request(url=new_url,method=method,data=new_data).text
            msg = one_case["title"] + "失败"
            success_result = do_config.get_value("msg","success_result")
            failure_result = do_config.get_value("msg","failure_result")
            self.assertEqual(expected,actual,msg=msg)
            do_log.info(f"{one_case['title']},期望结果：{expected}，实际结果：{actual}，测试结果【{success_result}】")
            do_excel.write_result(one_case["case_id"]+1,actual=actual,result=success_result)
        except AssertionError as e:
            do_log.error(f"{one_case['title']},期望结果：{expected}，实际结果：{actual}，测试结果【{failure_result}】")
            do_excel.write_result(one_case["case_id"]+1,actual=actual,result=failure_result)
            raise e


if __name__ == '__main__':
    unittest.main()
    pass