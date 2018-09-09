import sys
from skimage import color,io, data
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from scipy import ndimage
import random
from scipy.spatial import Voronoi, voronoi_plot_2d
#import cv2
import matplotlib.pyplot as plt

img = Image.open(sys.argv[1])
rgb_img = np.array(img)

class Individual:

    def __init__(self, n, allPoint):
        self.fitness = 0
        self.create(n, allPoint)
        self.length = len(self.polygons)

    def calc_fitness(self):
        #draw image on canvas
        base = Image.new('RGB',(350,350), (0,0,0))
        global drw
        drw = ImageDraw.Draw(base,'RGB')
        x = 0
        for polygon in self.polygons:
            if polygon:
                coord = []
                for i  in range(len(polygon)):
                    coord.append(tuple(polygon[i]))
                color =tuple(self.colors[x])
                drw.polygon(coord, color, None)
            x+=1
        base.save('base.jpg')
        
        #calculate fitness
        base_arr = np.array(base)
        self.fitness = -1*np.linalg.norm(rgb_img-base_arr)

    def create(self,n, allPoint):
        #Step1: Create vornoi diagram
        selectedPoints = getFeatures(n,allPoint)
        vor = Voronoi(selectedPoints)

        #extract voronoi polygons
        self.polygons  = []
        flag = 1
        for region in vor.regions:
            polygon = []
            if -1 not in region:
                for i in region:
                    temp = vor.vertices[i]
                    temp = np.array(temp)
                    polygon.append(temp.astype(int))
                self.polygons.append(polygon)

        self.colors = []
        for polygon in self.polygons:
            if polygon:
                y = polygon[0][0]%350
                x = polygon[0][1]%350
                global color
                color = rgb_img[x][y]
                color = np.append(color, [1])
                self.colors.append(color)

            else:
                self.colors.append([])

class Population:

    def __init__(self, pop_size):
        self.pop_size = pop_size
        allPoint = imagePreProcessing()
        self.individuals = [Individual(500,allPoint) for i in range(self.pop_size)]

    def calculate_fitness(self):
        for i in range(self.pop_size):
            self.individuals[i].calc_fitness()
        self.individuals.sort(key = lambda x:x.fitness)
        self.max_fitness = self.individuals[self.pop_size-1].fitness

    '''def selection(self):
        parents = []
        for i in range(10):
            parents.append(copy.deepcopy(self.individuals[i+self.pop_size-10]))
        return parents

    def changepopulation(self, offspring):
        for i in range(10):
            self.individuals[i] = copy.deepcopy(offspring)
        self.individuals.sort(key = lambda x:x.fitness)
        self.max_fitness = self.individuals[self.pop_size-1].fitness'''


def imagePreProcessing():


    #Step 2: Get feature point

    #Step 2.1: greyscaling image to get the edges
    greyscaled = color.rgb2grey(rgb_img)
    
    #Step 2.2: Convolving image with filter to get edge
    filter = np.array([[1,1,1],
                       [0,0,0],
                       [-1,-1,-1]])
    convolved_image = ndimage.convolve(greyscaled,filter)
    convolved_image[convolved_image > 0.5] = 255.0
    convolved_image[convolved_image <= 0.5] = 0

    #returns points which could be part of sample
    return np.argwhere(convolved_image==0)

def getFeatures(n,allPoint):
    # n - number of points to select
    # Fetch points from convolved image for sampling

    # using Poisson Process to select random points

    # TO-DO: Use sobol or halton quasirandom process to select points or
    #        use adaptive mesh refinement to select points
    count = 0
    selectedPoints = []
    while len(allPoint) and count < n :
        inx = int(random.expovariate(1)*len(allPoint))%len(allPoint)
        selectedPoints.append(allPoint[inx])
        allPoint = np.delete(allPoint, inx, 0)
        count = count+1

    return selectedPoints


population = Population(100)
population.calculate_fitness()


