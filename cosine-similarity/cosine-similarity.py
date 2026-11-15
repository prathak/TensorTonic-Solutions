import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    na,nb = np.linalg.norm(a), np.linalg.norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return float(np.dot(a,b)/(na*nb))