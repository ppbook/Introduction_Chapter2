import numpy as np  # NumPy を np という名前でインポート

a = np.array([1, 2, 3, 4])  # NumPy配列の作成
p_list = a.tolist()         # list型に変換

# 各種データ表示
print(a)            # [1 2 3 4]
print(type(a))      # <class 'numpy.ndarray'>
print(a.shape)      # (4,)
print(a[0])         # 行列の0番目の要素

b = np.array([5, 6, 7, 8])

# 各種計算
print(a+b)    # 各要素の足し算 [6, 8, 10, 12]
print(a*10)   # 各要素のアダマール積 [10, 20, 30, 40]
print(a<3)    # 各要素の条件判定結果のTrue False

print(np.dot(a, b))  # 行列の積

np.zeros((2,4), int) # すべて0の行列
np.eye(10)           # 単位行列（正方行列）

np.save('filename.npy', e)  # ファイルの保存
f = np.load('filename.npy') # ファイルの読み込み
