# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:11:02 2016

@author: charles
"""

import numpy as np
import pickle as pkl
from tools import toDataSet
from collections import Counter
from random import shuffle

def _set_from_file(filepath):
    data = pkl.load(open('Data/'+filepath))
    X, Y = toDataSet(data)
    return (X, Y)

def data_train():
    return _set_from_file('data-train.pkl')
    
def data_validate():
    return _set_from_file('data-validate.pkl')
    
def create_data():
    f = open('Data/sent_messages.txt')
    lines = f.readlines()
    
    c = Counter()
    for line in lines:
        c += Counter(line)
      
    dict_vocab = zip(*c.most_common())[0]
    dict_range = range(1,len(dict_vocab)+1)
    
    v2i = dict(zip(dict_vocab, dict_range))
    i2v = dict(zip(dict_range, dict_vocab))
    pkl.dump((v2i, i2v), open('Data/dicts.pkl', 'w'))
    
    
    lines = np.array(lines)    
    R = range(len(lines))
    shuffle(R)
    train = R[:6000]
    validate = R[6000:]
    
    pkl.dump(lines[train], open('Data/data-train.pkl', 'w'))
    pkl.dump(lines[validate], open('Data/data-validate.pkl', 'w'))