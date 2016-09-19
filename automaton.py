import numpy as np
import constants as c

class AUTOMATON:

        def __init__(self):

		self.path = np.random.randint(0,10,[c.MAX_WIRES_PER_THREAD,4])

	def Add_Wires(self,wires):

		self.xStart = self.path[0,0]

		self.yStart = self.path[0,1]

		for i in range(0,c.MAX_WIRES_PER_THREAD):

			self.direction = self.path[i,2]

			self.Enforce_Forward_Movement()

			self.distance = self.path[i,3]

			self.Compute_Target_Position()

			print self.xStart, self.yStart, self.xEnd, self.yEnd

			self.xStart = self.xEnd

			self.yStart = self.yEnd

	def Compute_Target_Position(self):

		if ( self.direction == RIGHT ):

			self.xEnd = self.xStart + distance

			self.yEnd = self.yStart

                elif ( self.direction == DOWN_RIGHT ):

                        self.xEnd = self.xStart + distance

                        self.yEnd = self.yStart + distance

                elif ( self.direction == DOWN ):

			self.xEnd = self.xStart

                        self.yEnd = self.yStart + distance

                elif ( self.direction == DOWN_LEFT ):

                        self.xEnd = self.xStart - distance

                        self.yEnd = self.yStart + distance

                elif ( self.direction == LEFT ):

                        self.xEnd = self.xStart - distance

			self.yEnd = self.yStart

	def Enforce_Forward_Movement(self):

		if ( self.direction == UP_LEFT ):

			self.direction = DOWN_LEFT

		if ( self.direction == UP ):

			self.direction = DOWN

		if ( self.direction == UP_RIGHT ):

			self.direction = DOWN_RIGHT
