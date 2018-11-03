import sys
from PIL import Image
import numpy as np

import vornoi
import fitness as fit

img = Image.open(sys.argv[1])
orignal_rgb = np.array(img)

class Individual:

    def __init__(self, n):
        print("Individual Initialised")
        self.fitness = 0
        #Create Vornoi Diagram (basic structure)
        self.vor = vornoi.vornoiWireFrame(n)

    def calc_fitness(self):
        #draw image on canvas and get fitness wrt original image
        vornoi_image = vornoi.drawVornoi(self.vor)
        vornoi_image = np.array(vornoi_image)

        #calculate fitness
        self.fitness = fit.calFitness(orignal_rgb, vornoi_image)s

class Population:

    def __init__(self, pop_size):
        print("Initialising Population")
        self.pop_size = pop_size
        self.individuals = [Individual(500) for i in range(self.pop_size)]
        print("Population Initialised")

    def calculate_fitness(self):
        for i in range(self.pop_size):
            self.individuals[i].calc_fitness()

        #sort individuals on the basis of fitness
        self.individuals.sort(key = lambda x:x.fitness)

        #store the maximum fitness
        self.max_fitness = self.individuals[self.pop_size-1].fitness


population = Population(100)
population.calculate_fitness()

print(population)
