# TPUとの接続(TensorFlow)とTensorFlowのバージョン確認
%tensorflow_version 2.x
import tensorflow as tf
print("Tensorflow version " + tf.__version__)

# TPU関連のエラー出力抑制
import logging
tf.get_logger().setLevel(logging.ERROR) 

try: 
  # TPU検出
  tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
  print('TPU起動 ', tpu.cluster_spec().as_dict()['worker'])

except ValueError:
  raise BaseException('ERROR: TPU接続エラー')

# TPU接続と初期化
tf.config.experimental_connect_to_cluster(tpu)
tf.tpu.experimental.initialize_tpu_system(tpu)
tpu_strategy = tf.distribute.TPUStrategy(tpu)
