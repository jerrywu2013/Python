#導入函式庫
import tensorflow as tf
import utils
import pandas

#以二進位讀模式打開打開預先訓練完成的的model
with open("vgg16.tfmodel", mode='rb') as f:
  fileContent = f.read()

#創建一個GrphDef圖形化流程結構
graph_def = tf.GraphDef()
#將模型導出單個文件定義權重
graph_def.ParseFromString(fileContent)

#輸入圖片長,寬,rgb
images = tf.placeholder("float", [None, 224, 224, 3])
#將graph_def圖導入到python中
tf.import_graph_def(graph_def, input_map={ "images": images })
print ("graph loaded from disk")

#返回當前默認圖
graph = tf.get_default_graph()

#上傳圖片功能
cat = utils.load_image("Common-dog-behaviors-explained.jpg")

#使用session初始化所有變數
with tf.Session() as sess:
  init = tf.initialize_all_variables()
  sess.run(init)
  print ("variables initialized")
  #將我們輸入的圖片重新設定尺寸成(圖片數目,224,224,rgb)形式圖片
  batch = cat.reshape((1, 224, 224, 3))
  #用assert判斷輸入格式是否為正確格式
  assert batch.shape == (1, 224, 224, 3)
  #用來來傳入image的tensor
  feed_dict = { images: batch }
  #根據名稱返回tensor的數據
  prob_tensor = graph.get_tensor_by_name("import/prob:0")
  #將輸入圖片和模型進行預測
  prob = sess.run(prob_tensor, feed_dict=feed_dict)
#輸出預測的結果
utils.print_prob(prob[0])


