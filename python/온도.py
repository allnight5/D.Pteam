from urllib.request import urlopen
import bs4

url =  "https://weather.naver.com/rgn/cityWetrMain.nhn"

html = urlopen(url)


bs_obj = bs4.BeautifulSoup(html.read(), "html.parser")
zxzxz=bs_obj.find("table",class_="tbl_weather tbl_today")

dsfd=zxzxz.find("tbody")
ewed=dsfd.findAll("tr")


for tr in ewed:
    eeie=tr.find("th")
    ere=eeie.find("a")

#오전   (최저기온)
    defw=tr.find("td")
    sfwe=defw.find("ul",class_="text")
    fee=sfwe.findAll("li")
    edde=fee[1].find("span" ,class_="temp")
    rtrt=edde.find("strong")

#오후   (최고기온)
    efwf = tr.find("td", class_="line")
    efwf2 = efwf.find("ul", class_="text")
    efwf3 = efwf2.findAll("li")
    efwf4 = efwf3[1].find("span", class_="temp")
    rtrt2 = efwf4.find("strong")

    print(ere.text,"오전"+":"+rtrt.text,"오후"+":"+rtrt2.text)
