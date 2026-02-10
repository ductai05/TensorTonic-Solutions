import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.array(x)
    sigmoid_x = 1 / (1 + np.exp(-x))
    swish_x = x * sigmoid_x
    return swish_x
