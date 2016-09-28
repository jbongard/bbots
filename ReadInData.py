import numpy as np

import pickle

import constants as c


runIndex = 3

GOorEO = c.GO

fileName = 'Data_H4/best'+str(runIndex)+'_'+str(GOorEO)+'.p'

f = open(fileName,'rb')

fitnesses = -pickle.load(f)

f.close()

print fitnesses
