import constants as c
import numpy as np

class ANN:

        def __init__(self):

		self.sh = np.zeros((c.NUM_SENSORS,c.NUM_HIDDEN_NEURONS),dtype='f')

		self.sm = np.zeros((c.NUM_SENSORS,c.NUM_MOTORS),dtype='f')

		self.hh = np.zeros((c.NUM_HIDDEN_NEURONS,c.NUM_HIDDEN_NEURONS),dtype='f')

                self.hm = np.zeros((c.NUM_HIDDEN_NEURONS,c.NUM_MOTORS),dtype='f')

        def Compute_Additional_Required_Hidden_Neurons(self):

                self.additionalHiddenNeurons = np.count_nonzero( self.sm )

	def Convert_Threads_To_Synapses(self,threads):

		self.Compute_Additional_Required_Hidden_Neurons()

                for t in range(0,threads.numThreads):

                        wires = threads.threads[t]

                        for w in range(0,wires.numWires):

				if ( wires.Convertable_Wire(w) ):

					self.Convert_Wire_To_Synapse(wires,w)

	def Convert_Wire_To_Synapse(self,wires,w):

		if ( wires.From_Sensor_To_Hidden(w) ):

			self.Convert_Wire_To_SH_Synapse(wires,w)

		if ( wires.From_Sensor_To_Motor(w) ):

                        self.Convert_Wire_To_SM_Synapse(wires,w)

                elif ( wires.From_Hidden_To_Hidden(w) ):

                        self.Convert_Wire_To_HH_Synapse(wires,w)

                elif ( wires.From_Hidden_To_Motor(w) ):

                        self.Convert_Wire_To_HM_Synapse(wires,w) 

	def Convert_Wire_To_SH_Synapse(self,wires,w):

		i = wires.Get_From_Sensor_Index(w)

		j = wires.Get_To_Hidden_Index(w)

		self.sh[i,j] = self.sh[i,j] + wires.Get_Weight(w)

        def Convert_Wire_To_SM_Synapse(self,wires,w):

                i = wires.Get_From_Sensor_Index(w)

                j = wires.Get_To_Motor_Index(w)

                self.sm[i,j] = self.sm[i,j] + wires.Get_Weight(w)

        def Convert_Wire_To_HH_Synapse(self,wires,w):

                i = wires.Get_From_Hidden_Index(w)

                j = wires.Get_To_Hidden_Index(w)

                self.hh[i,j] = self.hh[i,j] + wires.Get_Weight(w)

        def Convert_Wire_To_HM_Synapse(self,wires,w):

                i = wires.Get_From_Hidden_Index(w)

                j = wires.Get_To_Motor_Index(w)

                self.hm[i,j] = self.hm[i,j] + wires.Get_Weight(w)

	def Get_SH_Weight(self,s,h):

		return self.sh[s,h]

        def Get_SM_Weight(self,s,m):

                return self.sm[s,m]

        def Get_HH_Weight(self,h1,h2):

                return self.hh[h1,h2]

        def Get_HM_Weight(self,h,m):

                return self.hm[h,m]

	def Number_Of_Synapses(self):

		return np.count_nonzero(self.sh) + np.count_nonzero(self.sm) + np.count_nonzero(self.hh) + np.count_nonzero(self.hm)

		# return np.count_nonzero(self.sm)

	def Print(self):

		print self.sh

		print self.sm

		print self.hh

		print self.hm
