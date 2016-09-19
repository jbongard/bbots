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

	def Draw(self):

		for t in range(0,self.numThreads):

			self.threads[t].Draw()

        def Load(self):

                f = open('threads.p','rb')

                self = pickle.load(f)

                f.close()

                return self

	def Print(self):

		print self.numThreads

        def Save(self):

                f = open('tmp.p','wb')

                pickle.dump(self,f)

                f.close()

                os.rename('tmp.p','threads.p')

