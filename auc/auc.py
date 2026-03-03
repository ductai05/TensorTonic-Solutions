import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    n = len(fpr)
    AUC = 0
    for i in range(0, n-1):
        AUC += (tpr[i]+tpr[i+1])*(fpr[i+1]-fpr[i]) * 1/2
    return AUC