import random
import copy
import numpy as np

from shape import *

class Individual:

    def __init__(self, length, shapetype):
        self.fitness = 0
        self.length = length
        temp = primitive[shapetype]
        instanceOf = temp.__class__
        self.genes = [instanceOf() for i in range(self.length)]

    def calc_fitness(self, orig_arr):
        x,y,z = np.shape(orig_arr)
        base = Image.new('RGB',(x,y), (0,0,0))
        for i in range(self.length):
            base = self.genes[i].draw(base)
        base_arr = np.array(base)
        self.fitness = -1*np.linalg.norm(orig_arr-base_arr)

class Population:

    def __init__(self, pop_size, individual_size, shapetype):
        self.pop_size = pop_size
        self.individuals = [Individual(individual_size, shapetype) for i in range(self.pop_size)]

    def calculate_fitness(self, orig_arr):
        for i in range(self.pop_size):
            self.individuals[i].calc_fitness(orig_arr)
        self.individuals.sort(key = lambda x:x.fitness)
        self.max_fitness = self.individuals[self.pop_size-1].fitness

    def selection(self):
        parents = []
        for i in range(10):
            parents.append(copy.deepcopy(self.individuals[i+self.pop_size-10]))
        return parents

    def changepopulation(self, offspring):
        for i in range(10):
            self.individuals[i] = copy.deepcopy(offspring)
        self.individuals.sort(key = lambda x:x.fitness)
        self.max_fitness = self.individuals[self.pop_size-1].fitness