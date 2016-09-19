import constants as c
from pyrosim import PYROSIM
from pins import PINS
from threads import THREADS
from automaton import AUTOMATON

import random
import numpy as np
import math
import os
import pickle

class GENOME:

        def __init__(self,ID):

		self.ID = ID

		self.age = 0

		self.evaluated = False

		self.sh = np.random.rand(c.NUM_SENSORS,c.NUM_HIDDEN_NEURONS) * 2 - 1

                self.hh = np.random.rand(c.NUM_HIDDEN_NEURONS,c.NUM_HIDDEN_NEURONS) * 2 - 1

		self.hm = np.random.rand(c.NUM_HIDDEN_NEURONS,c.NUM_MOTORS) * 2 - 1

		self.hiddenTaus = np.random.rand(c.NUM_HIDDEN_NEURONS) * 2 * c.MAX_HIDDEN_TAU - 1

		validCircuit = False

		while ( validCircuit == False ):

			self.pins = PINS()

			self.threads = THREADS()

			for t in range(0,c.MAX_THREADS):
	
				self.automaton = AUTOMATON()

				self.automaton.Add_Thread(self.pins,self.threads)

			validCircuit = self.threads.Contains_Max_Thread_Length() 
	
			if ( validCircuit ):

				self.threads.Print()
	
				self.threads.Save()

		exit()

        def Age(self):

                self.age = self.age + 1

        def Dominates(self,other):

                if ( self.fitness <= other.fitness ):

                        if ( self.age <= other.age ):

                                if ( (self.fitness == other.fitness) & (self.age==other.age) ):

                                        i_am_younger = self.ID > other.ID

                                        return i_am_younger
                                else:
                                        return True
                        else:
                                return False
                else:
                        return False

	def End(self):

		self.fitness = 1000000.0

		# self.fitness = 0.0

                for e in range(0,c.NUM_ENVIRONMENTS):

			self.sim = self.sims[e]

                	self.sims[e].Wait_To_Finish()

			self.Compute_Fitness()

		self.fitness = -self.fitness

		self.evaluated = True

		del self.sims
		del self.sim

        def Get_Dominated(self):

                return self.dominated

	def Mutate(self):

		mutType = random.randint(0,3)

		if ( mutType == 0 ):

			self.Mutate_SH()

		elif ( mutType == 1 ):

			self.Mutate_HH()

		elif ( mutType == 2 ):

			self.Mutate_HM()
		else:
			self.Mutate_Hidden_Taus()

        def Print(self):

                printString = ''

                printString = printString + '[f: '+str(self.fitness)+'] \t'

                printString = printString + '[a: '+str(self.age)+'] \t'

                printString = printString + '[d: '+str(self.dominated)+'] \t'

                print printString

        def Reset(self):

                self.evaluated = False

                self.fitness = 0.0

                self.dominated = False

        def Save(self):

                f = open('tmp.txt','wb')

                pickle.dump(self,f)

                f.close()

                os.rename('tmp.txt','best.txt')

        def Set_Dominated(self,dominated):

                self.dominated = dominated

        def Start(self,obstacles,playBlind,playPaused):

                self.sims = {}

                for e in range(0,c.NUM_ENVIRONMENTS):

                        self.sims[e] = PYROSIM(playBlind=playBlind,playPaused=playPaused)

                        self.sim = self.sims[e]

                        self.Send_To_Sim(e)

                        obstacles.Send_To_Sim(self.sims[e])

                        self.sims[e].Start()

