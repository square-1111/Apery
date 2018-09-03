import sys
from skimage import color,io, data
import numpy as np
from scipy import ndimage
import random

import matplotlib.pyplot as plt


#Step 1 :Reading image
rgb_img = io.imread(sys.argv[1])

def imagePreProcessing():
    #Step 1.1: color conversion rgb to colorlab
    # lab = color.rgb2lab(img)
    # print(lab.shape)


    #Step 2: Get feature point

    #Step 2.1: greyscaling image to get the edges
    greyscaled = color.rgb2grey(rgb_img)

    #Step 2.2: Convolving image with filter to get edge
    filter = np.array([[1,0,-1],
                       [1,0,-1],
                       [1,0,-1]])
    convolved_image = ndimage.convolve(greyscaled,filter)
    convolved_image[convolved_image > 0] = 255.0

    #returns points which could be part of sample
    return np.argwhere(convolved_image>0)

def getFeatures(n):
    # n - number of points to select
    #Step3: Fetch points from convolved image for sampling
    allPoint = imagePreProcessing()

    # using Poisson Process to select random points

    # TO-DO: Use sobol or halton quasirandom process to select points or
    #        use adaptive mesh refinement to select points
    count = 0
    x_coor = []
    y_coor = []
    while len(allPoint) and count < n :
        inx = int(random.expovariate(1)*len(allPoint))%len(allPoint)
        inx = 4
        print("he {}".format(inx))
        print(allPoint[inx,0])
        # x_coor.append(allPoint[inx][0])
        # y_coor.append(allPoint[inx][1])
        allPoint = np.delete(allPoint, inx)
        count = count+1

    return x_coor, y_coor

def main():
    x_coord, y_coord = getFeatures(100)
    print(x_coord)

if __name__ == '__main__':
    main()
