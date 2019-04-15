from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import  FirefoxBinary
from selenium.webdriver.common.desired_capabilities import  DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys
import datetime as dt
import pandas as pd

binary=FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
browser=webdriver.Firefox(executable_path='C:/Users/김현구/Downloads/geckodriver-v0.24.0-win64/geckodriver.exe',firefox_binary=binary)



url='https://www.airkorea.or.kr/web/realSearch'

browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

tweets = soup.find("table", {"class": "st_1 stoke"})
dod=tweets.find("tbody")
trs=dod.findAll("tr")
for tr in trs:
        dwe = tr.findAll("td")
        dwe2 = tr.find("th")
        print(dwe2.text,"=>",dwe[5].text)

