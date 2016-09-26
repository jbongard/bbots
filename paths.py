import constants as c

class PATHS:

        def __init__(self):

		self.paths = {}

	def Convert_Binary_To_Decimal(self,b):

		if ( (b[0]==0) and (b[1]==0) and (b[2]==0) and (b[3]==0) ):

			return 0

                if ( (b[0]==0) and (b[1]==0) and (b[2]==0) and (b[3]==1) ):

                        return 1

                if ( (b[0]==0) and (b[1]==0) and (b[2]==1) and (b[3]==0) ):

                        return 2 

                if ( (b[0]==0) and (b[1]==0) and (b[2]==1) and (b[3]==1) ):

                        return 3 

                if ( (b[0]==0) and (b[1]==1) and (b[2]==0) and (b[3]==0) ):

                        return 4

                if ( (b[0]==0) and (b[1]==1) and (b[2]==0) and (b[3]==1) ):

                        return 5

                if ( (b[0]==0) and (b[1]==1) and (b[2]==1) and (b[3]==0) ):

                        return 6

                if ( (b[0]==0) and (b[1]==1) and (b[2]==1) and (b[3]==1) ):

                        return 7

                if ( (b[0]==1) and (b[1]==0) and (b[2]==0) and (b[3]==0) ):

                        return 8

                if ( (b[0]==1) and (b[1]==0) and (b[2]==0) and (b[3]==1) ):

                        return 9

                if ( (b[0]==1) and (b[1]==0) and (b[2]==1) and (b[3]==0) ):

                        return 10

                if ( (b[0]==1) and (b[1]==0) and (b[2]==1) and (b[3]==1) ):

                        return 11

                if ( (b[0]==1) and (b[1]==1) and (b[2]==0) and (b[3]==0) ):

                        return 12

                if ( (b[0]==1) and (b[1]==1) and (b[2]==0) and (b[3]==1) ):

                        return 13

                if ( (b[0]==1) and (b[1]==1) and (b[2]==1) and (b[3]==0) ):

                        return 14

                if ( (b[0]==1) and (b[1]==1) and (b[2]==1) and (b[3]==1) ):

                        return 15

	def Convert_Bases_To_Paths(self,bases):

		for p in range(0,c.MAX_THREADS):

			self.paths[p] = self.Convert_Bases_To_Path(p,bases)

	def Convert_Bases_To_Path(self,p,bases):

		path = []

		for b in range(0,c.BASES_PER_THREAD,4):

			baseIndex = p*c.BASES_PER_THREAD + b

			decimal = self.Convert_Binary_To_Decimal(bases[baseIndex:baseIndex+4])

			if ( decimal < 10 ):

				path.append(decimal)

		return path

	def Get_Path(self,p):

		return self.paths[p]

	def Print(self):

		for p in range(0,c.MAX_THREADS):

			print self.paths[p]
