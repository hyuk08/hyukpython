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
    return dictionary['data'][0]['Close']

# 크롤링(urls[0])
# 크롤링(urls[1])
# 크롤링(urls[2])
# 크롤링(urls[3])
# 크롤링(urls[4])
# 크롤링(urls[5])
# 크롤링(urls[6])
# 크롤링(urls[7])
# 크롤링(urls[8])
# 크롤링(urls[9])
# print('완료')
# exit()


# # map() # 리스트 자료에, 똑같은 작업을 전부 시키고 싶을 때 사용.
# 리스트 = [2, 3, 4, 5] # 이 리스트에 각각 1씩 더하고 싶다면? 
# for i in 리스트:
#     print(i + 1) # = 3, 4, 5, 6
# # 근데 여기서 map()함수를 쓰는 방법도 있음.
# def 아무거나함수(x):
#     return x + 1
# result = map(아무거나함수, 리스트)
# print(list(result))
# exit()
from multiprocessing.dummy import Pool as ThreadPool # 멀티쓰레딩 라이브러리

pool = ThreadPool(4)
result = pool.map(크롤링, urls)
pool.close()
pool.join()

print(result)