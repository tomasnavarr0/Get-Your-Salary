from sklearn.base import BaseEstimator, TransformerMixin
from typing_extensions import Self
from pandas import DataFrame
from app.models import Array
from numpy import array, ndarray


class OrganizationSizeTransformer(BaseEstimator, TransformerMixin):
    size_mapping = {
        "1 (solamente yo)": 1,
        "De 2 a 10 personas": 6,  # promedio de 2 y 10
        "De 11 a 50 personas": 30,
        "De 51 a 100 personas": 75,
        "De 101 a 200 personas": 150,
        "De 201 a 500 personas": 350,
        "De 501 a 1000 personas": 750,
        "De 1001 a 2000 personas": 1500,
        "De 2001a 5000 personas": 3500,
        "De 5001 a 10000 personas": 7500,
        "Más de 10000 personas": 15000,
    }

    def fit(self, X: Array, y: Array | None = None) -> Self:
        return self

    def transform(self, X: Array) -> ndarray:
        if isinstance(X, DataFrame):
            values = X.iloc[:, 0].values
        else:
            values = X.flatten()

        result = array([self.size_mapping.get(x, 0) for x in values])
        return result.reshape(-1, 1)
