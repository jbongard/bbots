import sys
from obstacles import OBSTACLES
import constants
from genome import GENOME
import random
import copy
import numpy as np
import pickle
import os

class AFPO:

        def __init__(self,randomSeed,EO_OR_GO):

		self.randomSeed = randomSeed

		self.EO_OR_GO = EO_OR_GO

		random.seed(self.randomSeed)

		np.random.seed(self.randomSeed)

		self.failures = np.zeros(8,dtype='d')

                self.obstacles = OBSTACLES()

		self.bestFitnesses = np.zeros(constants.NUM_GENERATIONS)

                self.genomes = {}

                self.nextAvailableID = 0

                self.numNonDominated = 0

                for g in range(0,constants.popSize):

                        self.genomes[g] = GENOME(self.nextAvailableID)

                        self.nextAvailableID = self.nextAvailableID + 1

        def Evolve(self,EO_OR_GO):

                self.Evaluate_All(EO_OR_GO)

                for self.g in range(0,constants.NUM_GENERATIONS):

			if ( EO_OR_GO == constants.GO ):

                        	print 'GO: ' + str(self.g) + ' ' + str(constants.NUM_GENERATIONS)
			else:
                                print 'EO: ' + str(self.g) + ' ' + str(constants.NUM_GENERATIONS)


                        self.Advance_One_Generation(EO_OR_GO)

	def Save_Fitnesses(self):

                f = open('Data/tmp'+str(self.randomSeed)+'_'+str(self.EO_OR_GO)+'.txt','wb')

                pickle.dump(self.bestFitnesses,f)

                f.close()

                os.rename('Data/tmp'+str(self.randomSeed)+'_'+str(self.EO_OR_GO)+'.txt','Data/best'+str(self.randomSeed)+'_'+str(self.EO_OR_GO)+'.p')

# -------------- Private methods -----------------------

	def Advance_One_Generation(self,EO_OR_GO):

                self.Find_Pareto_Front()

                self.Sort_By_Dominated()

                self.Count_NonDominated_Solutions()

		self.Sort_NonDominated_By_Fitness()

		# self.Print_Best()

		self.Save_Best()

		#self.Save_Random_Robot_From_Pareto_Front()

                self.Delete_Dominated_Solutions()

                self.Print()

                self.Age_NonDominated_Solutions()

                self.Fill()

                self.Evaluate_All(EO_OR_GO)

	def Age_NonDominated_Solutions(self):

		for g in range(0,constants.popSize):

			if ( g in self.genomes ):

				self.genomes[g].Age()

	def Count_NonDominated_Solutions(self):

		self.numNonDominated = 0

		for g in range(0,constants.popSize):

			if ( self.genomes[g].Get_Dominated() == False ):

				self.numNonDominated = self.numNonDominated + 1

	def Delete_Dominated_Solutions(self):

		for g in range(self.numNonDominated,constants.popSize):

			del self.genomes[g]

	def Display_Best(self):

		self.genomes[0].Display()

	def Evaluate_All(self,EO_OR_GO):

		runningGenome = self.numNonDominated

		self.genomes[runningGenome].Start(self.obstacles,playBlind=True,playPaused=False,failures=self.failures,experimentalRegime=EO_OR_GO)

		while ( (runningGenome+1) < constants.popSize ):

			self.genomes[runningGenome+1].Start(self.obstacles,playBlind=True,playPaused=False,failures=self.failures,experimentalRegime=EO_OR_GO)

			self.genomes[runningGenome].End()

			runningGenome = runningGenome + 1

		self.genomes[constants.popSize-1].End()

	def Fill(self):

		self.Spawn_Mutants_From_Pareto_Front()

		self.Inject_New_Genome()

	def Find_Pareto_Front(self):

		self.Make_All_Genomes_NonDominated()

		for i in range(0,constants.popSize):

			for j in range(0,constants.popSize):

				if ( i != j ):

					j_dominates_i = self.genomes[j].Dominates( self.genomes[i] )

					if ( j_dominates_i ):

						self.genomes[i].Set_Dominated( True )

	def Inject_New_Genome(self):

		self.genomes[constants.popSize-1] = GENOME(self.nextAvailableID)

		self.nextAvailableID = self.nextAvailableID + 1

	def Make_All_Genomes_NonDominated(self):

		for g in range(0,constants.popSize):

			self.genomes[g].Set_Dominated(False)

	def Print(self):

		for g in range(0,constants.popSize):

			if ( g in self.genomes ):

				self.genomes[g].Print()		

		# print self.failures

		print ''

	def Print_Best(self):

		self.genomes[0].ann.Print()

	def Save_Best(self):

		self.bestFitnesses[self.g] = self.genomes[0].fitness

		self.genomes[0].Save(self.randomSeed,self.EO_OR_GO)

	def Save_Random_Robot_From_Pareto_Front(self):

		selectedGenome = random.randint(0,self.numNonDominated-1)

		self.genomes[selectedGenome].Save()

		
	def Sort_By_Dominated(self):

		length = len(self.genomes) - 1

		sorted = False

		while not sorted:

			sorted = True

			for i in range(length):

				if ( (self.genomes[i].Get_Dominated()==True) and (self.genomes[i+1].Get_Dominated()==False) ):

					sorted = False

					self.genomes[i], self.genomes[i+1] = self.genomes[i+1], self.genomes[i]

        def Sort_NonDominated_By_Fitness(self):

                length = self.numNonDominated - 1

                sorted = False

                while not sorted:

                        sorted = True

                        for i in range(length):

                                if ( self.genomes[i].fitness > self.genomes[i+1].fitness ):

                                        sorted = False

                                        self.genomes[i], self.genomes[i+1] = self.genomes[i+1], self.genomes[i]


        def Spawn_Mutants_From_Pareto_Front(self):

                for g in range(self.numNonDominated,constants.popSize-1):

                        genomeIndexToCopy = random.randint(0,self.numNonDominated-1)

                        self.genomes[g] = copy.deepcopy( self.genomes[genomeIndexToCopy] )

			self.genomes[g].ID = self.nextAvailableID

			self.nextAvailableID = self.nextAvailableID + 1

                        self.genomes[g].Mutate()

                        self.genomes[g].Reset()
