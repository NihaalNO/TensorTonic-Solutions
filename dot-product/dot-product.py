import numpy as np

def dot_product(x: list, y: list) -> float:
    result = []
    
    for i in range(len(x)):
        result.append( x[i] * y[i])
    
    return float(sum(result))
    pass