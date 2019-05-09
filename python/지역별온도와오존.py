from urllib.request import urlopen
import bs4


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
경상북도="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B2%BD%EC%83%81%EB%B6%81%EB%8F%84%EB%82%A0%EC%94%A8&oquery=%EC%A0%84%EB%9D%BC%EB%82%A8%EB%8F%84%EB%82%A0%EC%94%A8&tqi=UL6kUwp0J1sssMnaLKosssssst0-251498"#경상남도="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B2%BD%EC%83%81%EB%82%A8%EB%8F%84%EB%82%A0%EC%94%A8&oquery=%EA%B2%BD%EC%83%81%EB%B6%81%EB%8F%84%EB%82%A0%EC%94%A8&tqi=UL6kNsp0YiRssclhtSlssssst4Z-478748"
제주도="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%A0%9C%EC%A3%BC%EB%8F%84%EB%82%A0%EC%94%A8&oquery=%EA%B2%BD%EC%83%81%EB%82%A8%EB%8F%84%EB%82%A0%EC%94%A8&tqi=UL6klwp0J1ZssvVIIzVssssssAZ-484652"
html = urlopen(전라북도)


bs_obj = bs4.BeautifulSoup(html.read(), "html.parser")

#오존수치 오늘
main2=bs_obj.find("div",class_="detail_box")
sfee=main2.find("dl")
ewef=sfee.findAll("dd")
ozan=ewef[2].find("span")


#온도 오늘
zxzxz=bs_obj.find("div",class_="main_info")
dsfd=zxzxz.find("div")
ede=dsfd.find("ul")
eiui=ede.findAll("li")
erer=eiui[1].find("span")
min2=erer.find("span",class_="min")

max2=erer.find("span", class_="max")

print("최고기온",max2.text,"최저기온",min2.text,"오존",ozan.text)

