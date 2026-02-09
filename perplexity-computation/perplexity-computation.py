def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    N = len(prob_distributions)
    H = 0
    for i in range(N):
        p_i = prob_distributions[i][actual_tokens[i]]
        H += math.log(p_i)

    H *= - 1 / N 
    PP = math.exp(H)
    return PP