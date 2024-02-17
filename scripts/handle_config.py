"""
...........................
@time :2024/1/7 19:09
@Author :lwt
@Email :457477841@qq.com
@File :handle_config.py
@Software :PyCharm Community Edition
...........................

"""

from configparser import ConfigParser
from scripts.constants import CONFIGS_FILE_PATH

class HandleConfig:

    def __init__(self,filename):
        self.filename = filename
        self.config = ConfigParser()
        self.config.read(self.filename,encoding="utf-8")

    def get_value(self,section,option):
        return self.config.get(section,option)

    def get_int(self,section,option):
        return self.config.getint(section,option)

    def get_float(self,section,option):
        return self.config.getfloat(section,option)

    def get_boolean(self,section,option):
        return self.config.getboolean(section,option)

    def get_eval_data(self,section,option):
        return eval(self.config.get(section,option))

    @staticmethod
    def write_config(filename,datas):
        """
        将数据写入到一个新的配置文件当中
        :param filename: 配置文件名
        :param data: 配置数据为一个嵌套字典的字典
        :return:
        """
        if isinstance(datas,dict):# 先判断外层是否为字典数据
          for value in datas.values():  # 再判断里层的value是否为字典数据
              if not isinstance(value,dict):
                  return "数据不合法！datas必须是嵌套字典的字典数据"
          config = ConfigParser()
          for key in datas:
              config[key] = datas[key] # 将配置解析器对象当成空字典，添加键值对
          with open(filename,mode="w",encoding="utf-8") as one_file:
              config.write(one_file) # 将配置解析器对象中数据写入到文件当中
              return f"数据{datas}写入到配置文件{filename}中成功！"
        else:
            return "数据不合法！datas必须是嵌套字典的字典数据"




do_config = HandleConfig(CONFIGS_FILE_PATH)


if __name__ == '__main__':
    filename = r"C:\Users\78228\Desktop\automated_testing_api\configs\testcase.conf"
    do_config = HandleConfig(filename)
    print(do_config.get_value("msg","success_result"))
    print(do_config.get_int("excel","actual_column"))
    datas = {
           "excel":{
               "success_column":6,
               "failure_column":7
           },
           "msg":{
               "success_result":"pass",
               "failure_result":"fail"
           }
    }
    print(do_config.write_config("测试.ini",datas))








