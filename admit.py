






import tensorflow as tf

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'), # sigmoid는 0과 1사이의 값을 뱉어줌
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(x데이터, y데이터, epochs=10)

# x데이터 예시 = [ [380,3.21,3], [660,3.67,3], [], [], [], [] ..... ] (리스트 안에 리스트 )
# y데이터 예시 = [ 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1 ...]