import numpy as np
from scipy.spatial import distance

def fitness(original, reproduced):
    original = np.array(original)
    reproduced = np.array(reproduced)
    return distance.euclidean(original, reproduced)
