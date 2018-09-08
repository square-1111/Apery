import random
import copy
import numpy as np
from Genetic_Evolution import *
from shape import *

class Main:

    def __init__(self):
        original = Image.open('mona_orig.jpg')
        self.orig_arr = np.array(original)
        Parameters.set(self.orig_arr)
        self.population = Population(pop_size=100, individual_size=50, shapetype=2)
        self.population.calculate_fitness(self.orig_arr)
        self.parents = []
        iter = 0
        while 1:
            iter+=1
            print('{}:'.format(iter))
            print('Max fitness of population:{}'.format(self.population.max_fitness))
            self.parents = self.population.selection()
            self.crossover()
            x = random.choice(range(1,11))
            if x<5:
                print('Mutating:')
                self.mutate()
            offspring = self.getfittestoffspring()
            self.population.changepopulation(offspring)
            
        print('Total Iterations:{}'.format(iter))
        
    def getfittestoffspring(self):
        

    def mutate(self):


    def crossover(self):
        

def main():
    demo = Main()

if __name__=='__main__':
    main()
    



