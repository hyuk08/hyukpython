import requests # 웹사이트 접속 도와주는 라이브러리
from bs4 import BeautifulSoup # 파이썬으로 html 웹문서 분석 도와주는 라이브러리
import json

res = requests.get('https://oname.kr/product/list_sale.html?cate_no=350', allow_redirects=True)

print(res.content)