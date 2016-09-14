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

		self.parent.Evaluate(self.obstacles,playBlind=True)

		for g in range(0,c.NUM_GENERATIONS):

			child = copy.deepcopy(self.parent)

			child.Mutate()

			child.Evaluate(self.obstacles,playBlind=True)

			print g , self.parent.fitness , child.fitness

			if ( child.fitness > self.parent.fitness ):

				self.parent = child

	def ShowBest(self):

		self.parent.Evaluate(self.obstacles,playBlind=False)

