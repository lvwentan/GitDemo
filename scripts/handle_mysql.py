"""
...........................
@time :2024/1/10 14:39
@Author :lwt
@Email :457477841@qq.com
@File :handle_mysql.py
@Software :PyCharm Community Edition
...........................

"""
import pymysql
import random
from scripts.handle_config import do_config

class HandleMysql:

    def __init__(self):
        self.conn = pymysql.connect(host=do_config.get_value("mysql","host"),
                                    user=do_config.get_value("mysql","user"),
                                    password=do_config.get_value("mysql","password"),
                                    db = do_config.get_value("mysql","db"),
                                    port=do_config.get_int("mysql","port"),
                                    charset="utf8",
                                    cursorclass=pymysql.cursors.DictCursor)

        self.cursor = self.conn.cursor()

    def get_value(self,sql,args=None,is_more=False):
        self.cursor.execute(sql,args=args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()


    def create_not_register_mobile(self):
        """
        创建数据库中未注册的手机号码
        :return:
        """
        while True:
            one_list = ["137","138","139","177","155"]
            start_mobile = random.choice(one_list)
            end_mobile = ''.join(random.sample("0123456789",8))
            mobile = start_mobile + end_mobile
            sql = "SELECT * FROM member WHERE MobilePhone=%s"
            # sql = "SELECT * FROM member WHERE MobilePhone={}"  两种占坑方式 %s、{}
            # if self.run(sql.format(mobile)) is None:
            if self.get_value(sql,args=(mobile,)) is None:
                return mobile

    def create_exist_mobile(self):
        """
        创建数据库中已经存在的手机号码
        :return:
        """
        sql = "SELECT MobilePhone FROM member limit 1;"
        return  self.get_value(sql)["MobilePhone"]

    def get_not_exist_memberID(self):
        """
        获取数据库中不存在的memberId
        :return:
        """
        sql = "SELECT Id from member ORDER BY Id DESC LIMIT 1"
        memberId = self.get_value(sql)["Id"] + 1
        return memberId


    def get_not_exist_loanID(self):
        """
        获取数据库中不存在的loanId
        :return:
        """
        sql = "SELECT Id from loan ORDER BY Id DESC LIMIT 1"
        loanId = self.get_value(sql)["Id"] + 1
        return loanId

if __name__ == '__main__':

        do_mysql = HandleMysql()
        # mobilephone = "15330417908"
        # sql1 = 'SELECT * FROM member WHERE MobilePhone=%s'
        #  print(do_mysql.get_value(sql1,args=(mobilephone,)))
        #
        # sql2 = 'SELECT * FROM member limit 10'
        # print(do_mysql.get_value(sql2,is_more=True))

        print(do_mysql.create_not_register_mobile())
        print(do_mysql.create_exist_mobile())
        print(do_mysql.get_not_exist_memberID())
        print(do_mysql.get_not_exist_loanID())
