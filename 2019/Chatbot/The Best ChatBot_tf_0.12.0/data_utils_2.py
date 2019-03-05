EN_WHITELIST = '0123456789abcdefghijklmnopqrstuvwxyz '


import numpy as np
import pickle

'''
 get metadata - lookup
  idx2w and w2idx

'''
def get_metadata():
    with open('./metadata.pkl', 'rb') as f:
        metadata = pickle.load(f)
    return metadata.get('idx2w'), metadata.get('w2idx'), metadata.get('limit')


'''
 a generic decode function 
    inputs : sequence, lookup

'''
def decode(sequence, lookup, separator=' '): # 0 used for padding, is ignored
    # print ([ lookup[element] for element in sequence if element ])
    return separator.join([ lookup[element] for element in sequence if element ])
    


'''
 encode function
    inputs : sentence, lookup

'''
def encode(sentence, lookup, maxlen, whitelist=EN_WHITELIST, separator=''):
    # to lower case
    sentence = sentence.lower()
    # allow only characters that are on whitelist
    sentence = ''.join( [ ch for ch in sentence if ch in whitelist ] )
    # words to indices
    indices_x = [ token for token in sentence.strip().split(' ') ]
    # clip the sentence to fit model (#words)
    indices_x = indices_x[-maxlen:] if len(indices_x) > maxlen else indices_x
    # zero pad
    idx_x = np.array(pad_seq(indices_x, lookup, maxlen))
    # reshape
    return idx_x.reshape([maxlen, 1])


'''
 replace words with indices in a sequence
  replace with unknown if word not in lookup
    return [list of indices]

'''
def pad_seq(seq, lookup, maxlen):
    indices = []
    for word in seq:
        if word in lookup:
            indices.append(lookup[word])
        else:
            indices.append(lookup['unk'])
    return indices + [0]*(maxlen - len(seq))
