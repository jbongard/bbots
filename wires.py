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

	def Add_Wire(self,start,end,weight,pins):

		self.wires[self.numWires] = [start,end,weight]

		pins.Occupy(start)

		pins.Occupy(end)

		self.numWires = self.numWires + 1

		return True

	def Convertable_Wire(self,w):

		return ( self.From_Sensor_To_Hidden(w) or self.From_Sensor_To_Motor(w) or self.From_Hidden_To_Hidden(w) or self.From_Hidden_To_Motor(w) )

	def Draw(self):

		fig = plt.figure(1)

		ax = plt.subplot(111)

		pins = PINS()

		pins.Draw()

		self.Draw_Wires(ax)

	def Draw_Wires(self,ax):

		col = np.random.rand(3)

		lineWidth = 5 * self.numWires + 1
	
		for w in range(0,self.numWires):

			wire = self.wires[w]

			start = wire[0]

			end = wire[1]

			xStart = start[0]
			yStart = start[1]

			xEnd   = end[0]
			yEnd   = end[1]

			weight = wire[2]

			print yStart, yEnd

			plt.plot([xStart,xEnd],[c.PIN_ROWS-yStart,c.PIN_ROWS-yEnd],'r-',linewidth=lineWidth,color=col)

			lineWidth = lineWidth - 5

			col = col / 1.3

		ax.set_xlim(-1 , c.PIN_COLUMNS)

		ax.set_ylim(0 , c.PIN_ROWS+1)

		ax.set_xticks([])

		ax.set_yticks([])

        def From_Hidden_To_Hidden(self,w):

                wire = self.wires[w]

                start = wire[0]

                end = wire[1]

                startY = start[1]

                endY = end[1]

                fromHidden = (startY >= c.NUM_SENSORS) and ( startY < ( c.NUM_SENSORS + c.NUM_HIDDEN_NEURONS ) )

                toHidden = (endY >= c.NUM_SENSORS) and ( endY < ( c.NUM_SENSORS + c.NUM_HIDDEN_NEURONS ) )

                return ( fromHidden and toHidden )

        def From_Hidden_To_Motor(self,w):

                wire = self.wires[w]

                start = wire[0]

                end = wire[1]

                startY = start[1]

                endY = end[1]

                fromHidden = (startY >= c.NUM_SENSORS) and ( startY < ( c.NUM_SENSORS + c.NUM_HIDDEN_NEURONS ) )

                toMotor = endY >= ( c.NUM_SENSORS + c.NUM_HIDDEN_NEURONS )

                return ( fromHidden and toMotor )

        def From_Sensor_To_Hidden(self,w):

                wire = self.wires[w]

                start = wire[0]

                end = wire[1]

                startY = start[1]

                endY = end[1]

                fromSensor = ( startY < c.NUM_SENSORS )

                toHidden = (endY >= c.NUM_SENSORS) and ( endY < ( c.NUM_SENSORS + c.NUM_HIDDEN_NEURONS ) ) 

                return ( fromSensor and toHidden )

	def From_Sensor_To_Motor(self,w):

		wire = self.wires[w]

		start = wire[0]

		end = wire[1]

		startY = start[1]

		endY = end[1]

		fromSensor = ( startY < c.NUM_SENSORS )

		toMotor = ( endY >= (c.NUM_SENSORS + c.NUM_HIDDEN_NEURONS) )

		return ( fromSensor and toMotor ) 

	def Get_Length(self):

		return self.numWires

        def Get_From_Hidden_Index(self,w):

                wire = self.wires[w]

                start = wire[0]

                startY = start[1]

                return( startY - c.NUM_SENSORS )

	def Get_From_Sensor_Index(self,w):

		wire = self.wires[w]

		start = wire[0]

		startY = start[1]

		return ( startY )
	
	def Get_To_Hidden_Index(self,w):

                wire = self.wires[w]

		end = wire[1]

		endY = end[1]

		return( endY - c.NUM_SENSORS )
	
        def Get_To_Motor_Index(self,w):

                wire = self.wires[w]

                end = wire[1]

                endY = end[1]

                return( endY - (c.NUM_SENSORS + c.NUM_HIDDEN_NEURONS) )

	def Get_Weight(self,w):

		wire = self.wires[w]

		return wire[2]
	
	def Load(self):

		f = open('wires.p','rb')

		self = pickle.load(f)

		f.close()

		return self

	def Print(self,w):

		print self.wires[w]

	def Save(self):

		f = open('tmp.p','wb')

		pickle.dump(self,f)

		f.close()

		os.rename('tmp.p','wires.p')
