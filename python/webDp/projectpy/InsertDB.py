#설치 selenium, bs4
#pip install selenium
#pip install bs4
#를하던가 아래 내용을 친후에 bs4위나 selenium 커서를 둔후 alt+enter를 친후 import install을 클릭해도 된다.
import requests
#mysql과 파이썬을 연결하기 위해 사용하는 모듈
import pymysql
import random
#크롤링을 하기 위해서 사용하는 모듈
from urllib.request import urlopen
import bs4
from projectpy import exloader
#schedule은 시간을 설정을 못하여 시간을 설정할수 있는 pscheduler를 사용
#스케줄을 하기위해서 사용하는 모듈들
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError
import time
from datetime import datetime as times
 #조건의 16개 지역을 넣은 변수를 생성
서울 =  "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EC%A0%84%EB%82%A0%EC%94%A8&tqi=UL67ZwpVuE4ssblfMvwssssssKs-309815" #서울
부산="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B6%80%EC%82%B0%EB%82%A0%EC%94%A8&oquery=%EC%B6%A9%EC%B2%AD%EB%B6%81%EB%8F%84%EB%82%A0%EC%94%A8&tqi=UL6TJlp0J14ssbSxqZGssssstMG-249779"
대구 = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EB%B6%80%EC%82%B0%EB%82%A0%EC%94%A8&tqi=UL6jkdp0Jy0ssnbROZVssssstuK-040172"
인천="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9D%B8%EC%B2%9C%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=UL6jCsp0JXVssuKJK3Kssssst2h-423706"
광주="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B4%91%EC%A3%BC%EB%82%A0%EC%94%A8&oquery=%EC%9D%B8%EC%B2%9C%EB%82%A0%EC%94%A8&tqi=UL6jqsp0J14ssbrnDBossssss24-513381"
대전="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EC%A0%84%EB%82%A0%EC%94%A8&oquery=%EA%B4%91%EC%A3%BC%EB%82%A0%EC%94%A8&tqi=UL6jYsp0YiRsscmCbAGsssssslG-211199"
울산="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9A%B8%EC%82%B0%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EC%A0%84%EB%82%A0%EC%94%A8&tqi=UL6j1wp0JXossku5UR0sssssttw-133849"
경기도="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B2%BD%EA%B8%B0%EB%8F%84%EB%82%A0%EC%94%A8&oquery=%EC%9A%B8%EC%82%B0%EB%82%A0%EC%94%A8&tqi=UL6jIlp0J1ZssvzPiYlssssssV8-486772"
강원도="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B0%95%EC%9B%90%EB%8F%84%EB%82%A0%EC%94%A8&oquery=%EA%B2%BD%EA%B8%B0%EB%8F%84%EB%82%A0%EC%94%A8&tqi=UL6j%2Fdp0JXVssuLSMx8ssssstjV-450410"
충청북도 = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%B6%A9%EC%B2%AD%EB%B6%81%EB%8F%84%EB%82%A0%EC%94%A8&oquery=%EA%B0%95%EC%9B%90%EB%8F%84%EB%82%A0%EC%94%A8&tqi=UL6kasp0Yihssaa%2B0sGssssss8G-362632"
충청남도="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%B6%A9%EC%B2%AD%EB%82%A8%EB%8F%84%EB%82%A0%EC%94%A8&oquery=%EC%B6%A9%EC%B2%AD%EB%B6%81%EB%8F%84%EB%82%A0%EC%94%A8&tqi=UL6k6lp0JXVssuNln7Zssssss9w-439538"
전라북도="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%A0%84%EB%9D%BC%EB%B6%81%EB%8F%84%EB%82%A0%EC%94%A8&oquery=%EC%B6%A9%EC%B2%AD%EB%82%A8%EB%8F%84%EB%82%A0%EC%94%A8&tqi=UL6kMdp0JXVssu6ktslssssstwR-491634"
전라남도="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%A0%84%EB%9D%BC%EB%82%A8%EB%8F%84%EB%82%A0%EC%94%A8&oquery=%EC%A0%84%EB%9D%BC%EB%B6%81%EB%8F%84%EB%82%A0%EC%94%A8&tqi=UL6kRdp0JXossj8uJdRssssstC4-354428"
경상북도="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B2%BD%EC%83%81%EB%B6%81%EB%8F%84%EB%82%A0%EC%94%A8&oquery=%EC%A0%84%EB%9D%BC%EB%82%A8%EB%8F%84%EB%82%A0%EC%94%A8&tqi=UL6kUwp0J1sssMnaLKosssssst0-251498"
경상남도="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B2%BD%EC%83%81%EB%82%A8%EB%8F%84%EB%82%A0%EC%94%A8&oquery=%EA%B2%BD%EC%83%81%EB%B6%81%EB%8F%84%EB%82%A0%EC%94%A8&tqi=UL6kNsp0YiRssclhtSlssssst4Z-478748"
제주도="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%A0%9C%EC%A3%BC%EB%8F%84%EB%82%A0%EC%94%A8&oquery=%EA%B2%BD%EC%83%81%EB%82%A8%EB%8F%84%EB%82%A0%EC%94%A8&tqi=UL6klwp0J1ZssvVIIzVssssssAZ-484652"

