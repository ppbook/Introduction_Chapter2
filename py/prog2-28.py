# 日本語環境の構築
!pip install japanize-matplotlib

# matplotlibのインポート（pyplotをpltとして使用）
import matplotlib.pyplot as plt 

# 日本語表示への対応
import japanize_matplotlib  # 日本語化matplotlib
import seaborn as sns       # Matplotlibラッパ
sns.set(font="IPAexGothic") # 日本語フォント設定

# データの用意
x  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y1 = [1, 3, 5, 3, 1, 4, 2, 4, 1]
y2 = [2, 6, 6, 6, 2, 6, 6, 6, 2]

# グラフのプロット
plt.plot(x, y1, ls='-', marker='s', label="ライン：低")
plt.plot(x, y2, ls='-.', marker='o', label="ライン：高")

# 軸ラベルなどの設定
plt.xlabel("横軸")        # 横軸ラベル
plt.ylabel("縦軸")        # 縦軸ラベル
plt.title("線グラフ")     # グラフタイトル
plt.legend()              # 凡例表示

# グラフの描画（ファイル、画面）
plt.savefig("graph.png")  # ファイルに保存
plt.show()                # 画面にグラフ描画
