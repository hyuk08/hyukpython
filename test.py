# 파이썬 할당연산자
# = 왼쪽 변수에 오른쪽 값을 할당한다. ex) a = b 는 a = b 를 의미함.
# += 왼쪽 변수에 오른쪽 값을 더하고 그 결과를 왼쪽 변수에 할당한다. ex) a += b 는 a = a+b 를 의미함.
# -= 왼쪽 변수에 오른쪽 값을 빼고 그 결과를 왼쪽 변수에 할당한다. ex) a -= b 는 a = a-b 를 의미함.
# *= 왼쪽 변수에 오른쪽 값을 곱하고 그 결과를 왼쪽 변수에 할당한다. ex) a *= b 는 a = a*b 를 의미함.
# /= 왼쪽 변수에 오른쪽 값을 나누고 그 결과를 왼쪽 변수에 할당한다. ex) a /= b 는 a = a/b 를 의미함.
# %/ 왼쪽 변수에 오른쪽 값을 나눈 후 그 '나머지'를 왼쪽 변수에 할당한다. ex) a %/ b 는 a = a%b 를 의미함.
# //= 왼쪽 변수에 오른쪽 값을 나눈 후 그 몫을 왼쪽 변수에 할당한다. ex) a //= b 는 a = a//b를 의미함.
# **= 왼쪽 변수에 오른쪽 값을 제곱하고 그 결과를 왼쪽 변수에 할당한다. ex) a **= b 는 a = a**b 를 의미함.


# animal = "강아지"
# name = "구름"
# hobby = "산책"
# age = 8
# is_adult = age > 4

# print("저희 집 " + animal + " 이름은 " + name + "이고 " + hobby + "을 아주 좋아해요.")
# print(name + "이는 " + str(age) + "살이에요, 어른일까요? " + str(is_adult))
# 정수형 앞이나 불리안 앞은 str을 붙혀줘야 함.

# 정보 출력
# 입력값 vvv
# name = "한승혁"
# age = 23
# Education = "고등학교 졸업"

# print("이름 : ", name, "나이 : ", age, "최종학력 : ", Education)


# != 는 같지 않는 걸 True 로 출력. ex) print(1 != 3) -> True, print(3 != 3) -> False.
# == 는 같은 걸 True 로 출력. ex) print(2 == 2) -> True, print(1 == 2) -> False.

# # 두 값 중 하나라도 틀리면 False를 출력하는 and 불리언 (& 로도 쓸 수 있음.)
# print((3 < 4) and (1 > 0))
# print((3 < 4) and (1 < 0))

# # 두 값 중 하나라도 맞으면 True를 출력하는 or 불리언 (| 로도 쓸 수 있음.)
# print((3 < 4) or (1 < 0))
# print((3 < 4) | (1 < 0))

# from random import *
# print(random()) # 0.0 ~ 1.0 사이의 임의의 값 생성.
# print(int(random() * 10)) # 0.0 ~ 10.0 사이의 임의의 값 생성. int를 붙히면 소수점 없이 정수만 값만 생성.
# print(randrange(1, 10)) # 1 ~ 10 미만의 임의의 값 생성.
# print(randrange(1, 45)) # 1 ~ 45 미만의 임의의 값 생성.
# print(randint(1, 45)) # 1과 45를 포함하는 랜덤 값 생성.

# quiz
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")

# sentence = '''저는 한승혁이라고 하고,
# 파이썬이 쉽다고 해서
# 공부하는 중입니다. 코딩은 완전 처음이에요.'''
# print(sentence)

# jumin = "020824-3155314"
# print("성별 : " + jumin[7])
# print("생년월일 : " + jumin[0:6])
# print("뒷 7자리 : " + jumin[-7:])

# python = "python is amazing."
# print(age.replace("python", "java"))

# age = 23
# color = "카키"
# print("저는 " + str(age) + "살이고, " + color + "색을 좋아합니다.")

# print("저는 {age}살이고, {color}색을 좋아합니다.".format(age = "23", color = "카키")) # 변수처럼 지정 가능.
# print("저는 {1}살이고, {0}색을 좋아합니다.".format("카키", "23")) # format 괄호 안 입력된 순서대로 출력 가능.

# \n == 줄바꿈.
# print("백문이 불여일견,\n백견이 불여일타.")
# print("저는 \"한승혁\" 입니다") # 따옴표 뒤 역슬래쉬는 문장 안에서 따옴표를 사용할 수 있게 해줌.

