from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR


class SVM(BaseEstimator, ClassifierMixin):
    def __init__(self, c):
        self.c = c
        self.regr = make_pipeline(StandardScaler(), SVR(C=c, epsilon=0.2))

    def fit(self, x, y, **fit_params):
        self.regr.fit(x, y)
        return self

    def predict(self, x, y=None):
        return self.regr.predict(x)
