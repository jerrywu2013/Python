import theano as th
from keras.models import Model
from keras.layers import Dense, Dropout, Flatten, merge, Input, advanced_activations
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.utils import np_utils
from keras.regularizers import l1l2, activity_l2, l2, l1
from keras.optimizers import SGD, Adadelta, Adam
from keras.utils import np_utils
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.layers.normalization import BatchNormalization
from keras.callbacks import EarlyStopping
from sklearn.model_selection import StratifiedKFold


train = np.load('/home/someone/irony/data.npy')

"""
for i in range (0,1500):
    train[i] = np.array(train[i]).astype(float)
   
t=[]
for l in train:
    t.append(len(l))
    if len(l) != 59:
        print(train.index(l))

print('max:'+str(max(t)))
""" 

'''
first number-->0 not irony, 1 irony 
second number-->all sentence score
0~1186 1187~1499
'''
n_sar = 3554
sar = 374
# total  3928
label_0 = np.repeat(0, n_sar) #not sarcasm
label_1 = np.repeat(1, sar) #sarcasm
train_label = np.append(label_0, label_1)


# resize shape to see the shape
train = np.resize(train, (n_sar+sar, 1, 121, 1)) # 1500 sentences, 1, vector size 121, 1
train.shape
train_label.shape

#shuffle
np.random.seed(10)
shuffle_num = np.random.choice(range(1,n_sar+sar),n_sar+sar)
train = train[shuffle_num,:,:,:]
train_label = train_label[shuffle_num,]

# use the last 1200 examples as validation data, you may use random split                         
# total 3928, train 3000
test = train[3000:, :, :, :]
test_label = train_label[3000:]
train = train[:3000, :, :, :]
train_label = train_label[:3000]


train_label = np_utils.to_categorical(train_label, 2) # one hot encoding
test_label = np_utils.to_categorical(test_label, 2)


# batch_size=1200
nb_epoch=1000
#dropout=0.2
nb_filters=64
nb_row=1
nb_col=6
output1=128


input1 = Input(shape = (1, 121, 1), name="input1")
seq1 = Convolution2D(
				nb_filters,
				nb_row,
				nb_col,
				init = "glorot_uniform",
				border_mode = 'valid',
				W_regularizer = l2( l = 0.01),
				input_shape = (1, 121, 1),
				activation = "relu"
				)(input1)
seq1 = BatchNormalization(epsilon=1e-06, mode=0, momentum=0.5, weights=None)(seq1)
seq1 = MaxPooling2D(pool_size=(1, 3), strides=(3, 1), border_mode='valid')(seq1)

seq1 = Convolution2D(
				nb_filters,
				nb_row,
				nb_col,
				init = "glorot_uniform",
				border_mode = 'valid',
				W_regularizer = l2( l = 0.001),
				activation = "relu"
				)(seq1)
seq1 = BatchNormalization(epsilon=1e-06, mode=0, momentum=0.5, weights=None)(seq1)		
seq1 = MaxPooling2D(pool_size=(1, 3), strides=(3, 1), border_mode='valid')(seq1)

seq1 = Convolution2D(
				nb_filters,
				nb_row,
				nb_col,
				init = "glorot_uniform",
				border_mode = 'valid',
				W_regularizer = l2( l = 0.01),
				activation = "relu"
				)(seq1)
seq1 = BatchNormalization(epsilon=1e-06, mode=0, momentum=0.5, weights=None)(seq1)		
seq1 = MaxPooling2D(pool_size=(1, 3), strides=(2, 1), border_mode='valid')(seq1)
seq1 = Flatten()(seq1)

output1 = Dense(output1, activation="relu")(seq1)
merged = Dense(256, activation="relu")(output1)
merged = Dense(128, activation="relu")(merged)
merged = Dense(64, activation="relu")(merged)
output = Dense(2, activation="softmax", name="output")(merged)

#optimizer
adam = Adam(lr = 0.001)

threshold = 10
callbacks = [
    EarlyStopping(monitor='loss', patience=threshold, verbose=0),
    ]
"""train cross validation, t for train, v for valid"""

valid_score = []
kfold = StratifiedKFold(n_splits=5, shuffle=False,  random_state=1)
count = 0
for train_index,valid_index in kfold.split(np.array([0]*3000),np.array([0]*3000)):
	print('<<<<<COUNT>>>>> '+str(count))
	model = Model(input = [input1], output=[output])
	model.compile(loss='binary_crossentropy', optimizer = "adam", metrics=['accuracy'])
	history = model.fit({'input1':train[train_index]}, {'output':train_label[train_index]},
						nb_epoch= nb_epoch, 
						verbose = True, 
						callbacks=callbacks) 
	loss, accuracy = model.evaluate(train[valid_index], train_label[valid_index], verbose=0)		
	valid_score.extend([accuracy])
	count = count+1
print("valid: %.2f%% (+/- %.2f%%)" % (np.mean(valid_score), np.std(valid_score)))


"""no cross validation"""
"""
model = Model(input = [input1], output=[output])
model.compile(loss='binary_crossentropy', optimizer = "adam", metrics=['accuracy'])
"""
	
"""valid score mean"""
"""
valid_score = []
kfold = StratifiedKFold(n_splits=5, shuffle=False,  random_state=1)
count = 0
for train_index,valid_index in kfold.split(np.array([0]*3000),np.array([0]*3000)):
	print('<<<<<COUNT>>>>> '+str(count))
	model = Model(input = [input1], output=[output])
	# load model weight
	CNN_model = model.load_weights('model(0.9375).h5')
	model.compile(loss='binary_crossentropy', optimizer = "adam", metrics=['accuracy'])
	loss, accuracy = model.evaluate(train[valid_index], train_label[valid_index], verbose=0)		
	valid_score.extend([accuracy])
	print('loss: '+str(loss)+', acc: '+str(accuracy))
	count = count+1
print("valid: %.2f%% (+/- %.2f%%)" % (np.mean(valid_score), np.std(valid_score)))	
"""

"""predict"""
predictions = model.predict({'input1':test})
POS_predict_keras = np_utils.probas_to_classes(predictions)
pre = np.sum(test_label[:,1]==POS_predict_keras)/len(POS_predict_keras)
print(pre)
 					

"""save result"""
model.save('CNN_model.h5')

import csv
f = open("POS_predict_keras.csv", "w")
writer = csv.writer(f, lineterminator="\n")
writer.writerow(POS_predict_keras)
f.close

#######
'''
print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
'''


