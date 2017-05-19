

import urllib.request
from  bs4 import BeautifulSoup
from selenium import webdriver # 웹 애플리케이션의 테스트를 자동화하기 위한 프레임워크
from selenium.webdriver.common.keys import Keys
import time # 중간중간 SLEEP 을 걸어야 해서 time 모듈을 import 받는다.

binary = 'C:\chromedriver/chromedriver.exe'
browser = webdriver.Chrome(binary)
browser.get("https://www.bing.com/?scope=images&FORM=Z9LH1")  # 빙 이미지 검색 url
elem = browser.find_element_by_id("sb_form_q")

# 검색어 입력
elem.send_keys("인공지능")
elem.submit()

# 반복할 횟수
for i in range(1, 2):
    browser.find_element_by_xpath("//body").send_keys(Keys.END)

    time.sleep(5)
time.sleep(5)
html = browser.page_source
soup = BeautifulSoup(html, "lxml")


def fetch_list_url():
    params = []
    imgList = soup.find_all("img", class_="mimg")
    for im in imgList:
        params.append(im["src"])
    return params


def fetch_detail_url():
    params = fetch_list_url()
    a = 1
    for p in params:
        urllib.request.urlretrieve(p, "c:/bingimage/" + str(a) + ".jpg")
        a = a + 1


fetch_detail_url()

browser.quit()
