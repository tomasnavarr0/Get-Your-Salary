from pandas import DataFrame
from typing_extensions import Self
from sklearn.base import BaseEstimator, TransformerMixin
from app.models import Array


class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, columns: list[str]):
        self.columns = columns

    def fit(self, X: DataFrame, y: Array | None = None) -> Self:
        return self

    def transform(self, X: DataFrame) -> DataFrame:
        return X[self.columns].values
