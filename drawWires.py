import os
import pickle
from wires import WIRES
import matplotlib.pyplot as plt
import constants as c

wires = WIRES()

wires = wires.Load()

fig = plt.figure()

ax = plt.subplot(111)

for j in range(0,4):

	plt.text(j , c.NUM_PIN_GROUP_ROWS - c.BL , 'BL,'+str(j) )

        plt.text(j , c.NUM_PIN_GROUP_ROWS - c.FL , 'FL,'+str(j) )

        plt.text(j , c.NUM_PIN_GROUP_ROWS - c.BR , 'BR,'+str(j) )

        plt.text(j , c.NUM_PIN_GROUP_ROWS - c.FR , 'FR,'+str(j) )

for j in range(0,7):

	plt.text(j , c.NUM_PIN_GROUP_ROWS - c.N1, 'N1,'+str(j) )

        plt.text(j , c.NUM_PIN_GROUP_ROWS - c.N2, 'N2,'+str(j) )

        plt.text(j , c.NUM_PIN_GROUP_ROWS - c.N3, 'N3,'+str(j) )

        plt.text(j , c.NUM_PIN_GROUP_ROWS - c.N4, 'N4,'+str(j) )

        plt.text(j , c.NUM_PIN_GROUP_ROWS - c.N5, 'N5,'+str(j) )

        plt.text(j , c.NUM_PIN_GROUP_ROWS - c.N6, 'N6,'+str(j) )

for j in range(0,6):

        plt.text(j , c.NUM_PIN_GROUP_ROWS - c.PL, 'PL,'+str(j) )

        plt.text(j , c.NUM_PIN_GROUP_ROWS - c.RL, 'RL,'+str(j) )

        plt.text(j , c.NUM_PIN_GROUP_ROWS - c.RR, 'RR,'+str(j) )

        plt.text(j , c.NUM_PIN_GROUP_ROWS - c.PR, 'PR,'+str(j) )

for w in range(0,wires.numWires):

	wire = wires.wires[w]

	start = wire[0]
	end = wire[1]
	weight = wire[2]

	print start, end, weight

	plt.plot([start[0],end[0]],[c.NUM_PIN_GROUP_ROWS-start[1],c.NUM_PIN_GROUP_ROWS-end[1]],'r-')

ax.set_xlim(-1 , c.MAX_PINS_PER_ROW)

ax.set_ylim(0 , c.NUM_PIN_GROUP_ROWS+1)

yticks = ax.get_yticks()

ax.set_xticks([])
ax.set_yticks([])

plt.show()
