import random
import copy
import numpy as np

from shape import *

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
