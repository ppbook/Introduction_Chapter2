# モジュールインポート
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

# 学習用データ準備
iris = datasets.load_iris()   # irisデータセットの読み込み
print(iris.DESCR)             # データセットの説明表示

# モデル設定と学習
model = svm.LinearSVC()           # モデル用意・設定
model.fit(iris.data, iris.target) # モデルの学習

# 学習済みモデルを用いて推論
# 入力：ガクの長さ、ガクの幅、花弁の長さ、花弁の幅
model.predict([[ 6.0,  4.0,  6.0,  1.0]])
