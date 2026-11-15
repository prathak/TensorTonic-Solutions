import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    return float(np.sqrt(np.sum(np.subtract(x,y)**2)))