# quiz
# ex) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 . 뒤에 부분은 모두 제외.
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + ! 로 구성.
#                 nav             5             1         !
# url = "http:///naver.com"
# my_str = url.replace("http://", "") # 규칙 1 성공. http:// 를 아예 입력이 없는 것으로 replace.
# my_str = my_str[:my_str.index(".")] # 규칙 2 성공. 처음부터, my_str에 있는 "." 직전까지만 출력. -> my_str.index(".")
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# #규칙 3 성공. my_str(naver)에 처음부터 3번째 직전까지(nav),
# #글자 갯수를 세야 하니까, len을 활용해서 my_str의 글자 갯수 출력 + .count("e")를 활용하여 e의 갯수 카운트 + ! len(my_str)과 my_str.count("e") 모두 정수형이기 때문에, str 붙임.
# print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))


## 5-1 리스트
# subway = ["한승혁", "강지호", "최용빈"]
# #           0        1       2
# print(subway.index("최용빈")) # 리스트 몇 번째에 들어가 있는지 찾을 수 있음.

# # 다음 정류장에서 김현민이 탐.
# subway.append("김현민") # append 는 맨 뒤에 추가.
# print(subway)

# # 전지호를 한승혁과 강지호 사이에 넣기.
# subway.insert(1, "전지호") # insert 이후 어디에 넣을 건지 지정 후 입력.
# print(subway)

# 한 명씩 뒤에서 꺼냄. (추출)
# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인
# print(subway.count("한승혁"))

# # 정렬 기능
# num_list = [4, 1, 2, 7, 6]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기
# num_list.reverse()
# print(num_list)

# #모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용 가능.
# mix_list = ["한승혁", 20, 5 < 10]
# print(mix_list)

# # 리스트 두 개 병합 가능.
# num_list = [66, 132, 12]
# num_list.extend(mix_list)
# print(num_list)


## 5-2 사전
# cabinet = {3:"한승혁", 100:"강지호"}
# print(cabinet.get(3))
# print(cabinet.get(100)) # .get에 괄호로 가져올 때, 그 값이 없는 값이라면 None 이라고 표시됨과 동시에 프로그램이 계속 진행 됨.
# # print(cabinet[3]) # .get 없이 대괄호로 값을 불러올 때, 그 값이 없다면 오류가 나면서 프로그램이 끝나버림. (둘 차이는 프로그램이 끝나느냐, 계속 진행되느냐 차이.)
# print(cabinet.get(1, "사용 가능합니다.")) # .get 이후 값이 있다면 그 값을 불러오지만, 없을 경우 쉼표 뒤 입력값을 출력함.(없으면 None)
# print(3 in cabinet) # 키가 캐비넷에 있는지 확인할 수 있음. 있으면 True 없으면 False
# cabinet = {"A-1":"한승혁", "A-2":"강지호"} # 문자열로도 가능.
# print(cabinet.get("A-1"))
# cabinet["A-3"] = "전지호" # 추가 (중복 시 추가한 값 출력.)
# print(cabinet)
# del cabinet["A-3"] # del 을 통한 제거.
# print(cabinet)
# print(cabinet.keys()) # key들만 출력.
# print(cabinet.values()) # values 만 출력.
# print(cabinet.items()) # key, value 쌍으로 출력.
# cabinet.clear() # 전체 삭제.
# print(cabinet)


## 튜플
# menu = ("돈까스", "치즈까스")
# print(menu[0]) # 정해진 값 이외의 추가를 한다거나 특정한 명령 불가.


## 집합(set) , 중복 안 됨, 순서 없음.
# my_set = {1,1,1,1,1,2,3}
# print(my_set)

# python = {"한승혁", "강지호", "전지호"}
# java = {"강지호", "전지호"}
# # 교집합 (파이썬 자바 둘 다 할 수 있는 개발자.)
# print(python & java)

# # 합집합 (파이썬을 할 수 있거나 자바를 할 수 있는 개발자. 사실상 전부)
# print(python | java)

# # 차집합 (파이썬을 할 줄 알지만 자바는 못하는 개발자.)
# print(python - java)

# # 추가
# python.add("최용빈")
# print(python)

# # 제거
# python.remove("최용빈")
# print(python)


## 5-5 자료구조의 변경
# menu = {"딸기", "커피", "우유"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu)) # list로 감싸주면 list로 변경 가능.

# menu = tuple(menu) # tuple로 감싸주면 마찬가지로 변경 가능.
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))


# quiz
# from random import *

# users = range(1, 21)
# users = list(users)
# print(users)
# shuffle(users)
# print(users)

