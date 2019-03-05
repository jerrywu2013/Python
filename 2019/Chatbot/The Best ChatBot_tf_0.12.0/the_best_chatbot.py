# Building The Best ChatBot with Deep NLP



# Importing the libraries
import seq2seq_wrapper
import importlib
importlib.reload(seq2seq_wrapper)
import data_preprocessing
import data_utils_1
import data_utils_2




########## PART 1 - DATA PREPROCESSING ##########



# Importing the dataset
metadata, idx_q, idx_a = data_preprocessing.load_data(PATH = './')

# Splitting the dataset into the Training set and the Test set
(trainX, trainY), (testX, testY), (validX, validY) = data_utils_1.split_dataset(idx_q, idx_a)

# Embedding
xseq_len = trainX.shape[-1]
yseq_len = trainY.shape[-1]
batch_size = 16
vocab_twit = metadata['idx2w']
xvocab_size = len(metadata['idx2w'])  
yvocab_size = xvocab_size
emb_dim = 1024
idx2w, w2idx, limit = data_utils_2.get_metadata()



########## PART 2 - BUILDING THE SEQ2SEQ MODEL ##########



# Building the seq2seq model
model = seq2seq_wrapper.Seq2Seq(xseq_len = xseq_len,
                                yseq_len = yseq_len,
                                xvocab_size = xvocab_size,
                                yvocab_size = yvocab_size,
                                ckpt_path = './weights',
                                emb_dim = emb_dim,
                                num_layers = 3)



########## PART 3 - TRAINING THE SEQ2SEQ MODEL ##########



# See the Training in seq2seq_wrapper.py



########## PART 4 - TESTING THE SEQ2SEQ MODEL ##########



# Loading the weights and Running the session
session = model.restore_last_session()

# Getting the ChatBot predicted answer
def respond(question):
    encoded_question = data_utils_2.encode(question, w2idx, limit['maxq'])
    answer = model.predict(session, encoded_question)[0]
    return data_utils_2.decode(answer, idx2w) 

# Setting up the chat
while True :
  question = input("You: ")
  answer = respond(question)
  print ("ChatBot: "+answer)