#오늘 날짜를 입력
day = times.today().strftime("%Y-%m-%d")

#url주소들을 입력
geome2 = (서울, 부산, 대구, 인천,광주, 대전,울산,경기도,강원도,충청북도,충청남도,전라북도,전라남도,경상북도,경상남도,제주도)
#지역이름을 입력
geome = ('서울', '부산', '대구', '인천','광주', '대전','울산','수원','속초','청주','천안','전주','순천','구미','진주','제주')
#gedata라는 2차원 배열을 생성
gedata = [[0 for rows in range(5)]for cols in range(16)]

#습도랑 기압을 크롤링 해오는 함수
def humiPha(geome, gedata):
    url =  "http://www.weather.go.kr/weather/observation/currentweather.jsp"
    html = urlopen(url)
    #bs4의 beautifulsoup으로 url주소의 html 안에 내용을 읽습니다.
    bs_obj = bs4.BeautifulSoup(html.read(), "html.parser")
    #해당 URL에 오늘의날씨 표 div의 고유의 클래스명을 찾고 find함수로 찾음
    zxzxz=bs_obj.find("div",class_="width2")
    #하나씩 고유의 아이디나 클래스명을 찾아들어가 오늘의 습도와 기압 수치가 나오는 수치까지 찾아내는과정
    weweee=zxzxz.find("div",id="content_weather")
    rtt=weweee.find("table",class_="table_develop3")
    #오늘의 날씨 수치 테이블
    dsfd=rtt.find("tbody")
    #오늘의 날씨 타이틀 테이블
    dsfd2=rtt.find("thead")
    tytyt=dsfd2.find("tr",id="table_header2")#타이틀 테이블의 두번째 행
    tytyt1=dsfd2.find("tr",id="table_header1")#타이틀 테이블의 첫번째 행
    tyty2=tytyt.findAll("th")#타이틀 테이블의 두번째행의 모든 열
    tyt2=tytyt1.findAll("th")#타이틀 테이블의 첫번째행의 모든 열
    rtr=tyty2[8]  #습도타이틀명
    #지점 rtr2=tyt2[0]
    rtr3=tyt2[5]  #기압타이틀명
    print("지역","  ",rtr.text,"  ",rtr3.text)
    tyty=dsfd.findAll("tr")
    #습도 % 기압
    for tr in tyty:
        ewe2=tr.findAll("td")
        #습도
        wefe2= ewe2[9]
        #기압
        wefe3 = ewe2[12]
        #지역
        wefe = ewe2[0]
        j=0
        for i in geome:
            #지역 이름 비교해서 맞다면 넣는다.
            if i == wefe.text:
                gedata[j][2] = float(wefe2.text)#습도
                gedata[j][3] = float(wefe3.text)#기압
            j = j+1;
    print("습도 기압 완료")

