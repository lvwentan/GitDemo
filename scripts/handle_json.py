import json


class HandleJson:
    """
    处理json格式数据的类
    """

    def __init__(self,filename=None):
        self.filename = filename

    def exchange_dict(self,json_str):
        return json.loads(json_str)

    def exchange_json(self,dict_data):
        return json.dumps(dict_data,ensure_ascii=False)

    def read_json_str(self):
        with open(self.filename,encoding="utf-8") as file:
            return  json.load(file)

    def  write_json(self,dict_data,filename=None):
        if filename is not None:
            with open(filename,mode="w",encoding="utf-8") as file:
                json.dump(dict_data,file,ensure_ascii=False,indent=2)
        else:
            with open(self.filename,mode="w",encoding="utf-8") as file:
                json.dump(dict_data,file,ensure_ascii=False,indent=2)



if __name__ == '__main__':
    dict_1 = {"name":None,"age":18}
    do_json = HandleJson("json.txt")
    do_json.write_json(dict_1)
    print(do_json.read_json_str())



