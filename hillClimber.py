import constants as c
from obstacles import OBSTACLES
from pyrosim import PYROSIM
from robot import ROBOT

import copy
import random
import numpy as np

class HILLCLIMBER:

        def __init__(self):

		self.obstacles = OBSTACLES()

	def Evolve(self):

		self.parent = ROBOT()

		self.parent.Evaluate(self.obstacles,playBlind=True,playPaused=False)

		for g in range(0,c.NUM_GENERATIONS):

			child = copy.deepcopy(self.parent)

			child.Mutate()

			child.Evaluate(self.obstacles,playBlind=True,playPaused=False)

			printString = "[generation " + str(g) + " of " + str(c.NUM_GENERATIONS) + "]: "

			printString = printString + "[parent fitness: " + str(self.parent.fitness) + "] "

                        printString = printString + "[child fitness: " + str(child.fitness) + "] "

			print printString

			if ( child.fitness > self.parent.fitness ):

				self.parent = child

	def ShowBest(self):

		self.parent.Evaluate(self.obstacles,playBlind=False,playPaused=True)