#최저기온, 최고기온, 오존을 크롤링하며 일교차를 구하는 함수
def temperoz(geo):
    for i in range(0, 16):
        html = urlopen(geo[i])
        bs_obj = bs4.BeautifulSoup(html.read(), "html.parser")
        # 오존수치 오늘
        main2 = bs_obj.find("div", class_="detail_box")
        sfee = main2.find("dl")
        ewef = sfee.findAll("dd")
        ozan = ewef[2].find("span")
        # 온도 오늘
        zxzxz = bs_obj.find("div", class_="main_info")
        dsfd = zxzxz.find("div")
        ede = dsfd.find("ul")
        eiui = ede.findAll("li")
        erer = eiui[1].find("span")
        min2=erer.find("span",class_="min")
        Min=min2.text
        #온도를 가져올때 ˚(도)를 빼고 변수에 넣는다.
        Min2=Min.replace("˚","")
        max2=erer.find("span", class_="max")
        Max=max2.text
        #온도를 가져올때 ˚(도)를 빼고 변수에 넣는다.
        Max2=Max.replace("˚","")
        #일교차를 구해줍니다.
        Rtem = float(Max2)-float(Min2)
        #일교차를 구하기위하여 계산해줌
        gedata[i][0] = float(Rtem)
        gedata[i][1] = float(Min2)
        #ppb를 빼고 오존 데이터만 가져오게 합니다.
        if ozan.text[0:4] == 'null':
            gedata[i][4] = float('0')
        else:
            gedata[i][4] = float(ozan.text[:5])
    print("최저 최고 오존 완료")


#new를 가져오는 주소와 가져오기
newsurl =  "https://search.naver.com/search.naver?query=%EC%B2%9C%EC%8B%9D&where=news&ie=utf8&sm=nws_hty"
newshtml = urlopen(newsurl)
bs_obj = bs4.BeautifulSoup(newshtml.read(), "html.parser")

#뉴스를 가져오도록 하는 함수
def newsdata():
    dni = bs_obj.find("div", class_="news mynews section _prs_nws")
    rrt = dni.find("ul", class_="type01")
    edata = rrt.findAll("li")
    #뉴스 내용을 담을 리스트
    list = []
    for li in edata:
        eii = li.findAll("dl")
        for dt in eii:
            #내용을 찾는다.
            searchlt = dt.find("a")
            link = searchlt['href'] #링크
            title = searchlt['title'] #타이틀
            list.append([day, link, title]) #순서대로 오늘날짜, 링크, 타이틀(제목) 순이다.
    print("뉴스 완료")
    return list #완성된 list를 돌려보내준다.

#mysql 데이터베이스 비번 입력

pas = 'Allday12345!'
def insert_news(newsinsert, check):
    #파이썬과 DB연결
    conn = pymysql.connect(host='localhost', port = 8808, user='root', password=pas, db='webdb', charset='utf8')
    try:
        #curs에 conn.cursor()의 기능을 줌
        with conn.cursor() as curs:
            #sql이라는 변수에 아래 데이터
            #today라는 DB에 입력하겠다.
            #today_news에 갯수가 몇개인지 세는 sql문
            sql = "select MAX(id) from today_news"

            #into today_news(id, today, href, today) today_news라는 테이블의 id와 today등 이런 칼럼 들에
            #values(%s, %s,%s, %s) 이 DB에 데이터를 4개를 넣어주겠다.
            sql1 = 'insert into today_news(id, today, href, title, temp) values(%s, %s, %s, %s, %s)'

            #오름차순으로 읽어오는 sql문
            sql2 = 'select*from today_news order by today desc'
            curs.execute("set names utf8")
            curs.execute(sql)
            number1 = curs.fetchall()
            number1 = list(number1[0])
            number2 = number1[0]+1
            curs.execute(sql2)
            check_news = curs.fetchall()
            in_date_count = 0  # 데이터를 몇개 넣을지 카운트 한다.
            check_num = [0 for rows in range(10)]  #넣을 번호째를 담을 배열을 생성
            for i in range(0, 10):
                over =0
                #10개 이상이라면 id의 갯수만큼 하는데
                if number2 > 10:
                    #20개가 가장 최대로 20개 이상이라면 상위 20개만 중복 검사 후 추가합니다.
                    if number2 >= 20:
                        for k in range(0, 20):
                            if check_news[k][3] == newsinsert[i][2]:
                                over = over+1  #같은게 있다면 카운트 한다.

                            if over >0 :
                                break; #같은게 있다면 종료시킨다.

                    #10개 이상이면서 20개 미만 이라면 id의 값만큼 중복 검사를 합니다.
                    else :
                        for k in range(0, number2):
                            if check_news[k][3] == newsinsert[i][2]:
                                over = over+1  #같은게 있다면 카운트 한다.

                            if over >0 :
                                break; #같은게 있다면 종료시킨다.
                else :
                    #10개 를 넣기 때문에 범위는 0부터 10개를 넣는다..
                    for k in range(0, 10):
                        if check_news[k][3] == newsinsert[i][2]:
                            over = over+1  #같은게 있다면 카운트 한다.

                        if over >0 :
                            break; #같은게 있다면 종료시킨다.

                #같은게 없다면 추가를 위해서 1을 추가하고 배열에 번호를 넣어줍니다.
                if over == 0 :
                    #배열에 넣을 id 번호를 추가
                    check_num[in_date_count] = i
                    #
                    in_date_count = in_date_count + 1

            j=0
            if in_date_count> 0:
                #최종 값부터 입력을 시작하며 중복이 아닌 갯수만큼만 추가합니다.
                for i in range(number2, number2+in_date_count):
                   #if check == 0:
                   #실행한다 차례대로 id, today(오늘날짜), 링크, 타이틀, 는 %s에 들어갈 내용들이다.
                   curs.execute(sql1, (i, newsinsert[check_num[j]][0], newsinsert[check_num[j]][1], newsinsert[check_num[j]][2], 0))
                   j= j+1

        #삽입 내용을 확정시킨다.
        #안하면 저장이 안된다.
        conn.commit()
    finally:
        #연결을 종료한다.
        conn.close()

