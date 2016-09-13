from pyrosim import PYROSIM

from obstacles import OBSTACLES

from robot import ROBOT

import constants as c

def Perform_Simulation():

	sims = {}

	for e in range(0,c.NUM_ENVIRONMENTS):

		sims[e] = PYROSIM(playBlind = True, playPaused = False)

		obstacles = OBSTACLES()

		obstacles.Send_To_Sim(sims[e])

		robot = ROBOT()

		robot.Send_To_Sim(sims[e])

		sims[e].Start()

        for e in range(0,c.NUM_ENVIRONMENTS):

		sims[e].Wait_To_Finish()

# --------------------- Main function ------------------

for s in range(0,10):

	Perform_Simulation()

