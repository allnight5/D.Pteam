# 전체 Select 하여 엑셀파일 쓰기
import pymysql
from openpyxl import load_workbook
pas = 'Allday12345!'

class Test:
    def __init__(self, num, name):
        self.num = num
        self.name = name
#전체 Select
def select_all():
    conn = pymysql.connect(host='localhost', port = 8808, user='root', password=pas, db='webdb', charset='utf8')
    try:
        with conn.cursor() as curs:
            sql = "select * from test"
            curs.execute(sql)
            rs = curs.fetchall()
            for row in rs:
                print(row)
    finally:
        conn.close()
#DB Delete All
def delete_all():
    conn = pymysql.connect(host='localhost', port = 8808, user='root', password=pas, db='webdb', charset='utf8')
    try:
        with conn.cursor() as curs:
            sql = 'delete from today'
            curs.execute(sql)
        conn.commit()
    finally:
        conn.close()

if __name__ == "__main__":
    delete_all()
