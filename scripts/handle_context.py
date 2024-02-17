import re
from scripts.handle_mysql import HandleMysql
from scripts.handle_config import HandleConfig
from scripts.constants import ACCOUNT_CONFIGS_PATH

class HandleContext:

     not_exist_mobile = r"\${not_exist_mobilephone}"
     exist_mobile = r"\${exist_mobilephone}"
     borrower_mobile = r"\${borrower_mobile}"
     invest_mobile = r"\${invest_mobile}"
     invest_pwd = r"\${invest_pwd}"
     admin_mobile = r"\${admin_mobile}"
     admin_pwd = r"\${admin_pwd}"
     invest_pwd_pattern = r"\${invest_pwd}"
     borrower_memberId = r"\${borrower_memberId}"
     invest_memberId = r"\${invest_memberId}"
     admin_memberId = r"\${admin_memberId}"
     not_exist_memberId = r"\${not_exist_memberId}"
     loan_id = r"\${loan_Id}"
     not_exist_loan_id = r"\${not_exist_loanId}"

     @classmethod
     def not_exist_mobile_replace(cls,data):
         """
         未注册的手机号码参数化替换
         :param data: 原始字符串
         :return:
         """
         if re.search(cls.not_exist_mobile,data):
             do_mysql = HandleMysql()
             data = re.sub(cls.not_exist_mobile,do_mysql.create_not_register_mobile(),data)
             do_mysql.close()
         # else:
         #     print("模式字符串无法匹配原始字符串！")
         return data

     @classmethod
     def exist_mobile_replace(cls, data):
         """
         已注册的手机号码参数化替换
         :param data:
         :return:
         """
         if re.search(cls.exist_mobile, data):
             do_mysql = HandleMysql()
             data = re.sub(cls.exist_mobile, do_mysql.create_exist_mobile(), data)
             do_mysql.close()
         # else:
         #     print("模式字符串无法匹配原始字符串！")
         return data

     @classmethod
     def borrower_mobile_replace(cls, data):
         """
         借款人的手机号码参数化替换
         :param data:
         :return:
         """
         if re.search(cls.borrower_mobile, data):
             do_config = HandleConfig(ACCOUNT_CONFIGS_PATH)
             data = re.sub(cls.borrower_mobile, do_config.get_value("borrower_account", "mobilephone"), data)
         # else:
         #     print("模式字符串无法匹配原始字符串！")
         return data

     @classmethod
     def borrower_memberId_replace(cls, data):
         """
         借款人的memberId参数化替换
         :param data:
         :return:
         """
         if re.search(cls.borrower_memberId, data):
             do_config = HandleConfig(ACCOUNT_CONFIGS_PATH)
             data = re.sub(cls.borrower_memberId,str(do_config.get_value("borrower_account", "id")), data)
         return data

     @classmethod
     def invest_mobile_replace(cls, data):
         """
         投资人的手机号码参数化替换
         :param data:
         :return:
         """
         if re.search(cls.invest_mobile, data):
             do_config = HandleConfig(ACCOUNT_CONFIGS_PATH)
             data = re.sub(cls.invest_mobile, do_config.get_value("invest_account", "mobilephone"), data)
         # else:
         #     print("模式字符串无法匹配原始字符串！")
         return data

     @classmethod
     def invest_pwd_replace(cls, data):
         """
         投资人的密码参数化替换
         :param data:
         :return:
         """
         if re.search(cls.invest_pwd_pattern, data):
             do_config = HandleConfig(ACCOUNT_CONFIGS_PATH)
             data = re.sub(cls.invest_pwd_pattern, do_config.get_value("invest_account", "pwd"), data)
         # else:
         #     print("模式字符串无法匹配原始字符串！")
         return data

     @classmethod
     def invest_memberId_replace(cls, data):
         """
         投资人的memberId参数化替换
         :param data:
         :return:
         """
         if re.search(cls.invest_memberId, data):
             do_config = HandleConfig(ACCOUNT_CONFIGS_PATH)
             data = re.sub(cls.invest_memberId, str(do_config.get_value("invest_account", "id")), data)
         return data

     @classmethod
     def admin_mobile_replace(cls, data):
         """
         管理员的手机号码参数化替换
         :param data:
         :return:
         """
         if re.search(cls.admin_mobile, data):
             do_config = HandleConfig(ACCOUNT_CONFIGS_PATH)
             data = re.sub(cls.admin_mobile, do_config.get_value("admin_account", "mobilephone"), data)
         # else:
         #     print("模式字符串无法匹配原始字符串！")
         return data

     @classmethod
     def admin_pwd_replace(cls, data):
         """
         管理员的密码参数化替换
         :param data:
         :return:
         """
         if re.search(cls.admin_pwd, data):
             do_config = HandleConfig(ACCOUNT_CONFIGS_PATH)
             data = re.sub(cls.admin_pwd, do_config.get_value("admin_account", "pwd"), data)
         # else:
         #     print("模式字符串无法匹配原始字符串！")
         return data

     @classmethod
     def not_exist_memberId_replace(cls, data):
         """
         将不存在的memberId参数化替换
         :param data:
         :return:
         """
         if re.search(cls.not_exist_memberId, data):
             do_mysql = HandleMysql()
             data = re.sub(cls.not_exist_memberId,str(do_mysql.get_not_exist_memberID()),data)
             do_mysql.close()
         return data

     @classmethod
     def get_loan_id_replace(cls, data):
         """
         管理员加标的loanId参数化替换
         :param data:
         :return:
         """
         if re.search(cls.loan_id, data):
             # excel文件中参数化占坑的字符串用动态创建类属性的值进行替换，而动态创建类属性的值来源于上一个接口请求完成后
             #响应体某个字段得值或者数据库中数据表中某个字段得值，可以用res.json()[key]获取或者用sql获取
             data = re.sub(cls.loan_id,str(HandleContext.loanId), data)
             # data = re.sub(cls.loan_id,str(getattr(HandleContext,"loanId")), data)


         return data

     @classmethod
     def not_exist_loan_id_replace(cls, data):
         """
         管理员加标的loanId参数化替换
         :param data:
         :return:
         """
         if re.search(cls.not_exist_loan_id, data):
             do_mysql = HandleMysql()
             data = re.sub(cls.not_exist_loan_id,str(do_mysql.get_not_exist_loanID()),data)
             do_mysql.close()
         return data

     @classmethod
     def register_parametrize_replace(cls,data):
         """
         将注册接口下面所有的参数化进行替换
         :param data: 原始字符串
         :return:
         """
         data = cls.not_exist_mobile_replace(data)
         data = cls.exist_mobile_replace(data)

         return data

     @classmethod
     def login_parametrize_replace(cls, data):
         """
         将登录接口下面所有的参数化进行替换
         :param data: 原始字符串
         :return:
         """
         data = cls.not_exist_mobile_replace(data)
         data = cls.exist_mobile_replace(data)
         data = cls.borrower_mobile_replace(data)
         return data

     @classmethod
     def recharge_parametrize_replace(cls, data):
         """
         将充值接口下面所有的参数化进行替换
         :param data: 原始字符串
         :return:
         """
         data = cls.not_exist_mobile_replace(data)
         data = cls.invest_mobile_replace(data)
         data = cls.invest_pwd_replace(data)
         return data

     @classmethod
     def add_parametrize_replace(cls, data):
         """
         加标的接口下面所有的参数化进行替换
         :param data: 原始字符串
         :return:
         """
         data = cls.admin_mobile_replace(data)
         data = cls.admin_pwd_replace(data)
         data = cls.not_exist_memberId_replace(data)
         data = cls.borrower_memberId_replace(data)
         return data

     @classmethod
     def invest_parametrize_replace(cls, data):
         """
         投资的接口下面所有的参数化进行替换
         :param data: 原始字符串
         :return:
         """
         data = cls.admin_mobile_replace(data)
         data = cls.admin_pwd_replace(data)
         data = cls.not_exist_memberId_replace(data)
         data = cls.borrower_memberId_replace(data)
         data = cls.get_loan_id_replace(data)
         data = cls.invest_mobile_replace(data)
         data = cls.invest_pwd_replace(data)
         data = cls.not_exist_loan_id_replace(data)
         data = cls.invest_memberId_replace(data)
         return data

