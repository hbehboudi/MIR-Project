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
    acc = (matrix[0][0] + matrix[1][1]) / (matrix[0][0] + matrix[1][1] + matrix[1][0] + matrix[0][1])
    return round(acc, 3)


def f1(y, y_hat, pos):
    p = precision(y, y_hat, pos)
    r = recall(y, y_hat, pos)
    return round(2 * p * r / (p + r), 3)


def precision(y, y_hat, pos) -> float:
    matrix = calculate_matrix(y_hat, y)
    pre = (matrix[pos][pos]) / (matrix[0][pos] + matrix[1][pos])
    return round(pre, 3)


def recall(y, y_hat, pos) -> float:
    matrix = calculate_matrix(y_hat, y)
    rec = (matrix[pos][pos]) / (matrix[pos][0] + matrix[pos][1])
    return round(rec, 3)


def f1_pos(y, y_hat):
    return f1(y, y_hat, 1)


def f1_neg(y, y_hat):
    return f1(y, y_hat, 0)


def precision_pos(y, y_hat) -> float:
    return precision(y, y_hat, 1)


def precision_neg(y, y_hat) -> float:
    return precision(y, y_hat, 0)


def recall_pos(y, y_hat) -> float:
    return recall(y, y_hat, 1)


def recall_neg(y, y_hat) -> float:
    return recall(y, y_hat, 0)


evaluation_functions = dict(accuracy=accuracy,
                            f1_pos=f1_pos, precision_pos=precision_pos, recall_pos=recall_pos,
                            f1_neg=f1_neg, precision_neg=precision_neg, recall_neg=recall_neg)


def evaluate(y, y_hat) -> th.Dict[str, float]:
    return {name: func(y, y_hat) for name, func in evaluation_functions.items()}
