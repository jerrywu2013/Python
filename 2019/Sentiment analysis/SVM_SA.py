# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 11:00:22 2017

@author: user
"""

import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import StratifiedKFold
from sklearn.externals import joblib

data = np.load('data.npy')

n_sar = 3554
sar = 374
# total  3928
label_0 = np.repeat(0, n_sar) #not sarcasm
label_1 = np.repeat(1, sar) #sarcasm
train_label = np.append(label_0, label_1)

"""shuffle"""
np.random.seed(10)
shuffle_num = np.random.choice(range(1,n_sar+sar),n_sar+sar)
data = data[shuffle_num,]
data_label = train_label[shuffle_num,]

"""use the last 3000 examples as validation data, you may use random split"""
test = data[3000:]
test_label = data_label[3000:]
train = data[:3000]
train_label = data_label[:3000]

import csv
f = open('data.csv','w')
writer = csv.writer(f, lineterminator="\n")
writer.writerow(data)
f.close()
f = open('label.csv','w')
writer = csv.writer(f, lineterminator="\n")
writer.writerow(data_label)
f.close()

"""generate a SVM classifier"""
classifier = svm.SVC()

"""train cross validation"""
valid_score = []
kfold = StratifiedKFold(n_splits=5, shuffle=False,  random_state=1)
count = 0
for train_index,valid_index in kfold.split(np.array([0]*3000),np.array([0]*3000)):
    print('<<<<<COUNT>>>>> '+str(count))
    classifier.fit(train[train_index],train_label[train_index])
    
    predicted = classifier.predict(train[valid_index])
    confus = metrics.confusion_matrix(train_label[valid_index], predicted)
    acc = (confus[0][0]+confus[1][1])/sum(sum(confus))    
    valid_score.extend([acc])
    count = count+1
print("valid: %.2f%% (+/- %.2f%%)" % (np.mean(valid_score), np.std(valid_score)))
# train model, classifier.fit(資料:data numberxdata size, 分類目標:data numberxlabel size)

"""test model"""
expected = test_label
predicted = classifier.predict(test)
confus = metrics.confusion_matrix(expected, predicted)
acc = (confus[0][0]+confus[1][1])/sum(sum(confus))
print('acc = '+str(acc))

"""save model"""
joblib.dump(classifier, 'SVM_model.pkl')
