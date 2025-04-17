from sklearn.base import BaseEstimator, TransformerMixin
from app.models import Array
from pandas import DataFrame
from numpy import array, ndarray
from typing_extensions import Self


class SeniorityTransformer(BaseEstimator, TransformerMixin):
    seniority_mapping: dict[str, int] = {"Junior": 1, "Semi-Senior": 2, "Senior": 3, "Manager or Above": 4}

    def fit(self, X: Array, y: Array | None = None) -> Self:
        return self

    def transform(self, X: Array) -> ndarray:
        if isinstance(X, DataFrame):
            values = X.iloc[:, 0].values
        else:
            values = X.flatten()

        result = array([self.seniority_mapping.get(x, 0) for x in values])
        return result.reshape(-1, 1)
