import urllib.request
from bs4 import BeautifulSoup
import re
import os

def fetch_list_url():

    num = 0
    for num in range(15):
        num +=1
        gesipan_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page="+str(num)+"&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&"

        url = urllib.request.Request(gesipan_url)
        res = urllib.request.urlopen(url).read().decode("utf-8")

        soup = BeautifulSoup(res, "html.parser")  # res 에 담긴 html 코드를 beautiful soup 모듈로 검색하기 위한 작업

        a = soup.find_all('p', class_="con")
        b = soup.find_all('span', class_="date")
        cnt = 0
        for i in a:
            print(b[cnt].text, i.get_text(strip=True))
            cnt += 1

fetch_list_url()
