import numpy as np

def vector_norms(v: list) -> np.ndarray:
    l1_norm = float(np.sum(np.abs(v)))
    l2_norm = float(np.linalg.norm(v))
    inf_nprm = np.max(np.abs(v))

    return np.array([l1_norm, l2_norm, inf_nprm], dtype=float)