import typing as th
import numpy as np
from sklearn.metrics.cluster import adjusted_rand_score, contingency_matrix


def purity(y, y_hat):
    cm = contingency_matrix(y, y_hat)
    return round(np.sum(np.amax(cm, axis=0)) / np.sum(cm), 3)


def adjusted_rand_index(y, y_hat) -> float:
    return round(adjusted_rand_score(y, y_hat), 3)


evaluation_functions = dict(purity=purity, adjusted_rand_index=adjusted_rand_index)


def evaluate(y, y_hat) -> th.Dict[str, float]:
    return {name: func(y, y_hat) for name, func in evaluation_functions.items()}
