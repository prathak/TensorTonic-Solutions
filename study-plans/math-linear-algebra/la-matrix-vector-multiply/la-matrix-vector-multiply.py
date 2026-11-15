import numpy as np

def matrix_vector_multiply(A: list, x: list) -> np.ndarray:
    return np.array(A, dtype=np.float64) @ np.array(x, dtype=np.float64)