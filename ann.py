import constants as c

class ANN:

        def __init__(self):

		pass

	def Convert_Threads_To_ANN(self,threads):

		self.numSensorNeurons = c.NUM_SENSORS	

		self.numHiddenNeurons = c.NUM_HIDDEN_NEURONS

		self.numMotorNeurons = c.NUM_MOTORS

		for t in range(0,threads.numThreads):

			wires = threads.threads[t]

			for w in range(0,wires.numWires):

				if ( wires.From_Sensor_To_Motor(w) ):

					self.numHiddenNeurons = self.numHiddenNeurons + 1

		self.Print()

	def Print(self):

		print ''

		print self.numSensorNeurons

                print self.numHiddenNeurons

                print self.numMotorNeurons

