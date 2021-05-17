import typing as th
import numpy as np


def calculate_matrix(expected, actual):
    expected = list(expected)
    actual = list(actual)

    c = np.array([[0, 0], [0, 0]], np.int32)

    for i in range(len(expected)):
        c[actual[i]][expected[i]] += 1

    return c


def accuracy(y, y_hat) -> float:
    matrix = calculate_matrix(y_hat, y)
    return (matrix[0][0] + matrix[1][1]) / (matrix[0][0] + matrix[1][1] + matrix[1][0] + matrix[0][1])


def f1(y, y_hat, pos):
    p = precision(y, y_hat, pos)
    r = recall(y, y_hat, pos)
    return 2 * p * r / (p + r)


def precision(y, y_hat, pos) -> float:
    matrix = calculate_matrix(y_hat, y)
    return (matrix[pos][pos]) / (matrix[0][pos] + matrix[1][pos])


def recall(y, y_hat, pos) -> float:
    matrix = calculate_matrix(y_hat, y)
    return (matrix[pos][pos]) / (matrix[pos][0] + matrix[pos][1])


evaluation_functions = dict(accuracy=accuracy, f1=f1, precision=precision, recall=recall)


def evaluate(y, y_hat) -> th.Dict[str, float]:
    return {name: func(y, y_hat) for name, func in evaluation_functions.items()}
