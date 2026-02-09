def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    n = len(rater1)
    p_o = sum(rater1[i] == rater2[i] for i in range (n)) / n

    unique_labels = set(rater1 + rater2)
    p_e = 0

    for label in unique_labels:
        p1 = rater1.count(label) / n
        p2 = rater2.count(label) / n
        p_e += p1 * p2
    # print(p_o, p_e)
    if p_e == 1:
        return 1.0
    return (p_o - p_e) / (1 - p_e)