import requests # 웹사이트 접속 도와주는 라이브러리
from bs4 import BeautifulSoup # 파이썬으로 html 웹문서 분석 도와주는 라이브러리

samsung = requests.get('https://finance.naver.com/item/sise.nhn?code=005930') # 웹사이트 데이터 수집하기
data = requests.get('https://flyturtlestudio.tistory.com/2609')
print(data.content) # url의 html 데이터 가져오기.
print(data.status_code) # 웹페이지 접속이 제대로 되었는지 확인하는 코드. 200이 뜨면 정상.

# 가져온 html = data.content 이기 때문에 
                    # vv 이 자리에 넣어줌.
soup = BeautifulSoup(samsung.content, 'html.parser')
## print(soup.find_all('태그명', 속성)) 찾은 결과물을 리스트 형태 안에 다 담아서 뱉어줌.



print('\n--- 삼성전자 ---')
print('현재가 = ', soup.find_all('strong', id="_nowVal")[0].text) # 뒤에 .text를 붙히면, 원하는 값만 뱉어줌.
print('거래량 = ', soup.find_all('span', id="_quant")[0].text)
print('전일대비 = ', soup.select('.rate_info .today .no_exday em span .blind').text)



lg = requests.get('https://finance.naver.com/item/sise.naver?code=066570')
soup = BeautifulSoup(lg.content, 'html.parser')
print('\n--- LG ---')
print('현재가 = ', soup.find_all('strong', id="_nowVal")[0].text)
print('거래량 = ', soup.find_all('span', class_="tah", id="_quant")[0].text)
print('등락률(%) = ', soup.find_all('span', class_="tah")[3].text) # 원본은 class="tah p11 nv01" 인데, class뒤에 _를 붙혀줘야하고, class_값이 여러개면 하나만 쓰면 됨.
# id 속성같은 경우는 유니크해서, html에 1개 밖에 없음. 반대로 class 속성은 ㅈㄴ 많음(중복가능). 그래서 리스트 불러오는 숫자에 값을 대입해서 찾아줘야 함.(인덱싱)
print(soup.find_all('em', class_="no_down")[0].text)
soup.find_all('태그명', class_="tah")
soup.select('.tah') # class는 . 
soup.select('#_nowVal') # id는 #
#soup.select 에서 태그명과 속성을 작성하는 법 vvvv
#soup.select('Strong#_nowVal') # 그냥 붙혀서 쓰면 됨.

#동일업종_등략률 = soup.select('.gray .f_down em')[0].text --> class="gray" 안에 class="f_down" 안에 있는 em 태그를 찾아주세요. (각각 사이에 공백은 내부 요소로 들어간다는 뜻.)

image = soup.select('.image-container img')[0]
print(image['src'])


#url에 있는 이미지 파일 가져올 때 vvvv
#urllib.request.urlretrieve(이미지URL, '파일명')
#urllib.request.urlretrieve('https://t1.daumcdn.net/cfile/tistory/9978C8335987D5060D', 'a.jpg')

SK하이닉스 = requests.get('https://finance.naver.com/item/sise.naver?code=000660')
soup = BeautifulSoup(SK하이닉스.content, 'html.parser')
print('\n--- SK하이닉스 ---')
print('현재가 = ', soup.find_all('strong', id="_nowVal")[0].text)
# print('거래량 = ', soup.find_all('span', class_="tah", id="_quant")[0].text)


# 현대차 = requests.get('https://finance.naver.com/item/sise.naver?code=005380')
# soup = BeautifulSoup(현대차.content, 'html.parser')
# print('\n--- 현대차 ---')
# print('현재가 = ', soup.find_all('strong', id="_nowVal")[0].text)
# print('거래량 = ', soup.find_all('span', class_="tah", id="_quant")[0].text)


# 기아 = requests.get('https://finance.naver.com/item/sise.naver?code=000270')
# soup = BeautifulSoup(기아.content, 'html.parser')
# print('\n--- 기아 ---')
# print('현재가 = ', soup.find_all('strong', id="_nowVal")[0].text)
# print('거래량 = ', soup.find_all('span', class_="tah", id="_quant")[0].text)


# POSCO홀딩스 = requests.get('https://finance.naver.com/item/sise.naver?code=005490')
# soup = BeautifulSoup(POSCO홀딩스.content, 'html.parser')
# print('\n--- POSCO홀딩스 ---')
# print('현재가 = ', soup.find_all('strong', id="_nowVal")[0].text)
# print('거래량 = ', soup.find_all('span', class_="tah", id="_quant")[0].text)


# NAVER = requests.get('https://finance.naver.com/item/sise.naver?code=035420')
# soup = BeautifulSoup(NAVER.content, 'html.parser')
# print('\n--- NAVER ---')
# print('현재가 = ', soup.find_all('strong', id="_nowVal")[0].text)
# print('거래량 = ', soup.find_all('span', class_="tah", id="_quant")[0].text)


# def 현재가(종목번호):
#     data = requests.get(f'https://finance.naver.com/item/sise.naver?code={종목번호}') # 글자 중간에 변수를 넣을 땐 f'글자{}' 형태로 감싸줘야 함.
#     soup = BeautifulSoup(data.content, 'html.parser')
#     print('현재가 = ', soup.find_all('strong', id="_nowVal")[0].text)
    # print('거래량 = ', soup.find_all('span', class_="tah", id="_quant")[0].text)


# 카카오 = requests.get('https://finance.naver.com/item/sise.naver?code=035720')
# soup = BeautifulSoup(카카오.content, 'html.parser')
# print('거래량 = ', soup.find_all('span', class_="tah", id="_quant")[0].text)
# print('\n--- 카카오 ---')
# print('현재가 = ', soup.find_all('strong', id="_nowVal")[0].text)

# 현재가('035720')

# file = open('a.txt', 'w')
# file.write(str(현재가('035720')))
# file.close


def 현재가(종목코드):
    data = requests.get(f'https://finance.naver.com/item/sise.naver?code={종목코드}') # 글자 중간에 변수를 넣을 땐 f'글자{}' 형태로 감싸줘야 함. # 그냥 미리 알리는 정도고 굳이 밑에 코드에서 사용할 필요는 없음.
    soup = BeautifulSoup(data.content, 'html.parser')
    return soup.find_all('strong', id="_nowVal")[0].text # 현재가 출력. 
# 함수 끝.

list = ['005930', '066575', '005380', '035720', '034220', '003490']

file = open('종목들.txt', 'w') # 왜 안 됐냐면, 파일을 6번 열 필요는 없잖아.

# for i in range(6): 
#     file.write(현재가(list[i]) + '\n')
for i in list:
    file.write(현재가(i) + '\n') # 이게 더 깔끔함.

file.close() # 마찬가지로 6번 닫을 필요도 없기 때문에 밖으로 빼는 게 맞지.

file = open('종목들.txt', 'r')
print(file.read())
file.close()