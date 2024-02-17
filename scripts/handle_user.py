"""
...........................
@time :2024/1/10 22:41
@Author :lwt
@Email :457477841@qq.com
@File :register_caaount.py
@Software :PyCharm Community Edition
...........................

"""
import os
from scripts.handle_config import do_config
from scripts.handle_request import HandleRequest
from scripts.handle_mysql import HandleMysql
from scripts.constants import CONFIGS_DIR


def create_new_user(regname,pwd="123456"):
    """
    注册一个新的手机号码，并返回嵌套字典的字典数据
    :param regname:
    :param pwd:
    :return:
    """

    do_request = HandleRequest()
    do_mysql = HandleMysql()
    register_url = do_config.get_value("api","prefix") + "/member/register"
    sql = 'SELECT Id FROM member WHERE MobilePhone=%s'

    while True:
        mobilephone = do_mysql.create_not_register_mobile()
        data = {"mobilephone":mobilephone,"pwd":pwd,"regname":regname}
        do_request.to_request(register_url,data=data)

        result = do_mysql.get_value(sql,args=(mobilephone,))
        if result:
            user_id = result["Id"]
            break

    user_dict = {
        regname:{
            "id":user_id,
            "mobilephone":mobilephone,
            "pwd":pwd,
            "regname":regname,
                }
                }
    do_mysql.close()
    do_request.close()
    return user_dict

def generate_account_data():
    """
    将嵌套字典的字典数据写入到新的配置文件中
    :return:
    """
    users_datas_dict = {}
    users_datas_dict.update(create_new_user("borrower_account"))
    users_datas_dict.update(create_new_user("invest_account"))
    users_datas_dict.update(create_new_user("admin_account"))
    do_config.write_config(os.path.join(CONFIGS_DIR,"account.conf"),users_datas_dict)

if __name__ == '__main__':

    generate_account_data()




