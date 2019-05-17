# 전체 Select 하여 엑셀파일 쓰기
import pymysql
from openpyxl import load_workbook
#처리된 데이터를 json형식으로 리턴해주기위해 사용
import json
#python mysql 연결 드라이버
import pymysql
import numpy as np

class datainsert:
    def __init__(self, 서울, 부산, 대구, 인천, 광주, 대전,울산,경기도,강원도,충북,충남,전북,전남,경북,경남,제주):
        self.서울 = 서울
        self.부산 = 부산
        self.대구 = 대구
        self.인천 = 인천
        self.광주 = 광주
        self.대전 = 대전
        self.울산 = 울산
        self.경기도 = 경기도
        self.강원도 = 강원도
        self.충북 =충북
        self.충남 = 충남
        self.전북 = 전북
        self.전남 = 전남
        self.경북 = 경북
        self.경남 = 경남
        self.제주 = 제주

pas = 'Allday12345!'
#db연결을 담당할 함스
def getConnection():
    return pymysql.connect(host='localhost', port = 8808, user='root', password=pas,
                           db='webdb', charset='utf8')


englishgeo = ('서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기도', '강원도', '충북', '충남', '전북', '전남', '경북', '경남', '제주')

#등록된 내용을 가져옴
def getrule():
    # Connection 연결
    conn = getConnection()
    curs = conn.cursor()
    # SQL 처리
    sql = "select*from ifgeometry.ifgeometry_2016_2017"
    curs.execute(sql)
    #처리된 data 가져옴
    rows = curs.fetchall()
    indata = [[0 for ro in range(23)] for cols in range(16)]
    for i in range(0, 16):
        for j in range(0, 16):
            if englishgeo[j] == rows[i][0]:
                indata[j] = indata[i][1:]
    # Connection 닫기
    conn.close()
    #얻은 데이터를 보내준다.
    return rows

def rank_select(ifdata):
    #연결 담당 함수를 불러온다
    conn = getConnection()
    curs = conn.cursor()
    #SQL처리
    sql = "select*from today"
    curs.execute(sql)
    #데이터를 읽어옴
    rows = curs.fetchall()
    #2차원 배열을 만듬
    indata = [[0 for ro in range(5)]for cols in range(16)]
    for row in rows:
        ifn = 0
        for i in range(0,16):
            if rows[i][0] == englishgeo[i]:
                for j in range(1, 6):
                    if ifdata[i][ifn+2] < row[i][j] :
                        indata[i][j-1] = 4
                    elif ifdata[i][ifn+1] <= row[i][j] < ifdata[i][ifn+2]:
                        indata[i][j-1] = 3
                    elif ifdata[i][ifn] <= row[i][j] < ifdata[i][ifn+1]:
                        indata[i][j-1] = 2
                    else:
                        indata[i][j-1] = 1
                ifn = ifn + 3
    ALIdata = [0 for ro in range(16)]
    for i in range(0,16):
        ALIdata[i] = 0.5*indata[i][0]+0.6*indata[i][1]+1*indata[i][2]+\
                     2*indata[i][3]+0.4*indata[i][4]

    ALIrank = [0 for ro in range(16)]
    for i in range(0, 16):
        if ifdata[i][16] < ALIdata[i]:
            ALIrank[i] = 4
        elif ifdata[i][16] <= ALIdata[i] <ifdata[i][17]:
            ALIrank[i] = 3
        elif ifdata[i][17] <= ALIdata[i] <ifdata[i][18]:
            ALIrank[i] = 2
        else:
            ALIrank[i] = 1
    return ALIrank

def insertdanger(inser, check):
    conn = getConnection()
    try:
        curs = conn.cursor()
        #삽입 sql문
        sql1 = 'insert into danger_rank(서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기도, 강원도, 충북, 충남, 전북, 전남, 경북, 경남, 제주) ' \
                  'values(%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        #update(내용변경) sql문
        sql2 = 'UPDATE danger_rank set 서울= %s,부산= %s, 대구= %s, 인천= %s, 광주= %s, 대전= %s, 울산= %s,' \
                  '경기도= %s, 강원도= %s, 충북= %s, 전남= %s, 경북= %s, 경남= %s, 제주= %s'\
                  'WHERE id = %s'
        #비어있다면 넣어주고
        if check == 0:
            curs.execute(sql1,(1, inser.서울, inser.부산, inser.대구, inser.인천,inser.광주, inser.대전, inser.울산, inser.경기도,
                              inser.강원도, inser.충북, inser.충남, inser.전북, inser.전남, inser.경북, inser.경남, inser.제주))

        #들어가 있다면 업데이트로 내용을 변경해줍니다.
        else:
            curs.execute(sql2, (inser.서울, inser.부산, inser.대구, inser.인천,inser.광주, inser.대전, inser.울산, inser.경기도,
                               inser.강원도, inser.충북, inser.충남, inser.전북, inser.전남, inser.경북, inser.경남, inser.제주, 1))
        conn.commit()
    finally:
        conn.close()

def check_rank():
    #파이썬과 DB연결
    conn = pymysql.connect(host='localhost', port = 8808, user='root', password=pas, db='webdb', charset='utf8')
    num =0
    try:
        #curs에 conn.cursor()의 기능을 줌
        with conn.cursor() as curs:
            sql1 ='select*from danger_rank'
            row1 = curs.execute(sql1)
            if row1 != 0:
                num = 1
    finally:
        conn.close()

    return num

if __name__ == "__main__":
    che=check_rank()
    ifdat = getrule()
    #rd rankdata
    rd = rank_select(ifdat)
    indata = datainsert(rd[0], rd[1], rd[2],rd[3], rd[4], rd[5], rd[6], rd[7], rd[8],rd[9], rd[10], rd[11], rd[12],rd[13],rd[14],rd[15])
    insertdanger(indata, che)