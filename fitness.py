import numpy as np

#comparing original image with newly rendered image
#Using L2 norm
def calFitness(original, reproduced):
    return np.linalg.norm(original-reproduced)
