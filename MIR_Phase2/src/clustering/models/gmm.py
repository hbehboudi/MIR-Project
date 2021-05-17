from abc import ABCMeta
from sklearn.base import DensityMixin, BaseEstimator
from sklearn.mixture import GaussianMixture


class GMM(DensityMixin, BaseEstimator, metaclass=ABCMeta):
    def __init__(self, cluster_count: int, max_iteration: int):
        self.gm = GaussianMixture(n_components=cluster_count, max_iter=max_iteration)

    def fit(self, x):
        self.gm.fit(x)
        return self

    def predict(self, x):
        return self.gm.predict(x)
