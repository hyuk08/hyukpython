import requests
from bs4 import BeautifulSoup
import json

urls = ['https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000', 
        'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000',
        'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000',
        'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000',
        'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000',
        'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000',
        'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000',
        'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000',
        'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000',
        'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000',]

def 크롤링(A):
    res = requests.get(A)
    dictionary = json.loads(res.content)
    print(dictionary['body']['candles'][0:2][0]['dt']) # body 안에 candles 안에 0 ~ 1 지정하고, 그 속 0 안에 'dt' !


# 크롤링('https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/BTC?lastDt=1707534000000&interval=15m&1708253790947')
# exit()

for i in urls:
    크롤링(i)