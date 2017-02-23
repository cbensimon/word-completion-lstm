# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:08:40 2016

@author: charles
"""

import pickle as pkl

c2i, i2c = pkl.load(open('Data/dicts.pkl'))
maxlen = 150
batch_size = 8
vocab_size = len(c2i) + 1
target_loss = 0.0