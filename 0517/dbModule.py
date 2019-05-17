# file name : dbModule.py
# pwd : /WebDp/app/dbModule.py
import pymysql
pas = 'Allday12345!'

class Database():
    #DB를 연결해주는 기본 함수
    def __init__(self):
        self.db = pymysql.connect(host='localhost', port = 8808, user='root', password=pas,
                                  db='webdb', charset='utf8')
        #DIct형태로 데이터를 가져옴( {'columns 이름': 데이터 내용}의 형태로 가져옴)
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    #exceute함수(sql에 명령어 전송함수)
    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    #익스큐트후 읽어오는 한줄만 함수
    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        #DB에서 row를 한줄씩 읽어옴
        row = self.cursor.fetchone()
        #row를 돌려보내줌
        return row

    #전체적으로 읽어오는 함수
    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        #DB table 전체내용을 읽어옴
        row = self.cursor.fetchall()
        #row를 돌려보내줌
        return row

    #내용을 확정시킴
    def commit(self):
        self.db.commit()
