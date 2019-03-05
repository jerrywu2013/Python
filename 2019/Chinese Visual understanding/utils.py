#導入函式庫
import skimage
import skimage.io
import skimage.transform
import numpy as np

#將txt檔中的文字擷取下來
synset = [l.strip() for l in open('synset.txt').readlines()]


def load_image(path):
  #讀取資料
  img = skimage.io.imread(path)
  img = img / 255.0
  #使用all函式判斷image是否符合格式
  assert (0 <= img).all() and (img <= 1.0).all()
  
  # 裁剪圖片
  short_edge = min(img.shape[:2])
  #裁減y方向
  yy = int((img.shape[0] - short_edge) / 2)
  #裁減x方向
  xx = int((img.shape[1] - short_edge) / 2)
  #得到裁剪後圖片
  crop_img = img[yy : yy + short_edge, xx : xx + short_edge]
  #重設尺寸為224*224
  resized_img = skimage.transform.resize(crop_img, (224, 224))
  return resized_img


def print_prob(prob):
  
  print ("prob shape", prob.shape)
  #將預測機率由大排到小
  pred = np.argsort(prob)[::-1]

  #得到預測第一結果
  top1 = synset[pred[0]]
  print ("預測結果： ", top1)
  # 取得預測前五名結果
  top5 = [synset[pred[i]] for i in range(5)]
  print ("預測結果Top5: ", top5)
  return top1
