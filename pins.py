import constants as c
import numpy as np

class PINS:

        def __init__(self):

		self.validPins = np.zeros([c.NUM_PINS,c.MAX_PINS_PER_ROW],dtype='d')

		self.validPins[c.BL,0:4] = 1

                self.validPins[c.N1,0:7] = 1
                self.validPins[c.N2,0:7] = 1
                self.validPins[c.N3,0:7] = 1

                self.validPins[c.FL,0:4] = 1

                self.validPins[c.N4,0:7] = 1
                self.validPins[c.N5,0:7] = 1
                self.validPins[c.N6,0:7] = 1

                self.validPins[c.BR,0:4] = 1

                self.validPins[c.PL,0:6] = 1
                self.validPins[c.RL,0:6] = 1
                self.validPins[c.RR,0:6] = 1

                self.validPins[c.FR,0:4] = 1

                self.validPins[c.PR,0:6] = 1


		self.pinTaken = np.zeros([c.NUM_PINS,c.MAX_PINS_PER_ROW],dtype='d')

        def Pin_Invalid(self,target):

		x = target[0]

		y = target[1]

		return self.validPins[y,x] == 0

	def Pin_Taken(self,target):

		x = target[0]

                y = target[1]
	
		return self.pinTaken[y,x] == 1	
