import numpy as np
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.base import BaseEstimator, ClassifierMixin


class NaiveBayes(BaseEstimator, ClassifierMixin):
    def __init__(self, kind):
        self.kind = kind

    def fit(self, X, y, **fit_params):
        X, y = check_X_y(X, y)
        self.priors_ = np.bincount(y) / len(y)
        self.n_classes_ = np.max(y) + 1

        self.means_ = np.array([X[np.where(y == i)].mean(axis=0) for i in range(self.n_classes_)])
        self.stds_ = np.array([X[np.where(y == i)].std(axis=0) for i in range(self.n_classes_)])

        return self

    def predict(self, X):
        check_is_fitted(self)
        X = check_array(X)

        res = self.predict_proba(X)

        return res.argmax(axis=1)

    def predict_proba(self, X):
        check_is_fitted(self)
        X = check_array(X)

        res = []
        for i in range(len(X)):
            probas = []
            for j in range(self.n_classes_):
                probas.append((1 / np.sqrt(2 * np.pi * self.stds_[j] ** 2) * np.exp(
                    -0.5 * ((X[i] - self.means_[j]) / self.stds_[j]) ** 2)).prod() * self.priors_[j])
            probas = np.array(probas)
            res.append(probas / probas.sum())

        return np.array(res)
