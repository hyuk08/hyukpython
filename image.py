import tensorflow as tf

# import matplotlib.pyplot as plt # 이미지 띄워주는 라이브러리

(trainX, trainY), (testX, testY) = tf.keras.datasets.fashion_mnist.load_data()

# plt.imshow(trainX[3475])
# plt.gray() # 흑백으로 표시
# plt.colorbar() # 컬러바 ui 표시
# plt.show()  

class_names = ['T-shirt/top', 'Trouser', 'pullover', 'Dress',
     'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankleboot']

model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, input_shape=(28,28), activation="relu"),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10, activation="softmax") 
])
# sigmoid: 결과를 0~1로 압축, binary 예측문제에 사용, 마지막 노드 갯수는 1개. 
# softmax: 결과를 0~1로 압축, 카테고리 예측문제에 사용, 카테고리 항목을 다 더하면 1이 나옴. # tlqkf 존나 어렵네

model.summary()

model.compile(loss="sparse_categorical_crossentropy", optimizer='adam', metrics=['accuracy'])
model.fit(trainX, trainY, epochs=5)