import numpy as np

def compute_cost_L2Norm(original, compared):
    orig = np.array(original)
    comp = np.array(compared)
    cost=0
    x,y,c = np.shape(orig)
    for i in range(c):
        for j in range(x):
            for k in range(y):
                cost += abs(int(orig[j][k][i])-int(ver[j][k][i]))**2
    
    return cost
