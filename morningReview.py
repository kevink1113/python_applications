from selenium import webdriver
from os import system

from urllib import request, parse, error
from bs4 import BeautifulSoup
import requests

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('--disable--gpu')
chrome_options.add_argument('lang=ko_KR')
browser = webdriver.Chrome('/Applications/chromedriver', options = chrome_options)

stocks = ["테슬라", "애플"]

def printStockInfo():
    print("\n[나스닥]")
    system("say 밤 동안의 나스닥 시황을 말씀드릴게요.")
    for stock in stocks:
        res = ""
        stockUrl = "http://search.naver.com/search.naver?query=" + stock + " 주식"
        browser.get(stockUrl)
        upDown = browser.find_elements_by_css_selector('#_cs_root > div.ar_spot > div > h3 > a > span.spt_con.up > span.n_ch > em')

        final = upDown[1].text
        final = final[1:-1]
        if final[0] == '-':
            sayUpDown = " 하락"
            final = final[1:]
        else:
            sayUpDown = " 상승"
        FINAL = (stock + ": " + final + sayUpDown)
        print(FINAL)
        system("say " + FINAL)
    system("say 했어요.")


def sayGoodMorning():
    system("say 안녕하세요, 상원님. 좋은 아침이에요. ")

def sayWeather():
    print("[날씨]")
    weatherUrl = "http://search.naver.com/search.naver?query=" + "날씨"
    browser.get(weatherUrl)
    weatherInfo = browser.find_elements_by_class_name("cast_txt")

    tempInfo = browser.find_elements_by_class_name("num")

    minTemp = tempInfo[0].text
    maxTemp = tempInfo[1].text
    feelTemp = tempInfo[2].text

    print(weatherInfo[0].text)
    print("최저 " + minTemp + "도, " + "최고 " + maxTemp + "도, " + "체감 " + feelTemp + "도")
    system("say 오늘의 날씨는")
    system("say " + weatherInfo[0].text + ". 최저 " + minTemp + "도, " + "최고 " + maxTemp + "도, " + "체감온도" + feelTemp + "도 랍니다.")

sayGoodMorning()
sayWeather()
printStockInfo()

browser.quit()