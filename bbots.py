import sys
import random
import numpy as np

import constants as c

from afpo import AFPO

# --------------------- Main function ------------------

randomSeed = 0

EO_OR_GO = c.GO

numberOfCommandLineArguments = len(sys.argv)

if ( numberOfCommandLineArguments > 1 ):

	randomSeed = int( sys.argv[1] )

if ( numberOfCommandLineArguments > 2 ):

	if ( sys.argv[2] == 'GO' ):

		EO_OR_GO = c.GO
	else:
		EO_OR_GO = c.EO

random.seed(randomSeed)

np.random.seed(randomSeed)

afpo = AFPO()

afpo.Evolve(EO_OR_GO)