#mysql에 입력하는 함수
def insert_db(dinsert, geome, check):

    #파이썬과 DB연결
    conn = pymysql.connect(host='localhost', port = 8808, user='root', password=pas, db='webdb', charset='utf8')

    try:
        #curs에 conn.cursor()의 기능을 줌
        with conn.cursor() as curs:
            #sql이라는 변수에 아래 데이터 today라는 DB에 입력하겠다.
            #into  today(geo, Maxtem, Mintem, Humi,Hpa,Ozone) today라는 테이블의 geo와 Maxtem등 이런 칼럼 들에
            #values(%s, %s,%s, %s,%s, %s) 이 DB에 문자열 6개를 넣어주겠다.
            sql1 = 'insert into today(geonum, geo, Maxtem, Mintem, Humi,Hpa,Ozone) values(%s, %s, %s,%s, %s, %s, %s)'
            sql2 = 'UPDATE today set Maxtem= %s, Mintem= %s, Humi= %s, Hpa= %s, Ozone= %s'\
                   'WHERE geonum = %s'

            for i in range(0, 16):
                if check == 0:
                #실행한다 insert.geo, dinsert.Maxtem, dinsert.Mintem, dinsert.Humi, dinsert.Hpa, dinsert.Ozone는 %s에 들어갈 내용들이다.
                    curs.execute(sql1, (i, geome[i], dinsert[i][0], dinsert[i][1], dinsert[i][2], dinsert[i][3], dinsert[i][4]))

                else :
                    #UPdate해서 내용을 바꿔준다.
                    curs.execute(sql2, (dinsert[i][0], dinsert[i][1], dinsert[i][2], dinsert[i][3], dinsert[i][4], i))

        #삽입 내용을 확정시킨다.
        #안하면 저장이 안된다.
        conn.commit()
    finally:
        #연결을 종료한다.
        conn.close()


#table이 비었는지 안비었는지 확인하는 함수
def check_db(day):
    #파이썬과 DB연결
    conn = pymysql.connect(host='localhost', port = 8808, user='root', password=pas, db='webdb', charset='utf8')
    num =0
    try:
        #curs에 conn.cursor()의 기능을 줌
        with conn.cursor() as curs:
            sql1 ='select*from %s'%day
            row1 = curs.execute(sql1)
            #비어있지않다면 1을 넣어준다.
            if row1 != 0:
                num = 1
    finally:
        conn.close()
    #비어있다면 0을 안비어있다면 1을 넘겨준다.
    return num

