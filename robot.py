import constants as c
import random

class ROBOT:

        def __init__(self):

		pass

	def Send_To_Sim(self,sim,environmentIndex,sh,hm):

		self.sim = sim

        	self.robotPosX = -c.OBSTACLE_WIDTH + (2.0 * environmentIndex * c.OBSTACLE_WIDTH) / ( c.NUM_ENVIRONMENTS - 1.0 )

        	self.robotPosY = -6.0 * c.OBSTACLE_LENGTH

        	self.Send_Left_Wheel()

        	self.Send_Right_Wheel()

        	self.Send_Back_Wheel()

        	self.Send_Chassis()

		self.Connect_Left_Wheel_To_Chassis()

                self.Connect_Right_Wheel_To_Chassis()

		self.Connect_Back_Wheel_To_Chassis()

		self.Add_Infrared_Sensors()

		self.Add_Light_Sensors()

		self.Add_Sensor_Neurons()

		self.Add_Hidden_Neurons()

		self.Add_Motor_Neurons()

		self.Add_Synapses(sh,hm)

# ------------------- Private methods ------------------------

	def Add_Hidden_Neurons(self):

		for h in range(0,c.NUM_HIDDEN_NEURONS):

        		self.sim.Send_Hidden_Neuron(ID = c.NUM_SENSORS + h , layer = 1)

	def Add_Infrared_Sensors(self):

		self.Add_Left_Infrared_Sensor()

		self.Add_Right_Infrared_Sensor()

	def Add_Left_Infrared_Sensor(self):

                x = self.robotPosX - c.ROBOT_WIDTH/2.0

                y = self.robotPosY + c.ROBOT_LENGTH/2.0

                z = c.WHEEL_RADIUS + c.ROBOT_HEIGHT

                self.sim.Send_Cylinder(ID=9, x=x, y=y, z=z, r1=1, r2=0, r3=0, length=0.0, radius=c.WHEEL_RADIUS/10.0, r=0, g=0, b=0)

                self.sim.Send_Joint(ID = 4, firstObjectID=8, secondObjectID=9, x=x, y=y, z=z, n1=1, n2=0, n3=0, lo=0,hi=0 )

        	self.sim.Send_Ray_Sensor(ID=0, objectIndex=9, x=x,y=y,z=z, r1=0,r2=1,r3=0)

	def Add_Left_Light_Sensor(self):

        	self.sim.Send_Light_Sensor(ID=2, objectIndex = 9 )

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

                self.sim.Send_Cylinder(ID=10, x=x, y=y, z=z, r1=1, r2=0, r3=0, length=0.0, radius=c.WHEEL_RADIUS/10.0, r=0, g=0, b=0)

                self.sim.Send_Joint(ID = 5, firstObjectID=8, secondObjectID=10, x=x, y=y, z=z, n1=1, n2=0, n3=0, lo=0,hi=0 )

                self.sim.Send_Ray_Sensor(ID=1, objectIndex=10, x=x,y=y,z=z, r1=0,r2=1,r3=0)

        def Add_Right_Light_Sensor(self):

                self.sim.Send_Light_Sensor(ID=3, objectIndex = 10 )

	def Add_Sensor_Neurons(self):

		for s in range(0,c.NUM_SENSORS):

			self.sim.Send_Sensor_Neuron(ID=s, sensorID=s, layer=0 )

	def Add_Synapses(self,sh,hm):

		for s in range(0,c.NUM_SENSORS):

			for h in range(0,c.NUM_HIDDEN_NEURONS):

				wt = sh[s,h] 

				self.sim.Send_Synapse(sourceNeuronIndex = s , targetNeuronIndex = c.NUM_SENSORS + h , weight = wt ) 

		for h in range(0,c.NUM_HIDDEN_NEURONS):

			for m in range(0,c.NUM_MOTORS):

				wt = hm[h,m]

                                self.sim.Send_Synapse(sourceNeuronIndex = c.NUM_SENSORS + h , targetNeuronIndex = c.NUM_SENSORS + c.NUM_HIDDEN_NEURONS + m , weight = wt )
	
        def Connect_Back_Wheel_To_Chassis(self):

                x = self.robotPosX

                y = self.robotPosY - c.ROBOT_LENGTH/2.0

                z = c.WHEEL_RADIUS

                self.sim.Send_Joint(ID = 2, firstObjectID=6, secondObjectID=7, x=x, y=y, z=z, n1=1, n2=0, n3=0)

                self.sim.Send_Joint(ID = 3, firstObjectID=7, secondObjectID=8, x=x, y=y, z=z, n1=0, n2=1, n3=0)

	def Connect_Left_Wheel_To_Chassis(self):

                x = self.robotPosX - c.ROBOT_WIDTH/2.0

                y = self.robotPosY + c.ROBOT_LENGTH/2.0

                z = c.WHEEL_RADIUS

		self.sim.Send_Joint(ID = 0, firstObjectID=4, secondObjectID=8, x=x, y=y, z=z, n1=1, n2=0, n3=0, lo=-c.WHEEL_SPEED, hi=+c.WHEEL_SPEED)

        def Connect_Right_Wheel_To_Chassis(self):

                x = self.robotPosX + c.ROBOT_WIDTH/2.0

                y = self.robotPosY + c.ROBOT_LENGTH/2.0

                z = c.WHEEL_RADIUS

                self.sim.Send_Joint(ID = 1, firstObjectID=5, secondObjectID=8, x=x, y=y, z=z, n1=1, n2=0, n3=0, lo=-c.WHEEL_SPEED, hi=+c.WHEEL_SPEED)

	def Send_Back_Wheel(self):

        	x = self.robotPosX

        	y = self.robotPosY - c.ROBOT_LENGTH/2.0

        	z = c.WHEEL_RADIUS

        	self.sim.Send_Cylinder(ID=6, x=x, y=y, z=z, r1=1, r2=0, r3=0, length=0.0, radius=c.WHEEL_RADIUS, r=1, g=1, b=1)

	        self.sim.Send_Cylinder(ID=7, x=x, y=y, z=z, r1=0, r2=1, r3=0, length=0.0, radius=c.WHEEL_RADIUS/2.0, r=0, g=1, b=0)

	def Send_Chassis(self):

        	x = self.robotPosX

        	y = self.robotPosY

        	z = c.WHEEL_RADIUS + c.ROBOT_HEIGHT/2

        	self.sim.Send_Box(ID=7, x=x, y=y, z=z, length=c.ROBOT_WIDTH, width=c.ROBOT_LENGTH, height=c.ROBOT_HEIGHT, r=1, g=1, b=1)

	def Send_Left_Wheel(self):

        	x = self.robotPosX - c.ROBOT_WIDTH/2.0

        	y = self.robotPosY + c.ROBOT_LENGTH/2.0

        	z = c.WHEEL_RADIUS

        	self.sim.Send_Cylinder(ID=4, x=x, y=y, z=z, r1=1, r2=0, r3=0, length=0.0, radius=c.WHEEL_RADIUS, r=1, g=1, b=1)

	def Send_Right_Wheel(self):

        	x = self.robotPosX + c.ROBOT_WIDTH/2.0

        	y = self.robotPosY + c.ROBOT_LENGTH/2.0

        	z = c.WHEEL_RADIUS

        	self.sim.Send_Cylinder(ID=5, x=x, y=y, z=z, r1=1, r2=0, r3=0, length=0.0, radius=c.WHEEL_RADIUS, r=1, g=1, b=1)

