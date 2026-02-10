import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    x = np.array(x)
    x_ReLU = np.array(np.maximum(0, x))
    if x_ReLU.shape == ():
        return x_ReLU.reshape(-1)
    return x_ReLU