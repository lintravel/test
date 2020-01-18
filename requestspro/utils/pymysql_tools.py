import pymysql
def query(dbinfo,sql):
    db = pymysql.connect(**dbinfo)
    cursor = db.cursor()
    cursor.execute(sql)
    res=cursor.fetchall()
    db.close()
    return res
