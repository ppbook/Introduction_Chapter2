# Pythonのバージョン確認コマンド
!python -V

# 導入済みライブラリのバージョン確認コマンド
!pip list

# grepコマンドへのパイプにより表示内容を制御する例
!pip list | grep -e numpy -e "^pandas " -e pandas-profiling -e scikit-learn -e "^matplotlib " -e "^tensorflow " -e "^Keras "
