# pandas APIのインポート
import pandas as pd

# pandas Seriesの作成
insect_names = pd.Series(['みみず', 'おけら', 'あめんぼ'])
numbers = pd.Series([100, 150, 175])

# pandas DataFrameの作成
pd.DataFrame({ '昆虫名': insect_names,\
              '数': numbers })

# 各種情報表示
print(insects['昆虫名'][1])     # 要素へのアクセス
print(insects.info())           # 情報表示

# DataFrameの操作
insects['足の数']=[0, 6, 6]     # 列の追加
insects.loc[3]=['とんぼ', 50]   # 行の追加

# ランタイム上のファイル(CSV)の読み込み
df = pd.read_csv('/content/c02.csv',encoding='MS932')
