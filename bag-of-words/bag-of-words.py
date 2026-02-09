import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    vector = np.zeros(len(vocab), dtype=int)
    for i, word in enumerate(vocab):
        vector[i] = tokens.count(word)
    return np.array(vector)