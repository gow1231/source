

import urllib.request # 웹브라우저에서 html 문서를 얻어오기 위해 통신하기 위한 모듈
from  bs4 import BeautifulSoup #html 문서 검색 모듈
import os

def get_save_path():
    save_path = input("Enter the file name and file location :" )
    save_path = save_path.replace("\\", "/")
    if not os.path.isdir(os.path.split(save_path)[0]):
        os.mkdir(os.path.split(save_path)[0])  # 폴더가 없으면 만드는 작업

    return save_path


def fetch_list_url():

        params = []

        for num in range(0, 20):

            list_url = "http://search.joins.com/JoongangNews?" \
                       "page={}&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&" \
                       "SortType=New&SearchCategoryType=JoongangNews".format(num)
            url = urllib.request.Request(list_url) # url 요청에 따른 http 통신 헤더값을 얻어낸다
            res = urllib.request.urlopen(url).read().decode("utf-8")

            soup = BeautifulSoup(res, "html.parser")  # res html 문서를 BeautifulSoup 모듈을 사용해서 검색할수있도록 설정

            for i in range(0,20):
                try:
                    soup2 = soup.find_all('div', class_="text")[i]
                    soup3 = soup2.find("a")["href"]
                    params.append(soup3)
                except Exception:
                    pass

        return params

fetch_list_url()


def fetch_list_url2():

    params2 = fetch_list_url()
    f = open(get_save_path(), 'w', encoding="utf-8") # w : write
    #print(params2) #['http://www.hani.co.kr/arti/culture/book/778730.html', 'http://www.hani.co.kr/arti/science/science_general/778615.html', 'http://www.hani.co.kr/arti/economy/it/778234.html',......]
    for i in params2:
        list_url2 = i
        url2 = urllib.request.Request(list_url2)
        res = urllib.request.urlopen(url2).read().decode("utf-8")
        soup = BeautifulSoup(res, "html.parser")
        result2 = soup.find_all('div', id="article_body")[0] # 굳이 for 문을 써서 tag를 바꾸지 않고 이렇게 바꿔도 됨!!!
        #print(type(result2)) #<class 'bs4.element.ResultSet'>

        result = soup.find_all('div',id="article_body")[0]
        final = result.get_text(strip=True, separator='\n')

        f.write(final)
    f.close()

fetch_list_url2()