# winners = sample(users, 4)
# print(" -- 당첨자 발표 --")
# print("치킨 당첨자 {0}".format(winners[0]))
# print("커피 당첨자 {0}".format(winners[1:]))
# print(" -- 축하합니다 --")


## if     # if elif else.

# weater = "비"
# if weater == "비":
#     print("우산을 챙기세요.")
# elif weater == "미세먼지":
#     print("마스크를 챙기세요")
# else:
# #     print("준비물이 필요없습니다.")

# weater = input("오늘 날씨는 어떤가요?(비, 눈, 안개, 맑음 중 선택.) ")
# if weater == "비":
#     print("오늘은 우산을 꼭 챙기세요.")
# elif weater == "눈":
#     print("눈길이 미끄러우니 운전 조심하시고 고속도로 및 자유로에서 20% 감속운전하세요.")
# elif weater == "안개":
#     print("안개 지대 진입 시 깜빡이 릴레이! 자유로에서 20% 감속 운전하세요.")
# else:
#     print("준비할 거 없는 가벼운 아침이네요. 조심히 다녀오세요.")

# temp = int(input("오늘 기온은 몇 도 인가요? 숫자만 입력. "))
# if temp <= 0:
#     print("물이 어는 수준입니다. 미끄럼 주의하세요.")
# elif temp >= 0 and temp <= 10:
#     print("많이 춥습니다. 외투를 챙기세요.")
# elif temp >= 10 and temp <= 20:
#     print("낮엔 덥지만 아침과 저녁이 쌀쌀해요. 겉옷을 챙기세요.")
# elif temp >= 20 and temp <= 30:
#     print("많이 덥습니다. 썬크림을 바르시고, 야외활동은 자제하세요.")
# elif temp >= 30 and temp <= 40:
#     print("밖이 끓는 수준입니다. 되도록이면 실내에 계십시오.")
# elif temp >= 40 and temp <= 100:
#     print("살이 익는 수준의 온도입니다. 절대 나가지 마세요. 무언가 잘못됐습니다. 경고!경고!경고!")
# else:
#     print("잘못된 입력입니다.")
# elif 0 <= temp <= 10: 같이 end 없이도 사용 가능.


## for # 반복문.
# starbucks = ["한승혁", "강지호", "전지호", "최용빈"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))


# while
# customer = "한승혁"
# index = 5
# while index >= 0: # index가 0보다 크거나 같을 때 까지 밑에 구문을 반복.
#     print("{0}님, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
#     index -= 1 # index = index - 1
#     if index == -1:
#         print("{0}님 커피가 폐기처분되었습니다.".format(customer))

# while life >= 0:
#     print("체력이 {0}칸 남았습니다.".format(life))
# life = 5
# attack = input("공격하시겠습니까? (y or n 을 입력하세요.) ")
# if attack == "y":
#     print("공격에 성공하셨습니다. 적 남은 체력 {0}".format(life))
#     life -= 1
# elif attack == "n":
#     print("공격하지 않습니다. 다음 턴.")
# elif life == 0:
#     print("적이 죽었습니다. you win!")
# else:
#     print("잘못된 입력입니다.")

# 한승혁이 올 때 까지 커피가 준비되었다는 걸 알려주고, 앞에 온 사람한테 이름을 묻는 걸 만들어보자.
# customer = "한승혁"
# person = "Unknown"

# while person != customer: # person이 customer가 아닐 때, 계속 반복.
#     print("{0}님, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")


## continue 와 break
# absent = [2, 5] # 결석
# no_book = [7] # 책을 깜빡함
# for student in range(1, 11):
#     if student in absent: # 만약 absent 값이 student 에 있다면,
#         continue # 다음 print 구문으로 넘어가지 않고, 윗 구문을 반복함.
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}번, 교무실로 따라와.".format(student))
#         break # break를 만나면 바로 반복문 탈출.
#     print("{0}번 학생, 58p 읽어보세요.".format(student))


## 한 줄 for문

# 출석번호 1, 2, 3, 4 앞에 100씩 더하기로함. -> 101, 102, 103, 104
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# quiz
# 당신은 Cocoa 서비스를 이용하는 택시 기사입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객수를 구하는 프로그램을 작성하시오.

# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해짐.
# 조건 2 : 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 함.

# (출력문 예제)
# [o] 1번째 손님 (소요시간 : 15분)
# [o] 2번째 손님 (소요시간 : 50분)
# [o] 3번째 손님 (소요시간 : 5분)
# ...
# [o] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2명


## 함수

# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): # 출금
#     if balance >= money: # 출금액이 잔액보다 적으면, 출금 가능.
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금에 실패하였습니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money): # 저녁에 출금
#     commission = 100 # 수수료
#     return commission, balance - money - commission


# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("출금이 완료되었습니다. 수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))


# 함수 기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}"\
#           .format(name, age, main_lang)) # 역슬래쉬 후 엔터는 밑 문장까지 하나로 처리하겠다는 뜻.
# profile("한승혁", 23, "python")
# profile("강지호", 23, "Js")
# profile("전지호", 23, "Java")

# 중복되는 값을 반복하여 작성할 필요 없이 기본값으로 만들어 줄 수 있음.
# def profile(name, age=23, main_lang="python"): # 변수 뒤 '=' 과 값을 붙혀줌으로써 기본값 생성.
#     print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}".format(name, age, main_lang))
# profile("한승혁")
# profile("전지호")
# profile("강지호")


# 키워드 값 # 처음 순서를 지정해두면, 어떤 순서로 프로필을 작성하던지간에, 처음 순서대로 출력됨.
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="한승혁", main_lang="python", age=23)
# profile(main_lang="Js", name="강지호", age=23)

# 가변인자 # 서로 다른 갯수의 값을 넣어줄 때 사용.
# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("강지호", 23, "python", "Java", "Javascript", "C++", "C#")
# profile("한승혁", 23, "python")


# 지역변수와 전역변수 # 스크래치에서 사용했던 이 스프라이트에서만 사용 체크박스와 같은 개념.
# gun = 10
# def checkpoint(soldiers): # 경계근무
#     global gun # 전역 공간에 있는 gun 변수 사용.
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun)) # 전체 총 갯수
# checkpoint(2) # 2명이 경계근무 나감.
# print("남은 총 : {0}".format(gun)) # 남은 총 갯수

# quiz # 키와 몸무게, 성별을 입력하면 그에 따른 표준 체중을 알려주는 프로그램.
# height = 168
# gender = "남자"

# def std_wight(height, gender): # 키는 미터 단위 (실수), 성별 "남자" / "여자"
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 168 # cm
# gender = "남자"
# weight = round(std_wight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


## 표준 입출력

# print("python", "java", "javascript", sep=" vs ") # sep="(이 사이에 있는 값이 곧 앞에 입력한 값들 사이를 구분해주는 입력값이 됨.)"

# print("python", "java", sep=" vs ", end=" ") # end="(공백 안에 값을 넣으면 그 값을 마지막으로 입력하고 구문이 출력 됨. 다음 글을 연장해서 출력하는 것으로도 사용할 수 있음.)"
# print("마참내!")

# scores = {"한국":2, "일본":1, "홍콩":1}
# for country, scores in scores.items():
#     print(country.ljust(4), str(scores).rjust(4), sep=":") #ljust , rjust = 왼쪽 정렬, 오른쪽 정렬. 괄호 안 값은 확보할 공간을 의미함.

# .zfill
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) # 3의 공간을 확보하는데, 나머지 없는 숫자는 0으로 채워줘라.

# answer = input("아무 값이나 입력하세요. ") # 사용자 입력을 통해서 값을 받게 되면, 항상 문자열로 받게 됨 (str)
# print("입력하신 값은 " + answer + " 입니다.")
# print(type(answer))


## 다양한 출력 포멧
# 빈 자리는 그냥 두고, 오른쪽 정렬을 하는데, 10칸을 확보하고 배치해라.
# print("{0: >10}".format(500))
# # 500은 오른쪽에 10칸 확보, 1은 왼쪽에 10칸 확보. 그 사이 콤마.
# print("{0: <10},{1: >10}".format(500, 1))
# # 값 앞에 양수 음수 표시하기 (+추가)
# print("{0: <+10}".format(-500))
# # 3자리마다 콤마 찍기.
# print("{0:,}".format(100000000000))
# # 3자리마다 콤마 찍고, + - 도 붙이기.
# print("{0:+,}".format(-100000000000))
# # 3자리마다 콤마 찍고, + - 도 붙이기. 자릿수도 확보하고, 돈이 많으면 기분이 좋으니까 빈칸은 ^로 채우기.
# print("{0:^<+30,}".format(10000000000))
# # 소수점 출력하기 인데, f 앞 .a를 붙이면, 소수점 a+1번째 자리에서 반올림 해라. 라는 뜻이 됨
# print("{0:.2f}".format(5/3))


