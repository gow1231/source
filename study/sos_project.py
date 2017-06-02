

#########한겨레################

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import os


def adress():
    keyword = '문재인'
    chrome = 'D:\chromedriver/chromedriver.exe'
    browser = webdriver.Chrome(chrome)  # 웹브라우저 인스턴스화
    browser.get('http://search.hani.co.kr/Search?command=query&keyword='+keyword+'&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.06.01&pageseq=1')
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    a = soup.find("ul",class_="search-result-list")
    b = a.find_all('dt')
    print(len(b))
    re = []
    for j in b:
        try:
            c = j.find('a')['href']  # 기사 주소 긁어오는 코드
            print(j.get_text())  # 기사제목
            re.append(c)
        except Exception:
            pass
    return re

def article_scroll():  #기사 내용 긁어오는 코드
    # adress = adress()    # 주소를 받아서 url_list에 하나씩 입력한다.
    # for i in adress:
    url_list = 'http://www.hani.co.kr/arti/politics/assembly/797238.html'
    url = urllib.request.Request(url_list)
    res = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(res, "html.parser")
    a = soup.find('div',class_='text')
    print(a.get_text())
article_scroll()


##############조선일보#############

def adress():
    keyword = '문재인'
    chrome = 'D:\chromedriver/chromedriver.exe'
    browser = webdriver.Chrome(chrome)  # 웹브라우저 인스턴스화
    browser.get('http://search.chosun.com/search/news.search?query='+keyword+'&pageno=1&orderby=news&naviarraystr=&kind=&cont1=&cont2=&cont5=&categoryname=&categoryd2=&c_scope=paging&sdate=&edate=&premium=')
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    a = soup.find("div",class_="search_news_box")
    b = a.find_all('dt')
    print(len(b))
    re = []
    for j in b:
        try:
            c = j.find('a')['href']  # 기사 주소 긁어오는 코드
            print(j.get_text())  # 기사제목
            re.append(c)
        except Exception:
            pass
    print(re)
    return re
def article_scroll():  #기사 내용 긁어오는 코드
    # adress = adress()    # 주소를 받아서 url_list에 하나씩 입력한다.
    # for i in adress:
    url_list = 'http://news.chosun.com/site/data/html_dir/2017/06/01/2017060103436.html'
    url = urllib.request.Request(url_list)
    res = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(res, "html.parser")
    a = soup.find('div',class_='par')
    print(a.get_text())
article_scroll()

################################ 동아일보 ###############################

def adress():
    keyword = '문재인'
    chrome = 'D:\chromedriver/chromedriver.exe'
    browser = webdriver.Chrome(chrome)  # 웹브라우저 인스턴스화
    browser.get('http://news.donga.com/search?p=16&query='+keyword+'&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1')
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    a = soup.find("div",class_="searchContWrap")
    b = a.find_all('div',class_="t")
    print(len(b))
    re = []
    for j in b:
        try:
            c = j.find('a')['href']  # 기사 주소 긁어오는 코드
            print(j.find('a').get_text())  # 기사제목
            re.append(c)
        except Exception:
            pass
    print(re)
    return re
# adress()
def article_scroll():  #기사 내용 긁어오는 코드
    # adress = adress()    # 주소를 받아서 url_list에 하나씩 입력한다.
    # for i in adress:
    url_list = 'http://news.donga.com/3/all/20170601/84679998/1'
    url = urllib.request.Request(url_list)
    res = urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(res, "html.parser")
    a = soup.find('div',class_='article_txt')
    print(a.get_text())
article_scroll()

###################경향신문##################

def adress():
    keyword = '문재인'
    chrome = 'D:\chromedriver/chromedriver.exe'
    browser = webdriver.Chrome(chrome)  # 웹브라우저 인스턴스화
    browser.get('http://search.khan.co.kr/search.html?stb=khan&q='+keyword+'&pg=1&sort=1')
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    a = soup.find("div",class_="news section")
    b = a.find_all('dl',class_="phArtc")
    print(len(b))
    re = []
    for j in b:
        try:
            c = j.find('a')['href']  # 기사 주소 긁어오는 코드
            print(j.find('a').get_text())  # 기사제목
            re.append(c)
        except Exception:
            pass
    print(re)
    return re
# adress()
def article_scroll():  #기사 내용 긁어오는 코드
    # adress = adress()    # 주소를 받아서 url_list에 하나씩 입력한다.
    # for i in adress:
    url_list = 'http://news.khan.co.kr/kh_news/khan_art_view.html?code=940100&artid=201706010600035'
    url = urllib.request.Request(url_list)
    res = urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(res, "html.parser")
    a = soup.find_all('p',class_='content_text')
    print(a)
    print(a.get_text())

article_scroll()
