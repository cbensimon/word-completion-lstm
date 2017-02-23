# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:05:44 2016

@author: charles
"""

import numpy as np
import pickle as pkl
from keras.preprocessing import sequence
from conf import *
from keras.callbacks import Callback
import os

def embed(x):
    X = np.zeros((x.shape[0], x.shape[1], vocab_size), dtype=np.uint8)
    for i in range(X.shape[0]):
        X[i, range(x.shape[1]), x[i]] = 1
    return X

def toDataSet(data):
    XY = [np.array([c2i[c] for c in s]).astype(np.uint8) for s in data]
    XY = sequence.pad_sequences(XY, maxlen=maxlen)
    x = XY[:,:-1]
    y = XY[:,1:]
    return x, embed(y)
    
def sampleText(model, seed='Bonjour, ', temperature=1):
    model.reset_states()
    for c in seed:
        i = c2i[c]
        y = model.predict(np.array([[i]]))
    result = '^'
    while result[-1] != '\n':
        p = y[0, 0]**temperature
        p /= p.sum()
        c = np.random.choice(range(vocab_size), p=p)
        if c == 0:
            result += '$'
        else:
            result += i2c[c]
        y = model.predict(np.array([[c]]))
    return seed + result[1:]
    
def predictWord(model, seed=''):
    model.reset_states()
    y = model.predict(np.array([[c2i['$']]]))
    for c in seed:
        i = c2i[c]
        y = model.predict(np.array([[i]]))
    result = '^'
    while result[-1] != '\n' and result[-1] != ' ':
        c = y[0, 0].argmax()
        if c == 0:
            result += '$'
        else:
            result += i2c[c]
        y = model.predict(np.array([[c]]))
    return result[1:]
    
class SaveBestLoss(Callback):
    
    def _loss(self):
        X, Y = self.model.validation_data[:2]
        return self.model.evaluate(X, Y, batch_size=batch_size, verbose=0)
    
    def __init__(self, filepath):  
        super(Callback, self).__init__()
        self.filepath = 'Weights/'+ filepath
            
    def on_train_begin(self, logs={}):
        if os.path.isfile(self.filepath):
            print 'Loading ' + self.filepath + '...'
            self.model.load_weights(self.filepath)
        elif os.path.isfile('Weights/init.hdf5'):
            print 'Loading init weights...'
            self.model.load_weights('Weights/init.hdf5')
        else:
            self.model.save_weights('Weights/init.hdf5')
        self.best_loss = self._loss()
        print 'Loss: ' + str(self.best_loss)
    
    def on_epoch_end(self, epoch, logs={}):
        loss = logs.get('val_loss')
        if (loss < self.best_loss):
            self.model.save_weights(self.filepath, overwrite=True)
            self.best_loss = loss
            if loss < target_loss:
                self.model.stop_training = True