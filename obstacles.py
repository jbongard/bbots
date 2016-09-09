import constants as c

class OBSTACLES:

        def __init__(self):

		pass

	def Send_To_Sim(self,sim):

        	sim.Send_Box(ID=0, x=0, y=0, z=c.OBSTACLE_HEIGHT/2.0, length=c.OBSTACLE_WIDTH, width=c.OBSTACLE_LENGTH, height=c.OBSTACLE_HEIGHT, r=.5, g=.5, b=.5)

        	sim.Send_Box(ID=1, x=-c.OBSTACLE_WIDTH, y=-3.0*c.OBSTACLE_LENGTH, z=c.OBSTACLE_HEIGHT/2.0, length=c.OBSTACLE_WIDTH, width=c.OBSTACLE_LENGTH, height=c.OBSTACLE_HEIGHT, r=.5, g=.5, b=.5)

        	sim.Send_Box(ID=2, x=+c.OBSTACLE_WIDTH, y=-3.0*c.OBSTACLE_LENGTH, z=c.OBSTACLE_HEIGHT/2.0, length=c.OBSTACLE_WIDTH, width=c.OBSTACLE_LENGTH, height=c.OBSTACLE_HEIGHT, r=.5, g=.5, b=.5)

        	sim.Send_Box(ID=3, x=0, y=5.0*c.OBSTACLE_LENGTH, z=c.LIGHT_SOURCE_HEIGHT/2.0, length=c.OBSTACLE_WIDTH, width=c.OBSTACLE_LENGTH, height=c.LIGHT_SOURCE_HEIGHT, r=1, g=1, b=1)
