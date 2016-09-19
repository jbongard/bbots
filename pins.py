import constants as c
import numpy as np
import matplotlib.pyplot as plt

class PINS:

        def __init__(self):

		self.pinTaken = np.zeros([c.PIN_ROWS,c.PIN_COLUMNS],dtype='d')

	def Draw(self):

	        for i in range(0,c.NUM_SENSORS):

			for j  in range(0,c.PIN_COLUMNS):

        	        	plt.text(j , c.PIN_ROWS - i , 'S'+str(i)+','+str(j) )

                for i in range(0,c.NUM_HIDDEN_NEURONS):

                        for j  in range(0,c.PIN_COLUMNS):

                                plt.text(j , c.PIN_ROWS - (c.NUM_SENSORS+i) , 'H'+str(i)+','+str(j) )

                for i in range(0,c.NUM_MOTORS):

                        for j  in range(0,c.PIN_COLUMNS):

                                plt.text(j , c.PIN_ROWS - (c.NUM_SENSORS+c.NUM_HIDDEN_NEURONS+i) , 'M'+str(i)+','+str(j) )

	def Occupy(self,position):

		x = position[0]

		y = position[1]

		self.pinTaken[ y , x ] = 1 

	def Pin_Group_Full(self,y):

		numberOfTakenPins = sum( self.pinTaken[y,:] )

		return ( numberOfTakenPins == c.PIN_COLUMNS )

	def Pin_Taken(self,target):

		x = target[0]

                y = target[1]
	
		return ( self.pinTaken[y,x] == 1 )

	def Print(self):

		print self.pinTaken

		print ''

	def Valid_Pin(self,target):

		x = target[0]

		y = target[1]

		if ( x < 0 ):

			return False

		if ( x >= c.PIN_ROWS ):

			return False

		if ( y < 0 ):

			return False

		if ( y >= c.PIN_COLUMNS ):

			return False

		return True
