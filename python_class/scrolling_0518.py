

import urllib.request # 웹브라우저에서 html 문서를 얻어오기 위해 통신하기 위한 모듈
from  bs4 import BeautifulSoup #html 문서 검색 모듈
import re
import os

def get_save_path():
    save_path = input("Enter the file name and file location :" )
    save_path = save_path.replace("\\", "/")
    if not os.path.isdir(os.path.split(save_path)[0]):
        os.mkdir(os.path.split(save_path)[0])  # 폴더가 없으면 만드는 작업

    return save_path

def fetch_list_url():

    params = []

    for j in range(1,30):
        list_url = "http://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_lis.jsp"

            # Java script 인 페이지를 스크롤링 하는 방법
        request_header = urllib.parse.urlencode({"page":j})
            #print(request_header) # page =1 , page =2 ...

            #utf-8 로 인코드해야 파이썬이 인식할 수 있다.6
        request_header = request_header.encode("utf-8")
        url = urllib.request.Request(list_url, request_header) #  request_header 정보를 줘야 한다.

        res = urllib.request.urlopen(url).read().decode("utf-8")

        soup = BeautifulSoup(res, "html.parser")  # res html 문서를 BeautifulSoup 모듈을 사용해서 검색할수있도록 설정
        soup2 = soup.find_all("li", class_="pclist_list_tit2")

        for soup3 in soup2:
            soup4 = soup3.find("a")["href"]
            params.append(re.search("[0-9]{14}", soup4).group())

    return params

fetch_list_url()

def fetch_list_url2():

    f = open(get_save_path(), 'w', encoding="utf-8")
    params2 = fetch_list_url()

    for i in params2:

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

        f.write("==" * 30 + "\n")
        f.write(title + "\n")
        f.write(date + "\n")
        f.write(question + "\n")
        f.write(answer + "\n")
        f.write("==" * 30 + "\n")

    f.close()

fetch_list_url2()



