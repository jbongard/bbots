import constants as c
from pyrosim import PYROSIM
from pins import PINS
from threads import THREADS
from automaton import AUTOMATON
from ann import ANN

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

		self.paths = np.random.randint(0,10,[c.MAX_THREADS,c.MAX_WIRES_PER_THREAD,c.NUM_PARAMETERS_PER_WIRE]) 

        def Age(self):

                self.age = self.age + 1

        def Attempt_To_Create_Valid_Circuit(self):

                self.pins = PINS()

                self.threads = THREADS()

                for t in range(0,c.MAX_THREADS):

                        self.automaton = AUTOMATON(self.paths[t,:,:])

                        self.automaton.Add_Thread(self.pins,self.threads)

                # return ( self.threads.Num_Threads() > 2 )  

		# return self.threads.Contains_Wire_From_Sensor_To_Motor()

		# return self.threads.Contains_Wire_From_Hidden_To_Hidden()

		# return self.threads.Contains_Wire_From_Hidden_To_Motor()

		# sh = self.threads.Contains_Wire_From_Sensor_To_Hidden()

		# hm = self.threads.Contains_Wire_From_Hidden_To_Motor()

		# return ( sh and hm )

		return True

        def Create_Valid_Circuit(self):

		validCircuit = False

		while ( validCircuit == False ):

			validCircuit = self.Attempt_To_Create_Valid_Circuit()

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

		# self.End_Simulation()

                self.fitness = -self.ann.Number_Of_Synapses()

	def End_Simulation(self):

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

		i = random.randint(0,c.MAX_THREADS-1)

		j = random.randint(0,c.MAX_WIRES_PER_THREAD-1)

		k = random.randint(0,c.NUM_PARAMETERS_PER_WIRE-1)

		self.paths[i,j,k] = random.randint(0,9)

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

	def Simulate(self,obstacles,playBlind,playPaused):

                self.sims = {}

                for e in range(0,c.NUM_ENVIRONMENTS):

			self.sims[e] = PYROSIM(playBlind=playBlind,playPaused=playPaused)

			self.sim = self.sims[e]

			self.Send_To_Sim(e)

			obstacles.Send_To_Sim(self.sims[e])

			self.sims[e].Start()

        def Start(self,obstacles,playBlind,playPaused):

                #self.threads.Save()

                self.ann = ANN()

                self.Create_Valid_Circuit()

                self.ann.Convert_Threads_To_Synapses(self.threads)

		#self.Simulate(obstacles,playBlind,playPaused)

# ------------------- Private methods ------------------------

        def Add_HH_Synapses(self):

                for h1 in range(0,c.NUM_HIDDEN_NEURONS):

                        for h2 in range(0,c.NUM_HIDDEN_NEURONS):

                                wt = self.ann.Get_HH_Weight(h1,h2) 

				if ( wt != 0.0 ):

                                	self.sim.Send_Synapse(sourceNeuronIndex = c.NUM_SENSORS + h1 , targetNeuronIndex = c.NUM_SENSORS + h2 , weight = wt )

	def Add_Hidden_Neurons(self):

		for h in range(0,c.NUM_HIDDEN_NEURONS):

        		self.sim.Send_Hidden_Neuron(ID = c.NUM_SENSORS + h , layer = 1, tau = c.MAX_HIDDEN_TAU)

		for h in range(0,self.ann.additionalHiddenNeurons ):

			self.sim.Send_Hidden_Neuron(ID = c.NUM_SENSORS + c.NUM_HIDDEN_NEURONS + h , layer = 1, tau = c.MAX_HIDDEN_TAU, transferFunction = c.IDENTITY_TRANSFER_FUNCTION)

        def Add_HM_Synapses(self):

                for h in range(0,c.NUM_HIDDEN_NEURONS):

                        for m in range(0,c.NUM_MOTORS):

                                wt = self.ann.Get_HM_Weight(h,m) 

				if ( wt != 0.0 ):

                                	self.sim.Send_Synapse(sourceNeuronIndex = c.NUM_SENSORS + h , targetNeuronIndex = c.NUM_SENSORS + c.NUM_HIDDEN_NEURONS + self.ann.additionalHiddenNeurons + m , weight = wt )

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

			self.sim.Send_Motor_Neuron(ID = c.NUM_SENSORS + c.NUM_HIDDEN_NEURONS + self.ann.additionalHiddenNeurons + m , jointID = m , layer = 2 , tau = c.MAX_ACCELERATION)

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

                                wt = self.ann.Get_SH_Weight(s,h)

				if ( wt != 0.0 ):

                                	self.sim.Send_Synapse(sourceNeuronIndex = s , targetNeuronIndex = c.NUM_SENSORS + h , weight = wt )

	def Add_SM_Synapses(self):

		currentAdditionalHiddenNeuron = 0

		for s in range(0,c.NUM_SENSORS):

			for m in range(0,c.NUM_MOTORS):

				wt = self.ann.Get_SM_Weight(s,m)

				if ( wt != 0.0 ):

					sIndex = s

					hIndex = c.NUM_SENSORS + c.NUM_HIDDEN_NEURONS + currentAdditionalHiddenNeuron

					mIndex = c.NUM_SENSORS + c.NUM_HIDDEN_NEURONS + self.ann.additionalHiddenNeurons + m

					self.sim.Send_Synapse(sourceNeuronIndex = sIndex , targetNeuronIndex = hIndex , weight = wt)

					self.sim.Send_Synapse(sourceNeuronIndex = hIndex , targetNeuronIndex = mIndex , weight = 1.0)

					currentAdditionalHiddenNeuron = currentAdditionalHiddenNeuron + 1

	def Add_Synapses(self):

		self.Add_SH_Synapses()

                self.Add_SM_Synapses()

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