def random_news():
    conn = pymysql.connect(host='localhost', port = 8808, user='root', password=pas, db='webdb', charset='utf8')
    try:
        #curs에 conn.cursor()의 기능을 줌
        with conn.cursor() as curs:
            #테이블안에 모든 내용 삭제 sql문
            delsql = 'delete from view_news'
            curs.execute(delsql)
            #sql이라는 변수에 아래 데이터
            #today_news에 갯수가 몇개인지 세는 sql문
            sql = "select MAX(id) from today_news"
            #into today_news(today, href, today) today_news라는 테이블의 today와 href 등 이런 칼럼 들에
            #values(%s, %s,%s) 이 DB에 데이터를 3개를 넣어주겠다.
            sql1 = 'insert into view_news(id, today, href, title) values(%s,%s, %s, %s)'
            #sql에서 뉴스가 들어있는 테이블을 읽어오는 쿼리문(질의문) 입니다.
            sql2 = 'select*from today_news order by id asc'
            curs.execute("set names utf8")
            curs.execute(sql)
            #전부 읽어들입니다.
            Maxnum = curs.fetchall()
            Maxnum = list(Maxnum[0])
            #최대 값에서 1을 더해줘야 최대값이 포함되기에 더하기 1을 해줍니다.
            Maxnumber = Maxnum[0]+1
            #이제 데이터를 0부터 순서대로 전부 읽어서 news_date변수에 넣습니다.
            curs.execute(sql2)
            news_date = curs.fetchall()
            #카운트를 위한 변수 j를 만듭니다.
            j=0
            rand = [0 for rows in range(10)]
            for i in range(0, 10):
                rand[i]= random.choice(range(Maxnumber))
                for j in range(0, 10):
                    if rand[i] == rand[j]:
                        i = i - 1
            #10개의 뉴스를 넣을것이니 범위는 0부터 10까지 합니다.
            for i in range(0, 10):
                #랜덤 함수를 사용하며 범위에는 위에서 구한 최대값으로 설정합니다.
                #랜덤에 따른 뉴스들의 위치를 테이블에 넣어줍니다.
                #실행한다 차례대로 today(오늘날짜), 링크, 타이틀, 들을 %s에 들어갈 내용들이다.
                curs.execute(sql1, (news_date[rand[i]][0], news_date[rand[i]][1], news_date[rand[i]][2], news_date[rand[i]][3]))
                j= j+1

        #삽입 내용을 확정시킨다.
        #안하면 저장이 안된다.
        conn.commit()
        print("Best 입력완료")
    finally:
        #연결을 종료한다.
        conn.close()



def allstart():
    #기압과 온도 함수
    humiPha(geome, gedata)
    #오존과 습도함수
    temperoz(geome2)
    ch = check_db('today')
    #insert함수를 통해서 DB에 자료를 넣어줍니다.
    insert_db(gedata,geome, ch)
    data = newsdata()
    #뉴스 내용 점검 함수
    ch = check_db('today_news')
    #insert함수를 통해서 DB에 자료를 넣어줍니다.
    insert_news(data, ch)
    #위험지수구하는 py파일을 불러와서 실행
    exloader.all()


#실행하는 함수
if __name__ == "__main__":

    #apscheduler에서 BackgroundScheduler를 sched에 담는다.
    sched = BackgroundScheduler()
    #BackgroundScheduler()를 실행히시킨다.
    sched.start()
    #스케줄러 사용 id를 Today1이라 하여 실행
    #매시간 5분에 allstart라는 함수를 작동하게 합니다.
    #함수부분에 함수 이름은 넣을수 있으나 allstat(1, 2) 형식은 불가합니다.
    #입력하여 하고 싶은경우 함수를 따로 만들어서 내용을 사용할 함수에서 실행하고 사용 함수를 입력해주세요.
    sched.add_job(allstart, 'cron', minute="5", second='00', id="Today1")

    #테이블에 한주간 보여줄 뉴스를 넣어줍니다.
    #day_of_week는 0이 mon부터 시작하여 tue,wed로 6까지 작성란입니다
    #hour은 시간으로 0~24, minute은 분으로 0~59, second는 초로 0~59가 가능합니다.
    sched.add_job(random_news, 'cron', day_of_week="3", hour="10", minute="6", second='00', id="News")

    #멈추지 않고 계속 돌아가기 위해서 필요한 반복문 입니다.
    #sleep안에 sleep한계 안의 숫자를 입력하시면 돌아가시는데 문제는 없습니다.
    count = 0
    while True:
        print(times.today().strftime("%H:%M:%S"))
        time.sleep(5)

    #실행이 waring이 뜨는데 저것은 utf8의 utf8MB3 버전이 UTF8MB4로 바뀌니 주의하라는 경고문입니다.
    #utf8이란 유니코드의 속해져 있는 인코딩 방법중 하나입니다.
    #유니코드란 컴퓨터에서 다양한 문자를 모아놓고 순서대로 번호를 붙여서 컴퓨터에서 그 글자를 인식하여(코드포인트)
    #보여줄수 있도록 해주는 코드입니다.
    #코드 포인트란 유니코드에서 그 문자나 숫자 그림을 찾기위해서 붙여둔 번호입니다.