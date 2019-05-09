from urllib.request import urlopen
import bs4

url =  "http://www.weather.go.kr/weather/observation/currentweather.jsp"

html = urlopen(url)


bs_obj = bs4.BeautifulSoup(html.read(), "html.parser")
zxzxz=bs_obj.find("div",class_="width2")

weweee=zxzxz.find("div",id="content_weather")
rtt=weweee.find("table",class_="table_develop3")
dsfd=rtt.find("tbody")
dsfd2=rtt.find("thead")
tytyt=dsfd2.find("tr",id="table_header2")
tytyt1=dsfd2.find("tr",id="table_header1")
tyty2=tytyt.findAll("th")
tyt2=tytyt1.findAll("th")
rtr=tyty2[8]
#지점 rtr2=tyt2[0]
rtr3=tyt2[5]  #기압
print("지역","  ",rtr.text,"  ",rtr3.text)
tyty=dsfd.findAll("tr")

#습도 % 기압
for tr in tyty:
    ewe2=tr.findAll("td")
    wefe=ewe2[9]
    wefe3 = ewe2[12]
    wefe2 = ewe2[0]
    print(wefe2.text,"-->",wefe.text,"  ",wefe3.text)

