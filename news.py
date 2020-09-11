from urllib import request, parse, error
from bs4 import BeautifulSoup
import requests
import webbrowser

url = 'https://www.daum.net/' #url 선언
response = requests.get("https://news.naver.com/main/ranking/popularDay.nhn")

soup = BeautifulSoup(response.content, "html.parser")
search_top = soup.select('.ranking_section dt a')



for i, ins in enumerate(search_top):
    num = i + 1
    if num == 1:
        print("\n[ 정치 ]")
    elif num == 6:
        print("\n[ 경제 ]")
    elif num == 11:
        print("\n[ 사회 ]")
    elif num == 16:
        print("\n[ 생활/문화 ]")
    elif num == 21:
        print("\n[ 세계 ]")
    elif num == 26:
        print("\n[ IT/과학 ]")
    search_word = ins.text
    print("{}: {}".format(num, search_word))

print("\n===============================================")
while 1:
    idx = int(input("자세히 보고 싶은 기사 번호를 입력하세요. (종료하려면 0): "))
    if idx == 0:
        break
    if idx >30 or idx < 0:
        print("Invalid number!")
        continue

    print("Opening " + search_top[idx-1].text + "\n")
    webbrowser.open_new_tab("https://news.naver.com" + search_top[idx-1]['href'])