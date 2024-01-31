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
absent = [2, 5] # 결석
for student in range(1, 11):
    if student in absent: # 만약 absent 값이 student 에 있다면, 다음 print 구문으로 넘어가지 않고, 윗 구문을 반복함.
        continue
    print("{0}번 학생, 58p 읽어보세요.".format(student)) 

입력이 됐나?

됐다 됐어.