import numpy as np
import constants as c
import pickle
import matplotlib.pyplot as plt
import math
from scipy.stats import ttest_ind, ttest_ind_from_stats

numRuns = 30

fitnesses = np.zeros([numRuns,c.NUM_GENERATIONS,2],dtype='f')

for i in range(0,numRuns):

	for k in range(0,2):

		fileName = 'Data_H4/best'+str(i)+'_'+str(k)+'.p'

                f = open(fileName,'rb')

                fitnesses[i,:,k] = -pickle.load(f)

		f.close()

		print i,k,fitnesses[i,c.NUM_GENERATIONS-1,k]

meanFitnesses = np.mean(fitnesses,0)

stdFitnesses = np.std(fitnesses,0)

serrFitnesses = stdFitnesses / math.sqrt(float(numRuns))

bestFitnessesAtEndOfGO = fitnesses[:,c.NUM_GENERATIONS-1,c.GO]

bestFitnessesAtEndOfEO = fitnesses[:,c.NUM_GENERATIONS-1,c.EO]

t, p = ttest_ind(bestFitnessesAtEndOfGO , bestFitnessesAtEndOfEO , equal_var=False)

print 'p value from Student t-test: ' + str(p)

fig = plt.figure(1)

ax = plt.subplot(111)

plt.plot(meanFitnesses[:,c.GO] + serrFitnesses[:,c.GO],	'r-')

plt.plot(meanFitnesses[:,c.GO],				'r-',linewidth=3)

plt.plot(meanFitnesses[:,c.GO] - serrFitnesses[:,c.GO],	'r-')



plt.plot(meanFitnesses[:,c.EO] + serrFitnesses[:,c.EO], 'b-')

plt.plot(meanFitnesses[:,c.EO],                         'b-',linewidth=3)

plt.plot(meanFitnesses[:,c.EO] - serrFitnesses[:,c.EO], 'b-')

plt.xlabel('Generations')

plt.ylabel('Fitness (total light exposure)')

#plt.show()

plt.savefig('Text/Fig1.png')

