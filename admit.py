# import pandas as pd # 엑셀 같은 구조화된 데이터를 가져오고싶을 때 활용함. ####  pandas

# data = pd.read_csv('gpascore.csv', encoding='cp949')

# data = data.dropna() # 빈값이 있는 행을 제거해줌.
# # date = data.fillna(100) # 빈값을 입력한 값으로 채워줌.
# # print(data['gre'].count()) # .min() = 그 열의 최소값 출력, .max() = 그 열의 최대값 출력, .count() = 열의 총 갯수 출력.

# y데이터 = data['admit'].values # .values 를 붙히면 그 안에 있던 모든 값을 리스트로 만들어줌.

# x데이터 = []

# for i, rows in data.iterrows(): # date 라는 dateframe 을 가로 한 줄씩(행) 출력해줘.
#     x데이터.append([ rows['gre'], rows['gpa'], rows['rank'] ])
# import numpy as np
# import tensorflow as tf

# model = tf.keras.models.Sequential([
#     tf.keras.layers.Dense(64, activation='tanh'),
#     tf.keras.layers.Dense(128, activation='tanh'),
#     tf.keras.layers.Dense(1, activation='sigmoid'), # sigmoid는 0과 1사이의 값을 뱉어줌
# ])

# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# model.fit(np.array(x데이터), np.array(y데이터), epochs=1500)

# from keras.models import load_model
# model.save('학습모델.h5')


# exit()
import pandas as pd
data = pd.read_csv('gpascore.csv', encoding='cp949')

from keras.models import load_model
model = load_model('학습모델_0.8.h5')

## x데이터 예시 = [ [380,3.21,3], [660,3.67,3], [], [], [], [] ..... ] (리스트 안에 리스트 )
## y데이터 예시 = [ 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1 ...]

## 예측 # GRE 성적이 700이고 학점은 3.7입니다 Rank4 에 지원하고 싶은데, 합격 확률이 어떻게 되나요?
예측값 = model.predict([ [700, 3.7, 4], [800, 1.2, 1] ])
print(예측값)