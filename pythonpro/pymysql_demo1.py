import pymysql
def query():
    dbinfo={
        "host":"127.0.0.1",
        "user":"root",
        "password":"123456",
        "db":"db_morning"
    }
    db = pymysql.connect(**dbinfo)
    cursor = db.cursor()
    sql="select * from tb_goods"
    cursor.execute(sql)
    res=cursor.fetchall()
    print(res)
    db.close()
if __name__=="__main__":
    query()