## 파일 입출력 # w = 쓰기 (덮어쓰기), a = 이어쓰기, r = 읽기
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 100", file=score_file)
# print("영어 : 100", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 100")
# score_file.write("\n코딩 : 100") # .write 사용 시 자동으로 줄바꿈이 되지 않음. \n을 통한 줄바꿈.
# score_file.close()

# # 파일 읽기 # "r"
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서를 다음 줄로 이동.
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 몇 줄 인지 모를 때.
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# # 또다른 방법.
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()


## pickle
# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"한승혁", "나이":23, "취미":["Blender", "UE5", "python"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile 에 있는 정보를 file 에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기.
# print(profile)
# profile_file.close()


## with
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬 공부중...")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())


##############

# # 버튼 누르면 시간 표시되는 프로그램.
# from tkinter import *
# from datetime import datetime
# win = Tk() # 창 생성

# win.geometry("600x100")
# win.title("What time ?")
# win.option_add("*Font", "바탕체 20")

# btn = Button(win) #btn 이라는 변수에 버튼을 만드는 함수 Button를 작성하고 괄호 안에 버튼을 넣을 창을 지정(win).
# # btn = Button(win, text ="현재 시각", width = 20, height = 20) # 이렇게 Button 함수 안에 작성해도 되지만, 가독성을 위해 밖으로 뺌.
# btn.config(text = "버튼을 누르면 현재 시간이 표시됩니다.") # 버튼에 텍스트 넣기.
# btn.config(width = 40, height = 5) # 버튼 크기 지정. (px)

# def what_time():
#    dnow = datetime.now()
#    btn.config(text = dnow)
# btn.config(command = what_time)

# btn.pack()
# win.mainloop() # 창 실행

###############


###############

# 로또번호 입력 받아서 당첨 번호 확인하기.

# from tkinter import *

# win = Tk()
# win.geometry("300x100")
# win.title("test")
# win.option_add("*Font", "바탕체 20")

# ent = Entry(win)
# ent.pack()


# def ent_p():
#     a = ent.get()
#     print(a)  # ent_p(): 를 입력시 a를 출력하는데, a = ent.get()


# btn = Button(win)
# btn.config(text="로또 당첨 번호 확인")
# btn.config(command=ent_p)
# btn.pack()

# win.mainloop()


# 함수 정리
# def 모자(구멍):
#     print(구멍 + 1)

# 모자(1)
# 모자(2)

# def 함수():
#     return 10 # 함수를 실행하고 나서 10을 남겨라? 함수 실행하고 나서 가죽을 남기고 싶을 때.

# 함수()




# ## 딥러닝 # tensor
# import tensorflow as tf

# # tensor = tf.constant( [3, 4, 5] )
# tensor2 = tf.constant( [ [1,2],
#                          [3,4] ] )     
# tensor3 = tf.constant( [ [5,6],  
#                          [7,8] ] ) # 행렬곱 # matmul    
# # 출력되는 dtype -> 정수는 int, 실수는 float 로 출력 됨.

# print(tf.matmul(tensor2, tensor3))

# tensor4 = tf.zeros([2,2,3])  # tensor shape #무슨 뜻이냐면, 뒤에서부터 해석하면 됨. 0이 3개 담긴 2개 행렬을 생성하는데 그걸 또 2개로 만들어줘라. 라는 뜻.
# print(tensor4)

# print(tensor2.shape) # shape 출력 방법. 텐서2는 (2,2)

# # tf.Variable() # 딥러닝의 weight 값이라고 생각해도 됨. 웨이트 같은 건 Variable로 만들어야 함.
# w = tf.Variable(1.0)
# print(w)


import tensorflow as tf

# 키를 통해 신발 사이즈를 예측
# y = ax + b
# 신발 = 키 * a + b

키 = 170
신발사이즈 = 260

a = tf.Variable(0.1)
b = tf.Variable(0.2)

def 손실함수():
    예측값 = 키 * a + b
    return tf.square(신발사이즈 - 예측값)
    # 실제값 - 예측값 뱉기(즉 오차). 마이너스로 치닿는 걸 막기 위해 제곱으로 계산함. 그게 -> tf.square

opt = tf.keras.optimizers.Adam(learning_rate=0.1)

resultA = 0
resultB = 0


for i in range(300):
    opt.minimize(손실함수, var_list=[a, b])
    print(a.numpy(), b.numpy())
    
    if i==299:
        resultA = a.numpy()
        resultB = b.numpy()
    # (a, b) 로 작성해도 되는데, 보기 불편해서 .numpy() 로 값만 출력하게 바꿔줌.

print('result : ', (키 * resultA + resultB))