# for i in range(1, 31, 10): # 10은 step값이구나. 아하! 1부터 30까지니까 10씩 띄우면, 1, 11, 21이 되겠제?
#     print(f'{i}번은 {i}번부터 {i+9}번까지 모아줘.')

# my_var = '123'
# for i in my_var:
#     print(i)

drama = ['시즌1', '시즌2', '시즌3', '시즌4', '시즌5']
for i in drama:
    if i == '시즌4': #어떠한 조건이 참일 때, 반복문을 탈출할 수 있음.
        print('노잼!!!!!!!!!')
        break
    print(f'{i} 시청')

