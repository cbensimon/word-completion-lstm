# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:38:29 2016

@author: charles
"""

from models import *
from data import *
from tools import *

X_train, Y_train = data_train()
X_validate, Y_validate = data_validate()

model = build_training_model()
ModelSaver = SaveBestLoss('best.hdf5')

print 'Training...'
model.fit(X_train, Y_train,
          batch_size=batch_size,
          nb_epoch=250,
          validation_data=(X_validate, Y_validate),
          callbacks=[ModelSaver],
          show_accuracy=True)