import numpy as np
import constants as c
import random
from wires import WIRES

class AUTOMATON:

        def __init__(self,path):

		self.path = path 

		self.pathIndex = 0

	def Add_Thread(self,pins,threads,failures):

		thread = WIRES()

		self.success = self.Set_Starting_Position()

		if ( self.success == False ):

			failures[0] = failures[0] + 1
			return False

		self.success = self.Handle_Starting_Position(pins,failures)

		if ( self.success == False ):

			failures[1] = failures[1] + 1
			return False

		while ( self.Bases_Remain() and self.success ):

			self.success = self.Attempt_To_Create_Wire(pins,thread,failures)

		if ( thread.numWires > 0 ):

			threads.Append(thread)

	def Attempt_To_Create_Wire(self,pins,thread,failures):

		success = self.Set_Direction()

		if ( success == False ):

			failures[3] = failures[3] + 1
			return False

		# self.Enforce_Forward_Movement()

		success = self.Set_Distance()

		if ( success == False ):

			failures[4] = failures[4] + 1
			return False

		self.Compute_Target_Position()

		success = self.Handle_Ending_Position(pins,failures)

		if ( success == False ):

			return False
	
		[success,wt] = self.Get_Weight()

		if ( success == False ):

			failures[7] = failures[7] + 1

			return False
 
		thread.Add_Wire([self.xStart,self.yStart],[self.xEnd,self.yEnd],wt,pins)

		return self.Set_Next_Position(pins,failures)

	def Bases_Remain(self):

                return ( self.pathIndex < len(self.path) )

	def Compute_Target_Position(self):

                if ( self.direction == c.UP ):

                        self.xEnd = self.xStart

                        self.yEnd = self.yStart - self.distance

                elif ( self.direction == c.UP_RIGHT ):

                        self.xEnd = self.xStart + self.distance

                        self.yEnd = self.yStart - self.distance

		elif ( self.direction == c.RIGHT ):

			self.xEnd = self.xStart + self.distance

			self.yEnd = self.yStart

                elif ( self.direction == c.DOWN_RIGHT ):

                        self.xEnd = self.xStart + self.distance

                        self.yEnd = self.yStart + self.distance

                elif ( self.direction == c.DOWN ):

			self.xEnd = self.xStart

                        self.yEnd = self.yStart + self.distance

                elif ( self.direction == c.DOWN_LEFT ):

                        self.xEnd = self.xStart - self.distance

                        self.yEnd = self.yStart + self.distance

                elif ( self.direction == c.LEFT ):

                        self.xEnd = self.xStart - self.distance

			self.yEnd = self.yStart

                elif ( self.direction == c.UP_LEFT ):

                        self.xEnd = self.xStart - self.distance

                        self.yEnd = self.yStart - self.distance

        def End_Position_Equals_Start_Position(self):

                return ( ( self.xStart == self.xEnd ) and ( self.yStart == self.yEnd ) )

	def Enforce_Forward_Movement(self):

		if ( self.direction == c.UP_LEFT ):

			self.direction = c.DOWN_LEFT

		if ( self.direction == c.UP ):

			self.direction = c.DOWN

		if ( self.direction == c.UP_RIGHT ):

			self.direction = c.DOWN_RIGHT

        def Get_Weight(self):

		w = 0.0

		if ( self.Bases_Remain() == False ):

			return False , w

		if ( self.path[self.pathIndex] == 0 ):

			w = -0.5

                elif ( self.path[self.pathIndex] == 1 ):

                        w = -0.4

                elif ( self.path[self.pathIndex] == 2 ):

                        w = -0.3

                elif ( self.path[self.pathIndex] == 3 ):

                        w = -0.2

                elif ( self.path[self.pathIndex] == 4 ):

                        w = -0.1

                elif ( self.path[self.pathIndex] == 5 ):

                        w = +0.1

                elif ( self.path[self.pathIndex] == 6 ):

                        w = +0.2

                elif ( self.path[self.pathIndex] == 7 ):

                        w = +0.3

                elif ( self.path[self.pathIndex] == 8 ):

                        w = +0.4

                else:
                        w= +0.5

		self.pathIndex = self.pathIndex + 1

		return True , w

        def Handle_Ending_Position(self,pins,failures):

                if ( pins.Invalid_Pin([self.xEnd,self.yEnd]) ):

			failures[5] = failures[5] + 1

                        return False

                if ( pins.Occupied_Pin([self.xEnd,self.yEnd]) or self.End_Position_Equals_Start_Position() ):

                        # return False # for destructive interaction case

			minimumFreePins = 1

			if ( self.Start_And_End_On_Same_Row() ):

				minimumFreePins = 2

                        if ( pins.Free_Pins_In_Row(self.yEnd) < minimumFreePins ):

				failures[6] = failures[6] + 1

                                return False
                        else:
                                self.xEnd = self.Move_X(self.xEnd,self.yEnd,pins)

        			while ( self.End_Position_Equals_Start_Position() ):

					self.xEnd = self.Move_X(self.xEnd,self.yEnd,pins)

		return True

        def Handle_Starting_Position(self,pins,failures):

                if ( pins.Invalid_Pin([self.xStart,self.yStart]) ):

			failures[1] = failures[1] + 1

                        return False

                if ( pins.Occupied_Pin([self.xStart,self.yStart]) ):

                        # return False # for destructive interaction case

                        if ( pins.Pin_Group_Full(self.yStart) ):

				failures[2] = failures[2] + 1

                                return False
                        else:
                                self.xStart = self.Move_X(self.xStart,self.yStart,pins)

		return True

	def Move_X(self,x,y,pins):

		x = random.randint(0,c.PIN_COLUMNS-1)

		while ( pins.Occupied_Pin([x,y]) ):

			x = random.randint(0,c.PIN_COLUMNS-1)

		return x
 
        def Set_Direction(self):

		if ( self.Bases_Remain() ):
	
                	self.direction = self.path[self.pathIndex]
		else:
			return False

                self.pathIndex = self.pathIndex + 1

		return self.Valid_Direction()

        def Set_Distance(self):

		if ( self.Bases_Remain() ):

                	self.distance = self.path[self.pathIndex]
		else:
			return False

                self.pathIndex = self.pathIndex + 1

		return True

        def Set_Next_Position(self,pins,failures):

		self.xStart = self.xEnd

                self.yStart = self.yEnd

		return self.Handle_Starting_Position(pins,failures)

        def Set_Starting_Position(self):

		if ( self.Bases_Remain() ):

                	self.xStart = self.path[self.pathIndex]
		else:
			return False

		self.pathIndex = self.pathIndex + 1

                if ( self.Bases_Remain() ):

                	self.yStart = self.path[self.pathIndex]
		else:
			return False

                self.pathIndex = self.pathIndex + 1

		return True

	def Start_And_End_On_Same_Row(self):

		return ( self.yEnd == self.yStart )

        def Valid_Direction(self):

                return ( self.direction <= c.UP_LEFT )
