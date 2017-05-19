

# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import operator
import time

class KMACrawler:
    FILE_PATH = 'C:\\kma\\' # 기상 데이터를 수집할 위치를 지정
    def __init__(self):
        self.location_list = {} # 검색 조건 3개 중 지역의 데이터를 담을 변수
        self.year_list = {} # 검색 조건 중 연도 데이터를 담을 변수
        self.factor_list = {} # 검색 조건 중 요소(평균기온, 최고기온....) 데이터를 담을 변수
        self.crawling_list = {} # 위의 세가지 조건으로 수집한 데이터 /  ('279', '1969', '07'): ('구미(무)', '1969', '평균기온') / key : value
        self.data = {} # 실제 결과 데이터를 담는 딕셔너리 변수
                       # 백령도(유), 2001, 최고기온
                       # 3.7,-1.5,7.0,8.5,12.5,22.1,25.8,24.8,27.8,19.4,13.0,8.3 ....

        self.default_url = 'http://www.kma.go.kr/weather/climate/past_table.jsp'
        # 기상청의 온도 확인하는 메인 url
        self.crawled_url = 'http://www.kma.go.kr/weather/climate/past_table.jsp?stn={}&yy={}&obs={}'
        # 특정 지역, 연도, 요소에 따라 데이터를 조회하는 상세 url

    # 지점, 연도, 요소에 데이터 가져오는 함수
    def get_kma_data(self):
        res = urlopen(Request(self.default_url)).read()
        #print(res) : 메인 url 에서 html 코드를 가져온다.
        soup = BeautifulSoup(res, 'html.parser')
        # res html 코드를 BeautifulSoup로 검색하기 위해 인스턴스화
        location = soup.find('select', id='observation_select1')
        # 지역에 관련한 html 코드만 가져오는 부분
        #print(location) # <option value="294">거제(무)</option>
        year = soup.find('select', id='observation_select2')
        # 연도에 관련한 html 코드만 가져오는 부분
        #print(year) # <option value="1960">1960</option>
        factor = soup.find('select', id='observation_select3')
        # 요소에 관련한 html 코드만 가져오는 부분
        #print(factor) # <option value="21">강수량</option>

        for tag in location.find_all('option'): # location에 해당하는 옵션 tag 부분을 전체 검색
            if tag.text != '--------': # html 코드에 있는 ------- 구분선이 나오지 않도록.
                self.location_list[tag['value']] = tag.text
                # print(tag['value']) # 294
                # print(tag.text)     # 거제(무)

        for tag in year.find_all('option'):
            if tag.text != '--------':
                self.year_list[tag['value']] = tag.text
                # print(tag['value']) #  1961
                # print(tag.text)     #  1961

        for tag in factor.find_all('option'):
            if tag.text != '--------':
                self.factor_list[tag['value']] = tag.text
                # print(tag['value'])  # 06
                # print(tag.text)     # 평균풍속
        # print(self.location‎_list.items())
        # print(self.year_list.items())
        # print(self.factor_list.items())
        for loc_key, loc_value in self.location_list.items():
            for year_key, year_value in self.year_list.items():
                for fac_key, fac_value in self.factor_list.items():
                    self.crawling_list[(loc_key, year_key, fac_key)] = (loc_value, year_value, fac_value)

        #print (self.crawling_list) #  ('136', '1969', '06'): ('안동(유)', '1969', '평균풍속'), ......


crawler = KMACrawler()
crawler.get_kma_data()
