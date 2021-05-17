import numpy as np
from sklearn.base import TransformerMixin, ClusterMixin, BaseEstimator


def euclidean_distance(vec_1, vec_2):
    distance = 0
    for i in range(len(vec_1)):
        distance += pow((vec_1[i] - vec_2[i]), 2)

    return np.sqrt(distance)


def _closest_centroid(sample, centroids):
    closest_i = None
    closest_distance = float("inf")
    for i, centroid in enumerate(centroids):
        distance = euclidean_distance(sample, centroid)
        if distance < closest_distance:
            closest_i = i
            closest_distance = distance
    return closest_i


def _get_cluster_labels(clusters, data):
    y_pred = np.zeros(np.shape(data)[0])
    for cluster_i, cluster in enumerate(clusters):
        for sample_i in cluster:
            y_pred[sample_i] = cluster_i
    return y_pred


class KMeans(TransformerMixin, ClusterMixin, BaseEstimator):
    def __init__(self, cluster_count=2, max_iter=10):
        self.k = cluster_count
        self.max_iterations = max_iter
        self.kmeans_centroids = []

    def _init_random_centroids(self, data):
        n_samples, n_features = np.shape(data)
        centroids = np.zeros((self.k, n_features))
        for i in range(self.k):
            centroid = data[np.random.choice(range(n_samples))]
            centroids[i] = centroid
        return centroids

    def _create_clusters(self, centroids, data):
        clusters = [[] for _ in range(self.k)]
        for sample_i, sample in enumerate(data):
            centroid_i = _closest_centroid(sample, centroids)
            clusters[centroid_i].append(sample_i)
        return clusters

    def _calculate_centroids(self, clusters, data):
        n_features = np.shape(data)[1]
        centroids = np.zeros((self.k, n_features))
        for i, cluster in enumerate(clusters):
            centroid = np.mean(data[cluster], axis=0)
            centroids[i] = centroid
        return centroids

    def fit(self, data):
        centroids = self._init_random_centroids(data)

        for _ in range(self.max_iterations):
            clusters = self._create_clusters(centroids, data)

            prev_centroids = centroids
            centroids = self._calculate_centroids(clusters, data)

            diff = centroids - prev_centroids
            if not diff.any():
                break

        self.kmeans_centroids = centroids
        return centroids

    def predict(self, data):
        clusters = self._create_clusters(self.kmeans_centroids, data)
        predicted_labels = _get_cluster_labels(clusters, data)
        return predicted_labels