if __name__ == '__main__':



    one_str = '{"mobilephone":"${not_exist_mobilephone}","pwd":"1223456","regname":"test"}'
    two_str = '{"mobilephone":"${exist_mobilephone}","pwd":"1223456","regname":"test"}'
    three_str = '{"mobilephone":"${borrower_mobile}","pwd":"123456"}'
    four_str = '{"mobilephone":"${invest_mobile}","amount":"100000"}'
    five_str = '{"mobilephone":"${invest_mobile}","pwd":"${invest_pwd}"}'
    six_str = '{"memberId":"${not_exist_memberId}","title":"testapi","amount":50000,"loanRate":16,"loanTerm":30."loanDateType":0,"repaymemtWay":4,"biddingDays":5}'
    str_7 = '{"memberId":"${invest_mobile}","password":"${invest_pwd}","loanId":"${not_exist_loanId}","amount":10000}'



    print(HandleContext.register_parametrize_replace(one_str))
    print(HandleContext.register_parametrize_replace(two_str))
    print(HandleContext.login_parametrize_replace(three_str))
    print(HandleContext.recharge_parametrize_replace(four_str))
    print(HandleContext.add_parametrize_replace(two_str))
    print(HandleContext.recharge_parametrize_replace(five_str))
    print(HandleContext.not_exist_memberId_replace(six_str))
    print(HandleContext.not_exist_loan_id_replace(str_7))





