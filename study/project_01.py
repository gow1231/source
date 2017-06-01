import urllib.request # 웹브라우저에서 html 문서를 얻어오기 위해 통신하기 위한 모듈
from  bs4 import BeautifulSoup #html 문서 검색 모듈
import os

# def get_save_path():
#     save_path = input("C:\data_haeri" )
#     save_path = save_path.replace("\\", "/")
#     if not os.path.isdir(os.path.split(save_path)[0]):
#         os.mkdir(os.path.split(save_path)[0])  # 폴더가 없으면 만드는 작업
#
#     return save_path

def fetch_list_url():

        params = []

        for num in range(0, 20):

            list_url = "http://search.joins.com/TotalNews?page="+str(num)+"&Keyword=%EB%AC%B8%EC%9E%AC%EC%9D%B8&SortType=New&SearchCategoryType=TotalNews"
            url = urllib.request.Request(list_url) # url 요청에 따른 http 통신 헤더값을 얻어낸다
            res = urllib.request.urlopen(url).read().decode("utf-8")

            soup = BeautifulSoup(res, "html.parser")  # res html 문서를 BeautifulSoup 모듈을 사용해서 검색할수있도록 설정

            for i in range(0,20):
                try:
                    soup2 = soup.find_all("div", class_="text")[i]
                    soup3 = soup2.find("a")["href"]
                    params.append(soup3)
                except Exception:
                    pass

        return params
        #print(params) 링크 타고 들어가니 기사..... 그냥 기사까지 전부 크롤링해도 괜찮겠는데?
        # ['http://news.joins.com/article/21631035',
        #  'http://news.joins.com/article/21631017', ...... ]

fetch_list_url()

def fetch_list_url2():

    params2 = fetch_list_url()
    #f = open(get_save_path(), 'w', encoding="utf-8") # w : write
    for i in params2:
        list_url2 = i
        url2 = urllib.request.Request(list_url2)
        res = urllib.request.urlopen(url2).read().decode("utf-8")
        soup = BeautifulSoup(res, "html.parser")
        result = soup.find_all('h1', id="article_title")[0] # 굳이 for 문을 써서 tag를 바꾸지 않고 이렇게 바꿔도 됨!!!
        print(result.get_text(strip=True))
        #print(type(result2)) #<class 'bs4.element.ResultSet'>

        #result = soup.find_all('div',id="article_body")[0]
        #final = result.get_text(strip=True, separator='\n')

        #f.write(final)
    #f.close()

fetch_list_url2()
