
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


    # 크롤링 된 데이터를 파일로 저장하는 함수
    def data_to_file(self):
        with open(KMACrawler.FILE_PATH + "kma_crawled.txt", "a", encoding="utf-8") as file:
            file.write('======================================================\n')
            for key, value in self.data.items():
                file.write('>> ' + key[0] + ', ' + key[1] + ', ' + key[2] + '\n')
                for v in value:
                    file.write(','.join(v) + '\n')
            file.write('======================================================\n\n')
            file.close()


    # 크롤링 수행하는 메인 함수
    def play_crawling(self):
        print('크롤링을 위한 데이터를 수집 중입니다...')
        self.get_kma_data()
        print('크롤링을 위한 데이터 수집 완료 !!!')
        print('크롤링을 시작합니다...')
        for key, value in sorted(self.crawling_list.items(), key=operator.itemgetter(0)):
            #print(self.crawling_list.items()) # dict_items([(('108', '1986', '35'), ('서울(유)', '1986', '일조시간'))])
            # .items() : 딕셔너리 변수 안의 내용을 보기 위해서.
            #print(key) # ('108', '1986', '35')
            #print(value) # ('서울(유)', '1986', '일조시간')
            res = urlopen(Request(self.crawled_url.format(key[0], key[1], key[2]))).read()
            # 상세 url 을 완성해서 기상청 웹서버에 요청해서 html 정보를 받아옴. -> res에 넣음
            #print(res) # 상세 url (crawled_url)에 대한 html 코드
            soup = BeautifulSoup(res, 'html.parser')
            print('현재 키워드 : {}, {}, {}'.format(*value)) # value 에서 그대로 가져오고 있는 것.

            for tr_tag in soup.find('table', class_='table_develop').find('tbody').find_all('tr'):
                                                                         # 하나뿐이면 find, 여러 개 있으면 find_all
                #print(tr_tag)
                if self.data.get(value) is None: #value 가 None 이라면
                    #print(self.data.get(value)) # None
                    self.data[value] = []  # data dic 의 key 에 빈 리스트 []를 넣어라. append 시키려고.
                self.data[value].append(['' if td_tag.text =='\xa0' else td_tag.text for td_tag in tr_tag.find_all('td') if td_tag.has_attr('scope') is False])
                # 뒤에서부터. tr 태그의 td(여러 값)를 찾아서 td 태그의 text 를 가져와서 / 이미지 참조 / append / dict_items 를 만들고 있는 것.
                # 1일, 2일 ... 을 빼고 데이터를 받고 싶다면 if td_tag.has_attr('scope') is False 를 추가한다. attribute 가 scope 인 데이터 -> 1일, 2일....
            #print (self.data.items()) # '\xa0' - 비어있는 값.
            print('{}, {}, {} 에 대한 데이터 저장...'.format(*value))
            # 저장하는 함수 data_to_file() 실행
            self.data_to_file()
            self.data.clear() # 파일에 저장하고 dict_items 를 클리어하는 것.
            print('저장 완료!!!\n\n')
            time.sleep(2)
        print('크롤링 완료 !!!')


crawler = KMACrawler()
crawler.play_crawling()
