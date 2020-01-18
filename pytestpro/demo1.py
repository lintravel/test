'''
异常处理
增强代码健壮性
关键字：try except else finally
捕获错误信息：exception as e
'''
ldict={"year":2019,"month":9,"date":2}
try:
    "year3"in ldict
    1==2
except Exception as e:
    print(e)
else:
    print("今年是{}年".format(ldict["year"]))
finally:
    print("----------")