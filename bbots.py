from pyrosim import PYROSIM

from obstacles import OBSTACLES

from robot import ROBOT

import constants as c

def Send_Back_Wheel(sim,robotPosX,robotPosY):

        leftWheelX = robotPosX

        leftWheelY = robotPosY - c.ROBOT_LENGTH/2.0

        leftWheelZ = c.WHEEL_RADIUS

        sim.Send_Cylinder(ID=6, x=leftWheelX, y=leftWheelY, z=leftWheelZ, r1=1, r2=0, r3=0, length=0.0, radius=c.WHEEL_RADIUS, r=1, g=1, b=1)

def Send_Chassis(sim,robotPosX,robotPosY):

        x = robotPosX

        y = robotPosY

        z = c.WHEEL_RADIUS + c.ROBOT_HEIGHT/2

        sim.Send_Box(ID=7, x=x, y=y, z=z, length=c.ROBOT_WIDTH, width=c.ROBOT_LENGTH, height=c.ROBOT_HEIGHT, r=1, g=1, b=1)

def Send_Left_Wheel(sim,robotPosX,robotPosY):

	leftWheelX = robotPosX - c.ROBOT_WIDTH/2.0

	leftWheelY = robotPosY + c.ROBOT_LENGTH/2.0  

	leftWheelZ = c.WHEEL_RADIUS

	sim.Send_Cylinder(ID=4, x=leftWheelX, y=leftWheelY, z=leftWheelZ, r1=1, r2=0, r3=0, length=0.0, radius=c.WHEEL_RADIUS, r=1, g=1, b=1)

def Send_Right_Wheel(sim,robotPosX,robotPosY):

        leftWheelX = robotPosX + c.ROBOT_WIDTH/2.0

        leftWheelY = robotPosY + c.ROBOT_LENGTH/2.0

        leftWheelZ = c.WHEEL_RADIUS

        sim.Send_Cylinder(ID=5, x=leftWheelX, y=leftWheelY, z=leftWheelZ, r1=1, r2=0, r3=0, length=0.0, radius=c.WHEEL_RADIUS, r=1, g=1, b=1)

def Send_Robot(sim):

        robotPosX = -c.OBSTACLE_WIDTH

        robotPosY = -6.0 * c.OBSTACLE_LENGTH

        Send_Left_Wheel(sim,robotPosX,robotPosY)

        Send_Right_Wheel(sim,robotPosX,robotPosY)

        Send_Back_Wheel(sim,robotPosX,robotPosY)

        Send_Chassis(sim,robotPosX,robotPosY)

# ------------- Main function --------------

sim = PYROSIM(playPaused = False)

obstacles = OBSTACLES()

obstacles.Send_To_Sim(sim)

robot = ROBOT()

robot.Send_To_Sim(sim)

#Send_Obstacles(sim)

#Send_Robot(sim)

sim.Start()
