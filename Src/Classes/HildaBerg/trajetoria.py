import numpy as np

def archimedean_spiral(theta, a, b):
        r = a + b * theta
        x = (r * np.cos(theta)).astype(int) 
        y = (r * np.sin(theta)).astype(int)
        return [x, y]
    