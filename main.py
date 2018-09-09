import random
import copy
import numpy as np

from shape import *

class Individual:

    def __init__(self, shapetype):
        self.fitness = 0
        self.length = 100
        temp = primitive[shapetype]
        instanceOf = temp.__class__
        self.genes = [instanceOf() for i in range(self.length)]

    def calc_fitness(self, orig_arr):
        base = Image.new('RGB',(350,350), (0,0,0))
        for i in range(self.length):
            base = self.genes[i].draw(base)
        base_arr = np.array(base)
        self.fitness = -1*np.linalg.norm(orig_arr-base_arr)
        base.save('out.png')

class Population:

    def __init__(self):
        self.pop_size = 50
        self.individuals = [Individual(0) for i in range(self.pop_size)]

    def calculate_fitness(self, orig_arr):
        for i in range(self.pop_size):
            self.individuals[i].calc_fitness(orig_arr)
        self.individuals.sort(key = lambda x:x.fitness)
        self.max_fitness = self.individuals[self.pop_size-1].fitness

    #Tournament Selection Technique for selecting parents
    def selection(self):
        parents = []
        k = 2
        for i in range(2):
            idxs = random.sample(range(0, self.pop_size), k)
            idx = max(idxs)
            parents.append(copy.deepcopy(self.individuals[idx]))
        return parents

    #Add offspring to the population and throw away worst individual from population
    def changepopulation(self, offspring):
            self.individuals[0] = copy.deepcopy(offspring)


class Genetic:

    def __init__(self):
        original = Image.open('mona_orig.jpg')
        self.orig_arr = np.array(original)
        self.population = Population()
        self.population.calculate_fitness(self.orig_arr)
        self.parents = []
        iter = 0
        while iter<10000:
            iter+=1
            print('{}:'.format(iter))
            print('Max fitness of population:{}'.format(self.population.max_fitness))
            self.parents = self.population.selection()
            print('Before CrossOver')
            self.crossover()
            x = random.choice(range(1,11))
            if x<3:
                print('Mutating:')
                self.mutate()
            offspring = self.getfittestoffspring()
            self.population.changepopulation(offspring)
            self.population.calculate_fitness(self.orig_arr)
            
        print('Total Iterations:{}'.format(iter))
        
    def getfittestoffspring(self):
        for x in self.parents:
            x.calc_fitness(self.orig_arr)
        if self.parents[0].fitness >= self.parents[1].fitness:
            return self.parents[0]
        return self.parents[1]

    #Mutation by flipping one randomly selected bit
    def mutate(self):
        for i in range(100):
            x = random.randint(1,10)
            y = random.randint(1,10)
            if x<2:
                self.parents[0].genes[i].remake()
            if y<2:
                self.parents[1].genes[i].remake()

    #CrossOver using One Point CrossOver Technique
    def crossover(self):
        crossover_point = random.choice(range(1,100))
        self.parents[0].genes[0:crossover_point], self.parents[1].genes[0:crossover_point] = self.parents[1].genes[0:crossover_point], self.parents[0].genes[0:crossover_point]


def main():
    demo = Genetic()

if __name__=='__main__':
    main()
    



