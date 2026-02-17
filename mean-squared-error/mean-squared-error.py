import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    n=len(y_pred)

    if y_pred.shape != y_true.shape:
        return None
    
    res = 0
    
    for i in range(n):
        e = (y_pred[i]-y_true[i])**2
        res+=e
        
    error = (1/n)*res
    return error

