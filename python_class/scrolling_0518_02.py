
import urllib.request # 웹브라우저에서 html 문서를 얻어오기 위해 통신하기 위한 모듈
from  bs4 import BeautifulSoup #html 문서 검색 모듈
import re

def fetch_list_url2():
    for i in params:
        detail_url = "http://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_vie.jsp"

        request_header = urllib.parse.urlencode({"RCEPT_NO": i})

        request_header = request_header.encode("utf-8")

        url = urllib.request.Request(detail_url, request_header)

        res = urllib.request.urlopen(url).read().decode("utf-8")

        soup = BeautifulSoup(res, "html.parser")

        soup2 = soup.find_all("div", class_="form_table")

        tables = soup2[0].find_all("table")

        table0 = tables[0].find_all("td")
        table1 = tables[1].find("div", class_="table_inner_desc")
        table2 = tables[2].find("div", class_="table_inner_desc")

        date = table0[1].get_text()
        title = table0[0].get_text()
        question = table1.get_text(strip=True)
        answer = table2.get_text(strip=True)

fetch_list_url2()