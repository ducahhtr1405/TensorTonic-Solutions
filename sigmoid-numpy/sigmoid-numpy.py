import numpy as np
def x_sigmoid(x):
    x = np.array(x)
    return 1/(1 + np.exp(-x))

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    return x_sigmoid(x)