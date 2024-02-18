import requests # 웹사이트 접속 도와주는 라이브러리
from bs4 import BeautifulSoup # 파이썬으로 html 웹문서 분석 도와주는 라이브러리
import json


def 검색어(serch):
    image_data = requests.get(f'https://s.search.naver.com/p/image/46/search.naver?ac=0\u0026aq=0\u0026display=100\u0026json_type=6\u0026mode=\u0026nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D\u0026nso=so%3Ar%2Cp%3Aall%2Ca%3Aall\u0026nx_search_query={serch}\u0026query=%EC%82%AC%EA%B3%BC\u0026section=image\u0026sqs=%7B%22intentblock%22%3A%7B%22v%22%3A%223%22%2C%22collections%22%3A%7B%22image%22%3A%7B%22blocks%22%3A%5B%7B%22bid%22%3A%22SYS-0000000047812426%22%2C%22sbr%22%3A%7B%22is_front_split%22%3Atrue%2C%22rank%22%3A1%2C%22score%22%3A0.06316185644827783%2C%22vertical_rank%22%3A1%7D%2C%22type%22%3A%22UGC_KEYWORD%22%7D%2C%7B%22bid%22%3A%22SYS-0000000047812427%22%2C%22sbr%22%3A%7B%22is_front_split%22%3Atrue%2C%22rank%22%3A2%2C%22score%22%3A0.06316185644827783%2C%22vertical_rank%22%3A2%7D%2C%22type%22%3A%22UGC_KEYWORD%22%7D%2C%7B%22bid%22%3A%22SYS-0000000046956373%22%2C%22sbr%22%3A%7B%22is_front_split%22%3Atrue%2C%22rank%22%3A3%2C%22score%22%3A0.06316185644827783%2C%22vertical_rank%22%3A3%7D%2C%22type%22%3A%22UGC_KEYWORD%22%7D%5D%2C%22qid%22%3A%22%EC%82%AC%EA%B3%BC%22%7D%7D%2C%22sbs_key%22%3A%22image-%EC%82%AC%EA%B3%BC-5d1883093f5bb02ee01e499cf65f896b%22%7D%7D\u0026where=image')

    soup = BeautifulSoup(image_data.text, 'html.parser')
    json_data = json.loads(image_data.content)
    for i in json_data["items"]:
        print('\n')
        print(i["title"])
        print(i["viewerThumb"])


A = input('검색어를 입력하세요. ')

검색어(A)

# file = open('a.html', 'w')
# file.write(str(soup))
# file.close()