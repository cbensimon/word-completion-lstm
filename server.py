# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 11:06:45 2016

@author: charles
"""

from models import build_sampling_model
from tools import predictWord
import zerorpc

sampling_model = build_sampling_model()
print 'Loading Weights'
sampling_model.load_weights('Weights/best.hdf5')
print 'Force compile...'
predictWord(sampling_model, seed='$')

class WordPredict(object):
	def predict(self, seed):
		print 'predict: '+ seed
		return predictWord(sampling_model, seed=seed)

s = zerorpc.Server(WordPredict())
s.bind('tcp://0.0.0.0:4242')
print 'Server run'
s.run()