# ------------------- Private methods ------------------------

        def Add_HH_Synapses(self):

                for h1 in range(0,c.NUM_HIDDEN_NEURONS):

                        for h2 in range(0,c.NUM_HIDDEN_NEURONS):

                                wt = self.hh[h1,h2]

                                self.sim.Send_Synapse(sourceNeuronIndex = c.NUM_SENSORS + h1 , targetNeuronIndex = c.NUM_SENSORS + h2 , weight = wt )

	def Add_Hidden_Neurons(self):

		for h in range(0,c.NUM_HIDDEN_NEURONS):

        		self.sim.Send_Hidden_Neuron(ID = c.NUM_SENSORS + h , layer = 1, tau = self.hiddenTaus[h])

        def Add_HM_Synapses(self):

                for h in range(0,c.NUM_HIDDEN_NEURONS):

                        for m in range(0,c.NUM_MOTORS):

                                wt = self.hm[h,m]

                                self.sim.Send_Synapse(sourceNeuronIndex = c.NUM_SENSORS + h , targetNeuronIndex = c.NUM_SENSORS + c.NUM_HIDDEN_NEURONS + m , weight = wt )

	def Add_Infrared_Sensors(self):

		self.Add_Left_Infrared_Sensor()

		self.Add_Right_Infrared_Sensor()

	def Add_Left_Infrared_Sensor(self):

                x = self.robotPosX - c.ROBOT_WIDTH/2.0

                y = self.robotPosY + c.ROBOT_LENGTH/2.0

                z = c.WHEEL_RADIUS + c.ROBOT_HEIGHT

                self.sim.Send_Cylinder(ID=5, x=x, y=y, z=z, r1=1, r2=0, r3=0, length=0.0, radius=c.WHEEL_RADIUS/10.0, r=0, g=0, b=0)

                self.sim.Send_Joint(ID = 4, firstObjectID=4, secondObjectID=5, x=x, y=y, z=z, n1=1, n2=0, n3=0, lo=0,hi=0 )

        	self.sim.Send_Ray_Sensor(ID=0, objectIndex=5, x=x,y=y,z=z, r1=0,r2=1,r3=0)

	def Add_Left_Light_Sensor(self):

        	self.sim.Send_Light_Sensor(ID=2, objectIndex = 5 )

        def Add_Left_Touch_Sensor(self):

                self.sim.Send_Touch_Sensor(ID=4, objectIndex = 0 )

        def Add_Light_Sensors(self):

                self.Add_Left_Light_Sensor()

                self.Add_Right_Light_Sensor()

	def Add_Motor_Neurons(self):

		for m in range(0,c.NUM_MOTORS):

			self.sim.Send_Motor_Neuron(ID = c.NUM_SENSORS + c.NUM_HIDDEN_NEURONS + m , jointID = m , layer = 2 , tau = c.MAX_ACCELERATION)

        def Add_Right_Infrared_Sensor(self):

                x = self.robotPosX + c.ROBOT_WIDTH/2.0

                y = self.robotPosY + c.ROBOT_LENGTH/2.0

                z = c.WHEEL_RADIUS + c.ROBOT_HEIGHT

                self.sim.Send_Cylinder(ID=6, x=x, y=y, z=z, r1=1, r2=0, r3=0, length=0.0, radius=c.WHEEL_RADIUS/10.0, r=0, g=0, b=0)

                self.sim.Send_Joint(ID = 5, firstObjectID=4, secondObjectID=6, x=x, y=y, z=z, n1=1, n2=0, n3=0, lo=0,hi=0 )

                self.sim.Send_Ray_Sensor(ID=1, objectIndex=6, x=x,y=y,z=z, r1=0,r2=1,r3=0)

        def Add_Right_Light_Sensor(self):

                self.sim.Send_Light_Sensor(ID=3, objectIndex = 6 )

        def Add_Right_Touch_Sensor(self):

                self.sim.Send_Touch_Sensor(ID=5, objectIndex = 1 )

	def Add_Sensor_Neurons(self):

		for s in range(0,c.NUM_SENSORS):

			self.sim.Send_Sensor_Neuron(ID=s, sensorID=s, layer=0 )

        def Add_SH_Synapses(self):

                for s in range(0,c.NUM_SENSORS):

                        for h in range(0,c.NUM_HIDDEN_NEURONS):

                                wt = self.sh[s,h]

                                self.sim.Send_Synapse(sourceNeuronIndex = s , targetNeuronIndex = c.NUM_SENSORS + h , weight = wt )

	def Add_Synapses(self):

		self.Add_SH_Synapses()

		self.Add_HH_Synapses()

		self.Add_HM_Synapses()


	def Add_Touch_Sensors(self):

		self.Add_Left_Touch_Sensor()

		self.Add_Right_Touch_Sensor()

        def Compute_Fitness(self):

                if ( self.sim.simulationSucceeded == False ):

			return

                sensorValues = np.zeros((2,c.evaluationTime),dtype='f')

                for t in range(0,c.evaluationTime):

			leftWheelOnTheGround = self.sim.Get_Sensor_Data(4,0,t)

                        rightWheelOnTheGround = self.sim.Get_Sensor_Data(5,0,t)

			bothWheelsOnTheGround = leftWheelOnTheGround and rightWheelOnTheGround

			if ( bothWheelsOnTheGround ):

                               	sensorValues[0,t] = self.sim.Get_Sensor_Data(2,0,t)

                                sensorValues[1,t] = self.sim.Get_Sensor_Data(3,0,t)

		fitnessInThisEnvironment = sum(sum(sensorValues))

		if ( fitnessInThisEnvironment < self.fitness ):

			self.fitness = fitnessInThisEnvironment

                # self.fitness = self.fitness - fitnessInThisEnvironment 

        def Connect_Back_Wheel_To_Chassis(self):

                x = self.robotPosX

                y = self.robotPosY - c.ROBOT_LENGTH/2.0

                z = c.WHEEL_RADIUS

                self.sim.Send_Joint(ID = 2, firstObjectID=2, secondObjectID=3, x=x, y=y, z=z, n1=1, n2=0, n3=0)

                self.sim.Send_Joint(ID = 3, firstObjectID=3, secondObjectID=4, x=x, y=y, z=z, n1=0, n2=1, n3=0)

	def Connect_Left_Wheel_To_Chassis(self):

                x = self.robotPosX - c.ROBOT_WIDTH/2.0

                y = self.robotPosY + c.ROBOT_LENGTH/2.0

                z = c.WHEEL_RADIUS

		self.sim.Send_Joint(ID = 0, firstObjectID=0, secondObjectID=4, x=x, y=y, z=z, n1=1, n2=0, n3=0, lo=-c.WHEEL_SPEED, hi=+c.WHEEL_SPEED)

        def Connect_Right_Wheel_To_Chassis(self):

                x = self.robotPosX + c.ROBOT_WIDTH/2.0

                y = self.robotPosY + c.ROBOT_LENGTH/2.0

                z = c.WHEEL_RADIUS

                self.sim.Send_Joint(ID = 1, firstObjectID=1, secondObjectID=4, x=x, y=y, z=z, n1=1, n2=0, n3=0, lo=-c.WHEEL_SPEED, hi=+c.WHEEL_SPEED)

        def Create_Body(self):

                self.Send_Left_Wheel()
                self.Send_Right_Wheel()
                self.Send_Back_Wheel()
                self.Send_Chassis()
                self.Connect_Left_Wheel_To_Chassis()
                self.Connect_Right_Wheel_To_Chassis()
                self.Connect_Back_Wheel_To_Chassis()
                self.Add_Infrared_Sensors()
                self.Add_Light_Sensors()
		self.Add_Touch_Sensors()

        def Create_Brain(self):

                self.Add_Sensor_Neurons()
                self.Add_Hidden_Neurons()
                self.Add_Motor_Neurons()
                self.Add_Synapses()

        def Mutate_SH(self):

                i = random.randint(0,c.NUM_SENSORS-1)

                j = random.randint(0,c.NUM_HIDDEN_NEURONS-1)

                self.sh[i,j] = random.gauss( self.sh[i,j] , math.fabs( self.sh[i,j] ) )

        def Mutate_HH(self):

                i = random.randint(0,c.NUM_HIDDEN_NEURONS-1)

                j = random.randint(0,c.NUM_HIDDEN_NEURONS-1)

                self.hh[i,j] = random.gauss( self.hh[i,j] , math.fabs( self.hh[i,j] ) )

        def Mutate_HM(self):

                i = random.randint(0,c.NUM_HIDDEN_NEURONS-1)

                j = random.randint(0,c.NUM_MOTORS-1)

                self.hm[i,j] = random.gauss( self.hm[i,j] , math.fabs( self.hm[i,j] ) )

	def Mutate_Hidden_Taus(self):

		j = random.randint(0,c.NUM_HIDDEN_NEURONS-1)

		self.hiddenTaus[j] = random.gauss( self.hiddenTaus[j] , math.fabs( self.hiddenTaus[j] )  )

		if ( self.hiddenTaus[j] > c.MAX_HIDDEN_TAU ):

			self.hiddenTaus[j] = c.MAX_HIDDEN_TAU

		if ( self.hiddenTaus[j] < -c.MAX_HIDDEN_TAU ):

			self.hiddenTaus[j] = -c.MAX_HIDDEN_TAU

	def Send_Back_Wheel(self):

        	x = self.robotPosX

        	y = self.robotPosY - c.ROBOT_LENGTH/2.0

        	z = c.WHEEL_RADIUS

        	self.sim.Send_Cylinder(ID=2, x=x, y=y, z=z, r1=1, r2=0, r3=0, length=0.0, radius=c.WHEEL_RADIUS, r=1, g=1, b=1)

	        self.sim.Send_Cylinder(ID=3, x=x, y=y, z=z, r1=0, r2=1, r3=0, length=0.0, radius=c.WHEEL_RADIUS/2.0, r=0, g=1, b=0)

	def Send_Chassis(self):

        	x = self.robotPosX

        	y = self.robotPosY

        	z = c.WHEEL_RADIUS + c.ROBOT_HEIGHT/2

        	self.sim.Send_Box(ID=4, x=x, y=y, z=z, length=c.ROBOT_WIDTH, width=c.ROBOT_LENGTH, height=c.ROBOT_HEIGHT, r=1, g=1, b=1)

	def Send_Left_Wheel(self):

        	x = self.robotPosX - c.ROBOT_WIDTH/2.0

        	y = self.robotPosY + c.ROBOT_LENGTH/2.0

        	z = c.WHEEL_RADIUS

        	self.sim.Send_Cylinder(ID=0, x=x, y=y, z=z, r1=1, r2=0, r3=0, length=0.0, radius=c.WHEEL_RADIUS, r=1, g=1, b=1)

	def Send_Right_Wheel(self):

        	x = self.robotPosX + c.ROBOT_WIDTH/2.0

        	y = self.robotPosY + c.ROBOT_LENGTH/2.0

        	z = c.WHEEL_RADIUS

        	self.sim.Send_Cylinder(ID=1, x=x, y=y, z=z, r1=1, r2=0, r3=0, length=0.0, radius=c.WHEEL_RADIUS, r=1, g=1, b=1)

        def Send_To_Sim(self,environmentIndex):

                self.robotPosX = -(3*c.OBSTACLE_WIDTH/2.0) + (environmentIndex * 3 * c.OBSTACLE_WIDTH) / ( c.NUM_ENVIRONMENTS - 1.0 )

                self.robotPosY = -6.0 * c.OBSTACLE_LENGTH

                self.Create_Body()

                self.Create_Brain()
