import os
import pickle
from wires import WIRES
import constants as c
import matplotlib.pyplot as plt

wires = WIRES()

wires = wires.Load()

wires.Draw()

plt.show()
