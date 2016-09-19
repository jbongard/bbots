import constants as c

class OBSTACLES:

        def __init__(self):

		pass

	def Send_To_Sim(self,sim):

        	sim.Send_Box(ID=c.NUM_ROBOT_PARTS+0, x=0, y=0, z=c.OBSTACLE_HEIGHT/2.0, length=c.OBSTACLE_WIDTH, width=c.OBSTACLE_LENGTH, height=c.OBSTACLE_HEIGHT, r=.5, g=.5, b=.5, partOfRobot=False, makeImmovable=True)

        	sim.Send_Box(ID=c.NUM_ROBOT_PARTS+1, x=-c.OBSTACLE_WIDTH, y=-3.0*c.OBSTACLE_LENGTH, z=c.OBSTACLE_HEIGHT/2.0, length=c.OBSTACLE_WIDTH, width=c.OBSTACLE_LENGTH, height=c.OBSTACLE_HEIGHT, r=.5, g=.5, b=.5, partOfRobot=False, makeImmovable=True)

        	sim.Send_Box(ID=c.NUM_ROBOT_PARTS+2, x=+c.OBSTACLE_WIDTH, y=-3.0*c.OBSTACLE_LENGTH, z=c.OBSTACLE_HEIGHT/2.0, length=c.OBSTACLE_WIDTH, width=c.OBSTACLE_LENGTH, height=c.OBSTACLE_HEIGHT, r=.5, g=.5, b=.5, partOfRobot=False, makeImmovable=True)

        	sim.Send_Box(ID=c.NUM_ROBOT_PARTS+3, x=0, y=5.0*c.OBSTACLE_LENGTH, z=c.LIGHT_SOURCE_HEIGHT/2.0, length=c.OBSTACLE_WIDTH, width=c.OBSTACLE_LENGTH, height=c.LIGHT_SOURCE_HEIGHT, r=1, g=1, b=1, partOfRobot=False, makeImmovable=True)

		sim.Send_Light_Source(objectIndex = c.NUM_ROBOT_PARTS+3 )

		sim.Send_Box(ID=c.NUM_ROBOT_PARTS+4, x=0, y=-c.BARRIER_LENGTH * c.OBSTACLE_LENGTH, z=c.OBSTACLE_HEIGHT/2.0, length=c.BARRIER_LENGTH*c.OBSTACLE_WIDTH, width=c.OBSTACLE_LENGTH, height=c.OBSTACLE_HEIGHT, r=.5, g=.5, b=.5, partOfRobot=False, makeImmovable=True)

                sim.Send_Box(ID=c.NUM_ROBOT_PARTS+5, x=0, y=+c.BARRIER_LENGTH * c.OBSTACLE_LENGTH, z=c.OBSTACLE_HEIGHT/2.0, length=c.BARRIER_LENGTH*c.OBSTACLE_WIDTH, width=c.OBSTACLE_LENGTH, height=c.OBSTACLE_HEIGHT, r=.5, g=.5, b=.5, partOfRobot=False, makeImmovable=True)

                sim.Send_Box(ID=c.NUM_ROBOT_PARTS+6, y=0, x=-c.BARRIER_LENGTH * c.OBSTACLE_LENGTH, z=c.OBSTACLE_HEIGHT/2.0,  width=c.BARRIER_LENGTH*c.OBSTACLE_WIDTH, length=c.OBSTACLE_LENGTH, height=c.OBSTACLE_HEIGHT, r=.5, g=.5, b=.5, partOfRobot=False, makeImmovable=True)

                sim.Send_Box(ID=c.NUM_ROBOT_PARTS+7, y=0, x=+c.BARRIER_LENGTH * c.OBSTACLE_LENGTH, z=c.OBSTACLE_HEIGHT/2.0,  width=c.BARRIER_LENGTH*c.OBSTACLE_WIDTH, length=c.OBSTACLE_LENGTH, height=c.OBSTACLE_HEIGHT, r=.5, g=.5, b=.5, partOfRobot=False, makeImmovable=True)

