import constants as c
import numpy as np
import pins
import pickle
import os
import matplotlib.pyplot as plt
from pins import PINS

class WIRES:

        def __init__(self):

		self.wires = {}

		self.numWires = 0

	def Add(self,start,end,weight,pins):

		if ( (start[0] < 0) or (end[0] < 0) ):

			return False

		if ( (start[0] >= c.PIN_COLUMNS) or (end[0] >= c.PIN_COLUMNS) ):

			return False

                if ( (start[1] < 0) or (end[1] < 0) ):

                        return False

                if ( (start[1] >= c.PIN_ROWS) or (end[1] >= c.PIN_ROWS) ):

                        return False

                if ( pins.Pin_Taken(end) ):

                        return False

		self.wires[self.numWires] = [start,end,weight]

		self.numWires = self.numWires + 1

		return True

	def Draw(self,i):

		fig = plt.figure(i+1)

		ax = plt.subplot(111)

		pins = PINS()

		pins.Draw()

		self.Draw_Wires(ax)

	def Draw_Wires(self,ax):
	
		for w in range(0,self.numWires):

			wire = self.wires[w]

			start = wire[0]

			end = wire[1]

			weight = wire[2]

			print start, end, weight

			print start[0],end[0],start[1],end[1]

			plt.plot([start[0],end[0]],[c.PIN_ROWS-start[1],c.PIN_ROWS-end[1]],'r-')

		ax.set_xlim(-1 , c.PIN_COLUMNS)

		ax.set_ylim(0 , c.PIN_ROWS+1)

		ax.set_xticks([])

		ax.set_yticks([])

	def Load(self,i):

		f = open('wires'+str(i)+'.p','rb')

		self = pickle.load(f)

		f.close()

		return self

	def Print(self):

		print self.wires

	def Save(self,i):

		f = open('tmp.p','wb')

		pickle.dump(self,f)

		f.close()

		os.rename('tmp.p','wires'+str(i)+'.p')
