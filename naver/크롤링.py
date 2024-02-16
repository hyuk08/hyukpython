import requests # 웹사이트 접속 도와주는 라이브러리
from bs4 import BeautifulSoup # 파이썬으로 html 웹문서 분석 도와주는 라이브러리

# naver_python = requests.get('https://s.search.naver.com/p/review/47/search.naver?ssc=tab.blog.all&api_type=4&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&start=1&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_jum&nso=so%3Ar%2Cp%3Aall&prank=65&ngn_country=KR&lgl_rcode=&fgn_region=&fgn_city=&lgl_lat=&lgl_long=&enlu_query=IggCAHSDULjtAAAAtdoURqXUdp9ygLuVMM8qJlLSaZYIB8zCgkkjbmqF2CccwGRoSv0vzTaiP6K%2F1aMT5%2FM7UUUkrTdp79YpKKqxI1pCn1b11McNPVz66PbCcU%2Fd6QUydG3HVLkmtsl25nGzAlilno%2BwiqJMiFuIfUb%2BA%2BqupQgaViBJ0j1DDvPoy%2FyhSmtlVLmQvLhWBABktjTlI0VdOpgaJNytGtsHN6XunbPp5TvBoM%2BDvULIeWmLUCkJa82SjwzYvvUQR07DMnkf1Z9UxpbHC%2FdeOr4%2F5J7lWzjb%2FpM4DU1UPXcJmWsNU2AqFlO9OQlhsqnqT9NfVP%2FmAUQRtNfhCgQaZb6Tun9BdkB%2Fq%2Fp66qqGKUjtjclLfvLJ%2B%2FyXDf8Ii8D2c%2FhYncSiARhVo0NGBOOtf2el6z8vT9wNOjv1WSXUYGeZOJMfIZ4ALBVr0%2FERsYApRpWK94lGaRTz20fOlO5r5c1XgWIPqg%3D%3D&abt=&_callback=getBlogContents&_callback=getBlogContents&_=1708074742520')
# print(naver_python.content)
# print(naver_python.status_code)
# 가끔 백슬래쉬가 낑겨있을 때가 있는데, 클래스명에 껴있으면 헷갈려함. 그래서 제거를 해줘야 하는데 
# 수프에 담굴 때 같이 빼주면 됨.                         vv 이것처럼 (두 번 쳐야 글자로 인식함.)
# soup = BeautifulSoup(naver_python.text.replace('\\', ''), 'html.parser')
# replace 를 하려면 앞에게 문자열이여야 하는데 .content는 문자열로 인식하지 않음. 그래서 .text로 바꿔서 입력함.(그래도 html 잘 나옴. ㅇㅇ)

# list = soup.select('a.title_link')
# for i in range(0, 30):
#     print(list[i].text)

# naver_python2 = requests.get('https://s.search.naver.com/p/review/47/search.naver?ssc=tab.blog.all&api_type=4&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&start=31&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_jum&nso=so%3Ar%2Cp%3Aall&prank=65&ngn_country=KR&lgl_rcode=&fgn_region=&fgn_city=&lgl_lat=&lgl_long=&enlu_query=IggCAHSDULjtAAAAtdoURqXUdp9ygLuVMM8qJlLSaZYIB8zCgkkjbmqF2CccwGRoSv0vzTaiP6K%2F1aMT5%2FM7UUUkrTdp79YpKKqxI1pCn1b11McNPVz66PbCcU%2Fd6QUydG3HVLkmtsl25nGzAlilno%2BwiqJMiFuIfUb%2BA%2BqupQgaViBJ0j1DDvPoy%2FyhSmtlVLmQvLhWBABktjTlI0VdOpgaJNytGtsHN6XunbPp5TvBoM%2BDvULIeWmLUCkJa82SjwzYvvUQR07DMnkf1Z9UxpbHC%2FdeOr4%2F5J7lWzjb%2FpM4DU1UPXcJmWsNU2AqFlO9OQlhsqnqT9NfVP%2FmAUQRtNfhCgQaZb6Tun9BdkB%2Fq%2Fp66qqGKUjtjclLfvLJ%2B%2FyXDf8Ii8D2c%2FhYncSiARhVo0NGBOOtf2el6z8vT9wNOjv1WSXUYGeZOJMfIZ4ALBVr0%2FERsYApRpWK94lGaRTz20fOlO5r5c1XgWIPqg%3D%3D&abt=&_callback=getBlogContents&_callback=getBlogContents&_=1708074742520')
# soup = BeautifulSoup(naver_python2.text.replace('\\', ''), 'html.parser')
# list = soup.select('a.title_link')
# for i in range(0, 30):
#     print(list[i].text)

# def 출력(page):
#     naver_python = requests.get(f'https://s.search.naver.com/p/review/47/search.naver?ssc=tab.blog.all&api_type=4&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&start={page}&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_jum&nso=so%3Ar%2Cp%3Aall&prank=65&ngn_country=KR&lgl_rcode=&fgn_region=&fgn_city=&lgl_lat=&lgl_long=&enlu_query=IggCAHSDULjtAAAAtdoURqXUdp9ygLuVMM8qJlLSaZYIB8zCgkkjbmqF2CccwGRoSv0vzTaiP6K%2F1aMT5%2FM7UUUkrTdp79YpKKqxI1pCn1b11McNPVz66PbCcU%2Fd6QUydG3HVLkmtsl25nGzAlilno%2BwiqJMiFuIfUb%2BA%2BqupQgaViBJ0j1DDvPoy%2FyhSmtlVLmQvLhWBABktjTlI0VdOpgaJNytGtsHN6XunbPp5TvBoM%2BDvULIeWmLUCkJa82SjwzYvvUQR07DMnkf1Z9UxpbHC%2FdeOr4%2F5J7lWzjb%2FpM4DU1UPXcJmWsNU2AqFlO9OQlhsqnqT9NfVP%2FmAUQRtNfhCgQaZb6Tun9BdkB%2Fq%2Fp66qqGKUjtjclLfvLJ%2B%2FyXDf8Ii8D2c%2FhYncSiARhVo0NGBOOtf2el6z8vT9wNOjv1WSXUYGeZOJMfIZ4ALBVr0%2FERsYApRpWK94lGaRTz20fOlO5r5c1XgWIPqg%3D%3D&abt=&_callback=getBlogContents&_callback=getBlogContents&_=1708074742520')
#     soup = BeautifulSoup(naver_python.text.replace('\\', ''), 'html.parser')
#     list = soup.select('a.title_link')
#     for i in range(0, 30):
#         print(list[i].text)

# 출력(1)
# 출력(31)
import requests # 웹사이트 접속 도와주는 라이브러리
from bs4 import BeautifulSoup # 파이썬으로 html 웹문서 분석 도와주는 라이브러리

url = requests.get('https://www.stardailynews.co.kr/news/articleView.html?idxno=436126')
soup = BeautifulSoup(url.content, 'html.parser')


# print(soup)
# # print(url.status_code)
# exit()

image_src = soup.select('div.IMGFLOATING > img')[0]['src']
print(image_src)