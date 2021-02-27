from urllib.request import urlopen
from io import StringIO
import pandas as pd

# Web上のデータを読み込む
data = urlopen("https://www.e-stat.go.jp/stat-search/file-download?statInfId=000031524030&fileKind=1").read().decode('MS932')
df = pd.read_csv(StringIO(data), encoding='MS932')

# DataFrameの先頭5行分を表示する
df.head()
