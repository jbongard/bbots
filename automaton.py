import numpy as np
import constants as c
import random
from wires import WIRES

class AUTOMATON:

        def __init__(self):

		self.path = np.random.randint(0,10,[c.MAX_WIRES_PER_THREAD,4])

	def Add_Thread(self,pins,threads):

		thread = WIRES()

		print ''

		self.Set_Starting_Position()

		self.success = self.Handle_Starting_Position(pins)

		if ( self.success == False ):

			return False

		self.w = 0

		while ( (self.w <  c.MAX_WIRES_PER_THREAD) and self.success ):

			self.success = self.Attempt_To_Create_Wire(pins,thread)

			if ( self.success ):

				self.w = self.w + 1

		threads.Append(thread)

	def Attempt_To_Create_Wire(self,pins,thread):

		success = self.Set_Direction()

		if ( success == False ):

			return False

		self.Enforce_Forward_Movement()

		self.Set_Distance()

		self.Compute_Target_Position()

		success = self.Handle_Ending_Position(pins)

		if ( success == False ):

			return False
	 
		thread.Add_Wire([self.xStart,self.yStart],[self.xEnd,self.yEnd],1,pins)

		return self.Set_Next_Position(pins)

	def Compute_Target_Position(self):

		if ( self.direction == c.RIGHT ):

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

        def End_Position_Equals_Start_Position(self):

                return ( ( self.xStart == self.xEnd ) and ( self.yStart == self.yEnd ) )

	def Enforce_Forward_Movement(self):

		if ( self.direction == c.UP_LEFT ):

			self.direction = c.DOWN_LEFT

		if ( self.direction == c.UP ):

			self.direction = c.DOWN

		if ( self.direction == c.UP_RIGHT ):

			self.direction = c.DOWN_RIGHT

        def Handle_Ending_Position(self,pins):

                if ( pins.Invalid_Pin([self.xEnd,self.yEnd]) ):

                        return False

                if ( pins.Occupied_Pin([self.xEnd,self.yEnd]) or self.End_Position_Equals_Start_Position() ):

                        # return False # for destructive interaction case

                        if ( pins.Pin_Group_Full(self.yEnd) ):

                                return False
                        else:
                                self.xEnd = self.Move_X(self.xEnd,self.yEnd,pins)

        			while ( self.End_Position_Equals_Start_Position() ):

					self.xEnd = self.Move_X(self.xEnd,self.yEnd,pins)

		return True

        def Handle_Starting_Position(self,pins):

                if ( pins.Invalid_Pin([self.xStart,self.yStart]) ):

                        return False

                if ( pins.Occupied_Pin([self.xStart,self.yStart]) ):

                        # return False # for destructive interaction case

                        if ( pins.Pin_Group_Full(self.yStart) ):

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

                self.direction = self.path[self.w,2]

		return self.Valid_Direction()

        def Set_Distance(self):

                self.distance = self.path[self.w,3]

        def Set_Next_Position(self,pins):

		self.xStart = self.xEnd

                self.yStart = self.yEnd

		return self.Handle_Starting_Position(pins)

        def Set_Starting_Position(self):

                self.xStart = self.path[0,0]

                self.yStart = self.path[0,1]

        def Valid_Direction(self):

                return ( self.direction <= c.UP_LEFT )