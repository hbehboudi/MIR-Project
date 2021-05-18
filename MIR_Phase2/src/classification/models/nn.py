from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.neural_network import MLPClassifier


class NeuralNetwork(BaseEstimator, ClassifierMixin):
    def __init__(self, alpha):
        self.clf = MLPClassifier(solver='lbfgs', alpha=alpha,
                                 hidden_layer_sizes=(5, 2), random_state=1)

    def fit(self, x, y):
        self.clf.fit(x, y)
        return self

    def predict(self, x):
        return self.clf.predict(x)
