# file = open('test.txt', 'w')
# file.write('Hello')
# file.close # 꼭 닫아줘야 함.

# file = open('test.txt', 'a')
# file.write(' world')
# file.close # 꼭 닫으세요.

# file = open('test.txt', 'r')
# print(file.read())
# file.close # 반드시 닫으세요.

# csv_file = open('data.csv', 'w')
# csv_file.write('고등학교 3학년, 영어, 100\n고등학교 3학년, 수학, 100\n고등학교 2학년, 영어, 80\n고등학교 2학년, 수학, 90')
# csv_file.close

# csv_file = open('data.csv', 'r')
# print(csv_file.read())
# csv_file.close

# file = open('list.txt' , 'w')
# file.write('삼성전자 \n카카오 \n네이버 \n신풍제약')
# file.close


# for A in range(2, 10):
#     print('------',A,'단','------')
#     for B in range(1, 10):
#         print(A * B)

# # for 문 안에 for 문
# for i in range(3):
#     print('--', '--')
#     for i in range(10):
#         print('320d 사세요!!!!')

# 원하는 모양 
# *
# * *
# * * *
# * * * *
# * * * * *
# for i in range(5):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()


list = ['삼성전자', '카카오', '네이버', '신풍제약']
# for i in list: # range 대신 list 를 넣을 수 있음. 넣으면 리스트 안 값 만큼 반복되고, i 는 1, 2, 3, 4, 5 가 아니라 리스트 속 하나의 값이 됨.
#     print(i)

file = open('list.txt', 'w')
for i in range(4):
    file.write(list[i] + '\n')
file.close

# 이렇게 할 필요가 없다는 거
# file = open('list.txt', 'w')
# file.write(list[0] + '\n')
# file.write(list[1] + '\n')
# file.write(list[2] + '\n')
# file.write(list[3] + '\n')
# file.close


# 구구단 만들어봅시다


for j in range(2, 10):
    for i in range(1, 10):
        print(j,'x', i,'=', j*i)

exit()
for a in range(2, 10):
    for b in range(1, 10):
        print(a, 'x', b, '=', t)