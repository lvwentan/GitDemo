import unittest
import os
import json
from libs.ddt import ddt,data
from scripts.handle_excel import HandleExcel
from scripts.handle_config import do_config
from scripts.handle_log import do_log
from scripts.constants import DATAS_DIR
from scripts.handle_context import HandleContext
from scripts.handle_request import HandleRequest
from scripts.handle_mysql import HandleMysql

do_excel = HandleExcel(os.path.join(DATAS_DIR,do_config.get_value("file name","cases_file_name")),"recharge")
cases = do_excel.get_cases()


@ddt
class TestRecharge(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.do_request = HandleRequest()
        cls.do_mysql = HandleMysql()
        do_log.info("{:=^40s}".format("开始执行用例"))

    @classmethod
    def tearDownClass(cls):
        cls.do_request.close()
        cls.do_mysql.close()
        do_log.info("{:=^40s}".format("执行用例结束"))

    @data(*cases)
    def test_recharge(self,one_case):

        if one_case["check_sql"]:
            check_sql = HandleContext.recharge_parametrize_replace(one_case["check_sql"])
            amount_before = round(float(self.do_mysql.get_value(check_sql)["LeaveAmount"]),2)

        try:
            recharge_url = do_config.get_value("api","prefix") + one_case["url"]
            recharge_data = HandleContext.recharge_parametrize_replace(one_case["data"])
            expected = one_case["expected"]
            actual  = self.do_request.to_request(url=recharge_url,method=one_case["method"],data=recharge_data).text
            msg = one_case["title"] + "失败"
            success_result = do_config.get_value("msg","success_result")
            failure_result = do_config.get_value("msg","failure_result")
            self.assertIn(expected,actual,msg=msg)

            if  one_case["check_sql"]:
                amount_after =round(self.do_mysql.get_value(check_sql)["LeaveAmount"],2)
                current_amount = round((json.loads(one_case["data"],encoding="utf-8"))["amount"],2)
                self.assertEqual(amount_before+current_amount,amount_after,msg="数据库中充值金额不正确")

            do_log.info(f"{one_case['title']},期望结果：{expected}，实际结果：{actual}，测试结果【{success_result}】")
            do_excel.write_result(one_case["case_id"]+1,actual=actual,result=success_result)
        except AssertionError as e:
            do_log.error(f"{one_case['title']},期望结果：{expected}，实际结果：{actual}，测试结果【{failure_result}】")
            do_excel.write_result(one_case["case_id"]+1,actual=actual,result=failure_result)
            raise e


if __name__ == '__main__':
    unittest.main()
    pass