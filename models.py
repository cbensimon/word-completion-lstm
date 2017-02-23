# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 09:54:30 2016

@author: charles
"""

from keras.models import Sequential
from keras.layers import Embedding, Dropout, TimeDistributedDense
from keras.layers.recurrent import LSTM
from conf import vocab_size

def build_training_model(): 
    print('Build model...')
    model = Sequential()
    model.add(Embedding(vocab_size, vocab_size, mask_zero=True, init='identity', trainable=False))
    model.add(LSTM(512, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(512, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(TimeDistributedDense(vocab_size, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
    return model
    
def build_sampling_model():
    print('Build model...')
    model = Sequential()
    model.add(Embedding(vocab_size, vocab_size, mask_zero=True, init='identity', batch_input_shape=(1,1)))
    model.add(LSTM(512, return_sequences=True, stateful=True))
    model.add(Dropout(0.2))
    model.add(LSTM(512, return_sequences=True, stateful=True))
    model.add(Dropout(0.2))
    model.add(TimeDistributedDense(vocab_size, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
    return model