import requests
from utils import excel_tools
from utils import pymysql_tools

testcases=excel_tools.read_excel("testcase\\接口测试用例模板.xlsx","Sheet1")
for testcase in testcases:
    url=testcase[1]
    method=testcase[5]
    datas=eval(testcase[7])
    casename=testcase[3]
    http_code=int(testcase[8])
    res_code=int(testcase[9])
    sql=testcase[10]

    r=requests.request(method=method,url=url,json=datas)

    try:
        assert r.status_code==http_code

        assert r.json().get("code")==res_code

        dbinfo={"host":"132.232.44.158","user":"vn","password":"Langjintest!@#4##","db":"lux"}
        re=pymysql_tools.query(dbinfo,sql)
        assert len(re)==1
        print("测试用例({})执行通过！".format(casename))
    except:
        print("测试用例({})执行失败！".format(casename))