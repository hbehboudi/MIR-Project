from sklearn import svm
from sklearn.base import BaseEstimator, ClassifierMixin


class SVM(BaseEstimator, ClassifierMixin):
    def __init__(self, c):
        self.clf = svm.SVC(kernel='linear', C=c)

    def fit(self, x, y):
        self.clf.fit(x, y)
        return self

    def predict(self, x):
        return self.clf.predict(x)
