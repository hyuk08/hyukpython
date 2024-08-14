import requests # 웹사이트 접속 도와주는 라이브러리
from bs4 import BeautifulSoup # 파이썬으로 html 웹문서 분석 도와주는 라이브러리

A = input('검색어를 입력하세요. ')

def 검색어(serch):
    url = requests.get(f'https://s.search.naver.com/p/review/47/search.naver?ssc=tab.blog.all&api_type=4&query={serch}&start=1&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_jum&nso=&prank=30&ngn_country=KR&lgl_rcode=&fgn_region=&fgn_city=&lgl_lat=&lgl_long=&enlu_query=IggCAFyDULjqAAAAtdoURqXUdp9ygLuVMM8qJvRm5uq4t7Hezx%2BI5KC1OLtnvfCDUGoxbb4rBZsXC2NVdG%2FAki6dXzKBvuK6OOOadKCHSk%2FqdY9H1it1ThgTHJfUWzdkg0bjVW7ChYVW75029kRScBLdXj2XCKUejtyIDFnTe8xCyczMj3SR7qHZP867EN6p4%2BQvSQeutnTruEpznIHCtkrJjQd8%2BhAOaeX%2FvO9YcWqt5GCX4ixNremxROT11myTk0OygJYjI00VdvMLixi7Za5cFJkTckYsi9FkX9E%2F%2BIy%2B2SGKmANopKE%2FCnCRpPpRm59Ct8Igm1%2FhGlfeT0YLhCv7I59GlUEvRosKak4Kwtx0jmSZhvd%2BZqqth5yzAPlMyDYq%2BA9YvoVJ3dxAdL3OsP2lOVPV9AR3nn5%2BPCDxn8rtQ35IXd1qBcrT5RBn9PwnvxeicdksEbyKqY9UD1hX%2BhbM9nt%2BHMssbOlm5vG8uMca0mZDHUzmlafzbjh4jRXXdELEdv3YenKRLrNa&abt=&_callback=getBlogContents&_callback=getBlogContents&_=1708154725264')
    soup = BeautifulSoup(url.text.replace('\\', ''), 'html.parser')

    # print(soup)
    # # print(url.status_code)
    # exit()

    title_list = soup.select('a.title_link')
    titlename_list = soup.select('a.title_link')
    print('\n -- 가장 상위에 노출되는 블로그 30 -- \n')
    for i in range(0, 30):
        print(titlename_list[i].text)
        print(title_list[i]['href'], '\n')

검색어(A)