from pyrosim import PYROSIM

from obstacles import OBSTACLES

from robot import ROBOT

import constants as c

import numpy as np

import copy

import random

import math

def Mutation_Of(parentSH,parentHM):

	childSH = copy.deepcopy(parentSH)

	i = random.randint(0,c.NUM_SENSORS-1)

	j = random.randint(0,c.NUM_HIDDEN_NEURONS-1)

	childSH[i,j] = random.gauss( childSH[i,j] , math.fabs( childSH[i,j] ) )



        childHM = copy.deepcopy(parentHM)

        i = random.randint(0,c.NUM_HIDDEN_NEURONS-1)

        j = random.randint(0,c.NUM_MOTORS-1)

        childHM[i,j] = random.gauss( childHM[i,j] , math.fabs( childHM[i,j] ) )


	return childSH , childHM 

def Perform_Simulation(sh,hm,playblind,playpaused):

	sims = {}

	for e in range(0,c.NUM_ENVIRONMENTS):

		sims[e] = PYROSIM(playBlind = playblind, playPaused = playpaused)

		obstacles = OBSTACLES()

		obstacles.Send_To_Sim(sims[e])

		robot = ROBOT()

		robot.Send_To_Sim(sims[e],e,sh,hm)

		sims[e].Start()

        for e in range(0,c.NUM_ENVIRONMENTS):

		sims[e].Wait_To_Finish()

		fitness = 0.0

		sensorValues = np.zeros((2,c.evaluationTime),dtype='f')

		for t in range(0,c.evaluationTime):

			for s in range(0,2):

        			sensorValues[s,t] = sims[e].Get_Sensor_Data(s+2,0,t)

		fitness = fitness + sum(sum(sensorValues))

	return fitness

# --------------------- Main function ------------------

parentSH = np.random.rand(c.NUM_SENSORS,c.NUM_HIDDEN_NEURONS) * 2 - 1

parentHM = np.random.rand(c.NUM_HIDDEN_NEURONS,c.NUM_MOTORS) * 2 - 1

parentFitness = Perform_Simulation(parentSH,parentHM,True,False)

for g in range(0,c.NUM_GENERATIONS):

	[childSH,childHM] = Mutation_Of(parentSH,parentHM)

	childFitness = Perform_Simulation(childSH,childHM,True,False)

	print g , parentFitness , childFitness

	if ( childFitness > parentFitness ):

		parentSH = childSH

		parentHM = childHM

		parentFitness = childFitness

parentFitness = Perform_Simulation(parentSH,parentHM,False,True)

