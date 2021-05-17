import typing as th


def purity(y, y_hat) -> float:
    groups = {}

    for i in range(len(y_hat)):
        label = y_hat[i]
        if not groups.__contains__(label):
            groups[label] = []
        groups[label].append(i)

    pur_num = 0

    for group in groups.values():
        count = {}
        for y_index in group:
            label = y[y_index]
            if not count.__contains__(label):
                count[label] = 0
            count[label] += 1
        pur_num += max(count.values())

    return pur_num / len(y_hat)


def adjusted_rand_index(y, y_hat) -> float:
    # todo: for you to implement
    pass


evaluation_functions = dict(purity=purity, adjusted_rand_index=adjusted_rand_index)


def evaluate(y, y_hat) -> th.Dict[str, float]:
    """
    :param y: ground truth
    :param y_hat: model predictions
    :return: a dictionary containing evaluated scores for provided values
    """
    return {name: func(y, y_hat) for name, func in evaluation_functions.items()}
