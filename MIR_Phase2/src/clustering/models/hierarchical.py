from sklearn.base import ClusterMixin, BaseEstimator
from sklearn.cluster import AgglomerativeClustering


class Hierarchical(ClusterMixin, BaseEstimator):
    def __init__(self, cluster_count: int):
        self.ac = AgglomerativeClustering(n_clusters=cluster_count)

    def fit_predict(self, x, **kwargs):
        return self.ac.fit_predict(x)
