import requests # 웹사이트 접속 도와주는 라이브러리
from bs4 import BeautifulSoup # 파이썬으로 html 웹문서 분석 도와주는 라이브러리
import json
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
# import requests # 웹사이트 접속 도와주는 라이브러리
# from bs4 import BeautifulSoup # 파이썬으로 html 웹문서 분석 도와주는 라이브러리

# exit()
# def 검색어(serch):
# #     url = requests.get(f'https://s.search.naver.com/p/review/47/search.naver?ssc=tab.blog.all&api_type=4&query={serch}&start=1&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_jum&nso=&prank=30&ngn_country=KR&lgl_rcode=&fgn_region=&fgn_city=&lgl_lat=&lgl_long=&enlu_query=IggCAFyDULjqAAAAtdoURqXUdp9ygLuVMM8qJvRm5uq4t7Hezx%2BI5KC1OLtnvfCDUGoxbb4rBZsXC2NVdG%2FAki6dXzKBvuK6OOOadKCHSk%2FqdY9H1it1ThgTHJfUWzdkg0bjVW7ChYVW75029kRScBLdXj2XCKUejtyIDFnTe8xCyczMj3SR7qHZP867EN6p4%2BQvSQeutnTruEpznIHCtkrJjQd8%2BhAOaeX%2FvO9YcWqt5GCX4ixNremxROT11myTk0OygJYjI00VdvMLixi7Za5cFJkTckYsi9FkX9E%2F%2BIy%2B2SGKmANopKE%2FCnCRpPpRm59Ct8Igm1%2FhGlfeT0YLhCv7I59GlUEvRosKak4Kwtx0jmSZhvd%2BZqqth5yzAPlMyDYq%2BA9YvoVJ3dxAdL3OsP2lOVPV9AR3nn5%2BPCDxn8rtQ35IXd1qBcrT5RBn9PwnvxeicdksEbyKqY9UD1hX%2BhbM9nt%2BHMssbOlm5vG8uMca0mZDHUzmlafzbjh4jRXXdELEdv3YenKRLrNa&abt=&_callback=getBlogContents&_callback=getBlogContents&_=1708154725264')
#     soup = BeautifulSoup(url.text.replace('\\', ''), 'html.parser')

#     # print(soup)
#     # # print(url.status_code)
#     # exit()

#     title_list = soup.select('a.title_link')
#     titlename_list = soup.select('a.title_link')
#     print('\n -- 가장 상위에 노출되는 블로그 30 -- \n')
#     for i in range(0, 30):
#         print(titlename_list[i].text)
#         print(title_list[i]['href'], '\n')

# A = input('검색어를 입력하세요. ')

# 검색어(A)

# import json

# data = requests.get('https://crix-api-cdn.upbit.com/v1/crix/candles/minutes/60?code=CRIX.UPBIT.KRW-BTC&count=2&to=2024-02-17T08%3A34%3A30Z&timestamp=1708158871839')

# i = json.loads(data.content) # "" -> '' (json 을 딕셔너리 형태로 바꿔줌.)
# print(i[0]['code'])
# print(i[1]['timestamp'])


# import json
# def 검색어(serch):
#     image_data = requests.get(f'https://s.search.naver.com/p/image/46/search.naver?ac=0\u0026aq=0\u0026display=100\u0026json_type=6\u0026mode=\u0026nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D\u0026nso=so%3Ar%2Cp%3Aall%2Ca%3Aall\u0026nx_search_query={serch}\u0026query=%EC%82%AC%EA%B3%BC\u0026section=image\u0026sqs=%7B%22intentblock%22%3A%7B%22v%22%3A%223%22%2C%22collections%22%3A%7B%22image%22%3A%7B%22blocks%22%3A%5B%7B%22bid%22%3A%22SYS-0000000047812426%22%2C%22sbr%22%3A%7B%22is_front_split%22%3Atrue%2C%22rank%22%3A1%2C%22score%22%3A0.06316185644827783%2C%22vertical_rank%22%3A1%7D%2C%22type%22%3A%22UGC_KEYWORD%22%7D%2C%7B%22bid%22%3A%22SYS-0000000047812427%22%2C%22sbr%22%3A%7B%22is_front_split%22%3Atrue%2C%22rank%22%3A2%2C%22score%22%3A0.06316185644827783%2C%22vertical_rank%22%3A2%7D%2C%22type%22%3A%22UGC_KEYWORD%22%7D%2C%7B%22bid%22%3A%22SYS-0000000046956373%22%2C%22sbr%22%3A%7B%22is_front_split%22%3Atrue%2C%22rank%22%3A3%2C%22score%22%3A0.06316185644827783%2C%22vertical_rank%22%3A3%7D%2C%22type%22%3A%22UGC_KEYWORD%22%7D%5D%2C%22qid%22%3A%22%EC%82%AC%EA%B3%BC%22%7D%7D%2C%22sbs_key%22%3A%22image-%EC%82%AC%EA%B3%BC-5d1883093f5bb02ee01e499cf65f896b%22%7D%7D\u0026where=image')

#     soup = BeautifulSoup(image_data.text, 'html.parser')

# # file = open('a.html', 'w')
# # file.write(str(soup))
# # file.close()

# # exit()
# # soup = BeautifulSoup(image_data.content, 'html.parser')
#     json_data = json.loads(image_data.content)
# # exit()
# # hdline_titles = soup.select('.tile_item ._fe_image_tab_content_tile')

#     for i in json_data["items"]:
#         print('\n')
#         print(i["title"])
#         print(i["viewerThumb"])


# A = input('검색어를 입력하세요. ')
# 검색어(A)



# res = requests.get('')


# json_data = json.loads(res.content)
# exit()

# file = open('b.json', 'w')
# file.write(str(soup))
# file.close()