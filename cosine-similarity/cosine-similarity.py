import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    numerator = np.dot(a,b)
    denominator = np.linalg.norm(a) * np.linalg.norm(b)
    result = numerator/denominator
    if result == 0 :
        return 0.0
    elif np.isnan(result):
        return 0.0
    else:
        return float(result)
    