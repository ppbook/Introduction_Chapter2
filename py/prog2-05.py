from google.colab import files

with open('test04.txt', 'w') as f:
  f.write('ファイルの内容（ダミーテキスト）')

files.download('test04.txt')
