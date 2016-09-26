import pickle

for r in range(0,1):

	for e in range(0,2):

		fileName = 'Data/best'+str(r)+'_'+str(e)+'.p'

        	f = open(fileName,'rb')

        	fitnesses = pickle.load(f)

		print r,e
		print fitnesses

        	f.close()
