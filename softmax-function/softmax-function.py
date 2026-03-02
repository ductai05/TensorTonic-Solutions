import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    x = np.array(x)
    np_array_1d = False
    if len(x.shape) == 1:
        x = x.reshape(1, -1)
        np_array_1d = True

    exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
    softmax_x = exp_x / np.sum(exp_x, axis=1, keepdims=True)
    
    if np_array_1d:
        return softmax_x.reshape(-1)
    return softmax_x