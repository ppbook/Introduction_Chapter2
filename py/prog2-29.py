# モジュールインポート
import tensorflow as tf

# TensorFlow内のKerasのdatasetsを用いて
# mnistデータセットをダウンロード
mnist = tf.keras.datasets.mnist

# mnistデータをload_data()関数を用いてロード
# 学習データとテストデータに分ける
# その後、データを正規化している
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# TensorFlow.kearsを用いてモデルを定義
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2), 
  tf.keras.layers.Dense(10, activation='softmax')
])

# モデルの学習設定
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

# モデルの学習
model.fit(x_train, y_train, epochs=5)

# モデルの評価
model.evaluate(x_test, y_test)
