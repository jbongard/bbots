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

	def Pin_Taken(self,target):

		x = target[0]

                y = target[1]
	
		return ( self.pinTaken[y,x] == 1 )
