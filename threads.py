import constants as c
import pickle
import os

class THREADS:

        def __init__(self):

                self.threads = {}
	
		self.numThreads = 0

	def Append(self,thread):

		self.threads[self.numThreads] = thread

		self.numThreads = self.numThreads + 1

	def Contains_Max_Thread_Length(self):

		longestThreadLength = 0

		for t in range(0,self.numThreads):

			threadLength = self.threads[t].Get_Length()

			if ( threadLength > longestThreadLength ):

				longestThreadLength = threadLength

		return ( longestThreadLength == c.MAX_WIRES_PER_THREAD )

	def Contains_Wire_From_Sensor_To_Motor(self):

		found = False

                for t in range(0,self.numThreads):

                        wires = self.threads[t]

                        for w in range(0,wires.numWires):

                                if ( wires.From_Sensor_To_Motor(w) ):

					found = True

		return found 


	def Draw(self):

		for t in range(0,self.numThreads):

			self.threads[t].Draw()

        def Load(self):

                f = open('threads.p','rb')

                self = pickle.load(f)

                f.close()

                return self

	def Num_Threads(self):

		return self.numThreads

	def Print(self):

		print 'num threads: ' + str(self.numThreads)

		for t in range(0,self.numThreads):

			print 'thread'+str(t)+': '+ str(self.threads[t].numWires)

			#self.threads[t].Print()

        def Save(self):

                f = open('tmp.p','wb')

                pickle.dump(self,f)

                f.close()

                os.rename('tmp.p','threads.p')

