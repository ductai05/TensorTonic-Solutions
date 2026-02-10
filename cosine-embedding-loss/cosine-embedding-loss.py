import numpy as np

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    
    x1, x2 = np.array(x1), np.array(x2)
    cos_x1_x2 = x1 @ x2 / (np.linalg.norm(x1) * np.linalg.norm(x2))
    L = 0
    if label == 1:
        L = 1 - cos_x1_x2
    elif label == -1:
        L = max(0, cos_x1_x2 - margin)
    return L