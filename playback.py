from genome import GENOME
from obstacles import OBSTACLES
import os
import pickle

if ( os.path.exists('best.txt') ):

	f = open('best.txt','rb')

        genome = pickle.load(f)

        f.close()

        genome.Start(OBSTACLES(),playBlind=False,playPaused=True)

	genome.End()

        print genome.fitness
