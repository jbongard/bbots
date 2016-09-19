import constants as c
import numpy as np
import pins
import pickle
import os

class WIRES:

        def __init__(self):

		self.wires = {}

		self.numWires = 0

	def Add(self,start,end,weight,pins):

		if ( (start[0] < 0) or (end[0] < 0) ):

			return False

		if ( (start[0] >= c.MAX_PINS_PER_ROW) or (end[0] >= c.MAX_PINS_PER_ROW) ):

			return False

		if ( pins.Pin_Invalid(end) ):

			return False

                if ( pins.Pin_Taken(end) ):

                        return False

		self.wires[self.numWires] = [start,end,weight]

		self.numWires = self.numWires + 1

		return True

	def Load(self):

		f = open('wires.p','rb')

		self = pickle.load(f)

		f.close()

		return self

	def Print(self):

		print self.wires

	def Save(self):

		f = open('tmp.p','wb')

		pickle.dump(self,f)

		f.close()

		os.rename('tmp.p','wires.p')
