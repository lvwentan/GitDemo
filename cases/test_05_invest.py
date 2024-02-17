import unittest
import os

from libs.ddt import ddt,data
from scripts.handle_excel import HandleExcel
from scripts.handle_config import do_config
from scripts.handle_log import do_log
from scripts.constants import DATAS_DIR
from scripts.handle_context import HandleContext
from scripts.handle_request import HandleRequest
from scripts.handle_mysql import HandleMysql


do_excel = HandleExcel(os.path.join(DATAS_DIR,do_config.get_value("file name","cases_file_name")),"invest")
cases = do_excel.get_cases()


@ddt
class TestInvest(unittest.TestCase):

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
    def test_invest(self,one_case):
        url = do_config.get_value("api", "prefix") + one_case["url"]
        data = HandleContext.invest_parametrize_replace(one_case["data"])
        try:
            expected = one_case["expected"]
            actual  = self.do_request.to_request(url=url,method=one_case["method"],data=data).text
            if "加标成功" in actual:
                if one_case["check_sql"]:
                    sql = HandleContext.invest_parametrize_replace(one_case["check_sql"])
                    loanId = self.do_mysql.get_value(sql)["Id"]
                    HandleContext.loanId =loanId
                    # setattr(HandleContext,"loanId",loanId) # 两种方式均可
                    # 管理员加标成功后，通过sql语句操作数据库的对象获取刚刚加标的id值传递给动态创建的类属性，作为下个接口请求请求参数化替换的真实值
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