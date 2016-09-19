from threads import THREADS

import matplotlib.pyplot as plt

threads = THREADS()

threads = threads.Load()

threads.Print()

threads.Draw()

plt.show()
