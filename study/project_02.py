#
#
# import urllib.request
# from bs4 import BeautifulSoup
# import re
# import os
#
press = {'중앙' : ["http://search.joins.com/TotalNews?page=2&Keyword=%EB%AC%B8%EC%9E%AC%EC%9D%B8&SortType=New&SearchCategoryType=TotalNews","CFFCGC"],
         '조선' : "http://search.chosun.com/search/news.search?query=%EB%AC%B8%EC%9E%AC%EC%9D%B8&pageno=2&orderby=news&naviarraystr=&kind=&cont1=&cont2=&cont5=&categoryname=&categoryd2=&c_scope=paging&sdate=&edate=&premium=",
         '동아' : "http://news.donga.com/search?p=16&query=%EB%AC%B8%EC%9E%AC%EC%9D%B8&check_news=2&more=1&sorting=1&search_date=1&v1=&v2=&range=1",
         '한겨레' : "http://search.hani.co.kr/Search?command=query&keyword=%EB%AC%B8%EC%9E%AC%EC%9D%B8&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.06.01&pageseq=1",
         '경향' : "http://search.khan.co.kr/search.html?stb=khan&q=%EB%AC%B8%EC%9E%AC%EC%9D%B8&pg=2&sort=1",
         '오마이' : "http://www.ohmynews.com/NWS_Web/Search/s_news.aspx?keyword=%uBB38%uC7AC%uC778&page=2"}

print(press.values()[0][1]) # 이게 뭐람??????????????

# def get_save_path():
#     save_path = input("C:\data7" )
#     save_path = save_path.replace("\\", "/")
#     if not os.path.isdir(os.path.split(save_path)[0]):
#         os.mkdir(os.path.split(save_path)[0])  # 폴더가 없으면 만드는 작업
#
#     return save_path
#
#
# # list_url = press
# # url = urllib.request.Request(list_url)
# # res = urllib.request.urlopen(url).read().decode('utf-8')
# # soup = BeautifulSoup(res, "html.parser")
#
#
# def fetch_list_url():
#     params = []
#
#     for num in range(0, 20):
#
#         list_url = press
#         url = urllib.request.Request(list_url)  # url 요청에 따른 http 통신 헤더값을 얻어낸다.
#         res = urllib.request.urlopen(url).read().decode("utf-8")
#
#         soup = BeautifulSoup(res, "html.parser")  # res html 문서를 BeautifulSoup 모듈을 사용해서 검색할수있도록 설정
#
#         for i in range(0, 20):
#             try:
#                 soup2 = soup.find_all('div', class_="text")[i]
#                 soup3 = soup2.find("a")["href"]
#                 params.append(soup3)
#             except Exception:
#                 pass
#
#     return params
#
#
# fetch_list_url()