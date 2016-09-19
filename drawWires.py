import os
import pickle
from wires import WIRES
import constants as c
import matplotlib.pyplot as plt

for i in range(0,1):

	wires = WIRES()

	wires = wires.Load(i)

	wires.Draw(i)

	plt.show()
