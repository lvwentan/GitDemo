import requests
import json
from scripts.handle_log import do_log

class HandleRequest:

    def __init__(self):
       self.one_session = requests.Session()

    def to_request(self,url,method="post",data=None,headers=None,is_json=False):
       """
       定义发送请求的实例方法
       :param url:
       :param method:
       :param data:
       :param headers:
       :param is_json:
       :return:
       """
       method = method.lower()
       if isinstance(data,str):
           try:
               data = json.loads(data,encoding="utf-8")
           except Exception as e:
               data = eval(data)
               do_log.info(f"该数据为字典类型的字符串！异常信息为：{e}")
       if method == "get":
           res = self.one_session.get(url=url,params=data,headers=headers)
       elif method == "post":
           if is_json:
               res = self.one_session.post(url=url,json=data,headers=headers)
           else:
               res = self.one_session.post(url=url,data=data,headers=headers)
       elif method == "delete":
           res = self.one_session.delete(url=url,headers=headers)
       else:
           res = None
           print(f"不支持该{method}方式的请求！")
       return res

    def close(self):
        self.one_session.close()


if __name__ == '__main__':

    do_request = HandleRequest()

    login_url = "http://192.168.0.129:9999/futureloan/mvc/api/member/login"
    recharge_url = "http://192.168.0.129:9999/futureloan/mvc/api/member/recharge"
    add_url = 'http://192.168.0.129:9999/futureloan/mvc/api/loan/add'
    ketangpai_url = 'https://openapiv5.ketangpai.com//UserApi/login'
    test_url = 'https://www.baidu.com/'

    login_params = {"mobilephone":"13839746018","pwd":"123456"}
    recharge_params = {"mobilephone":"17756829367","amount":100000}
    add_params = {"memberId":547,"title":"testapi","amount":50000,"loanRate":"aa","loanTerm":30,"loanDateType":0,"repaymemtWay":4,"biddingDays":5}
    ketangpai_params = {
  "email": "457477841@qq.com",
  "password": "220104wen",
  "remember": "0",
  "code": "",
  "mobile": "",
  "type": "login",
  "reqtimestamp": 1705209534609
}


    headers = {"User-Agent" : "Mozila/5.0"}

    headers1= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chro'
                      'me/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10548.400'
}

    res1 = do_request.to_request(login_url,"post",login_params)
    res2 = do_request.to_request(recharge_url,"post",recharge_params)
    res3 = do_request.to_request(add_url,"post",add_params)
    # res4 = do_request.to_request(ketangpai_url,"post",ketangpai_params)
    res5 = do_request.to_request(test_url,'get')

    print(res1.json())
    print(res2.json())
    print(res3.json())
    # print(res4.json())
    print(res5.status_code)

    pass








