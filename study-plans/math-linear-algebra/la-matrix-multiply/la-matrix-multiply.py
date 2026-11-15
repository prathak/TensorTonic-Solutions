import numpy as np

def matrix_multiply(A: list, B: list) -> np.ndarray:
    return np.array(A, dtype=float) @ np.array(B, dtype=float)