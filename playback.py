import constants as c
from genome import GENOME
from pyrosim import PYROSIM
from obstacles import OBSTACLES
import os
import pickle

if ( os.path.exists('best_1_1.txt') ):

	f = open('best_1_1.txt','rb')

        genome = pickle.load(f)

        f.close()

	obstacles = OBSTACLES()

	for e in range(0,c.NUM_ENVIRONMENTS):

        	genome.sim = PYROSIM(playBlind=False,playPaused=False)

        	genome.Send_To_Sim(e)

        	obstacles.Send_To_Sim(genome.sim)

        	genome.sim.Start()

		genome.sim.Wait_To_Finish()

        print genome.fitness
