#설치 selenium, bs4
#pip install selenium
#pip install bs4
#를하던가 아래 내용을 친후에 bs4위나 selenium 커서를 둔후 alt+enter를 친후 import install을 클릭해도 된다.
import requests
import pymysql
from urllib.request import urlopen
import bs4
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

geome2 = (서울, 부산, 대구, 인천,광주, 대전,울산,경기도,강원도,충청북도,충청남도,전라북도,전라남도,경상북도,경상남도,제주도)
geome = ('서울', '부산', '대구', '인천','광주', '대전','울산','수원','속초','청주','천안','전주','순천','구미','진주','제주')
#gedata라는 2차원 배열을 생성
gedata = [[0 for rows in range(5)]for cols in range(16)]
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
            if i == wefe.text:
                gedata[j][2] = float(wefe2.text)
                gedata[j][3] = float(wefe3.text)
                print(gedata[j][2], gedata[j][3])
            j = j+1;


def temperoz(geome2):
    for i in range(0, 16):
        html = urlopen(geome2[i])
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
        Min2=Min.replace("˚","")
        max2=erer.find("span", class_="max")
        Max=max2.text
        Max2=Max.replace("˚","")
        Rtem = float(Max2)-float(Min2)
        #일교차를 구하기위하여 계산해줌
        gedata[i][0] = float(Max2)
        gedata[i][1] = float(Min2)
        gedata[i][4] = float(ozan.text[:5])
        print("최고기온",Max2,"최저기온",Min2,"오존",ozan.text, "일교차", Rtem)

humiPha(geome, gedata)
temperoz(geome2)

#mysql 데이터베이스 비번 입력
pas = 'Allday12345!'
#기본적 토대가 되는 __init__작성
class Todayal:
    def __init__(self, geo, Maxtem, Mintem, Humi, Hpa, Ozone):
        self.geo = geo
        self.Maxtem = Maxtem
        self.Mintem = Mintem
        self.Humi = Humi
        self.Hpa = Hpa
        self.Ozone = Ozone


def insert_db(dinsert):
    #파이썬과 DB연결
    conn = pymysql.connect(host='localhost', port = 8808, user='root', password=pas, db='webdb', charset='utf8')
    try:
        #curs에 conn.cursor()의 기능을 줌
        with conn.cursor() as curs:
             #sql이라는 변수에 아래 데이터
             #today라는 DB에 입력하겠다.
             #into  today(geo, Maxtem, Mintem, Humi,Hpa,Ozone) today라는 테이블의 geo와 Maxtem등 이런 칼럼 들에
             #values(%s, %s,%s, %s,%s, %s) 이 DB에 문자열 6개를 넣어주겠다.
            sql = 'insert into today(geo, Maxtem, Mintem, Humi,Hpa,Ozone) values(%s, %s,%s, %s,%s, %s)'
             #실행한다 insert.geo, dinsert.Maxtem, dinsert.Mintem, dinsert.Humi, dinsert.Hpa, dinsert.Ozone는 %s에 들어갈 내용들이다.
            curs.execute(sql, (dinsert.geo, dinsert.Maxtem, dinsert.Mintem, dinsert.Humi, dinsert.Hpa, dinsert.Ozone))
        #삽입 내용을 확정시킨다.
        #안하면 저장이 안된다.
        conn.commit()
    finally:
        #연결을 종료한다.
        conn.close()

englishgeo = ('Seoul', 'Busan', 'Deagu', 'Incheon', 'Gwangju', 'Daejeon', 'Ulsan', 'Gyeonggi', 'Gangwon', 'Chungcheongbuk', 'Chungcheongnam', 'Jeollabuk', 'Jeollanam', 'Gyeongsangbuk', 'Gyeongsangnam', 'jeju')

if __name__ == "__main__":
    j=0
    for i in range(0, 16):
        #Test라는 함수를 불러와서 배열을 만들어 test에 넣어줍니다.
        test = Todayal(englishgeo[i], gedata[i][0], gedata[i][1],gedata[i][2],gedata[i][3],gedata[i][4])
        #insert함수를 통해서 DB에 자료를 넣어줍니다.
        insert_db(test)