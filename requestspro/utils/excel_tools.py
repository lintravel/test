# xlrd读取excel
import xlrd

def read_excel(excel_path,sheet_name):
    res=[]
    datas=xlrd.open_workbook(excel_path)
    table=datas.sheet_by_name(sheet_name)
    for row in range(1,table.nrows):
        d=table.row_values(row)
        res.append(d)
    return res

if __name__=="__main__":
    res=read_excel("testcase\\接口测试用例模板.xlsx","Sheet1")
    print(res)