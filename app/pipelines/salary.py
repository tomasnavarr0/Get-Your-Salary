from typing import Any
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from numpy import ndarray
from typing_extensions import Self
from sklearn.ensemble import RandomForestRegressor
from .df_selector import DataFrameSelector
from .transformers import SeniorityTransformer, OrganizationSizeTransformer
from app.data_models import Array
from pandas import DataFrame
from sklearn.feature_selection import SelectFromModel


class SalaryPredictionPipeline:
    """Pipeline completa para la predicción de salarios."""

    def __init__(self, model: Any | None = None):
        self.model = model
        self.pipeline: Pipeline | None = None
        self.categorical_columns: list[str] = [
            "dedicacion",
            "contrato",
            "cantidad_de_personas_en_tu_organizacion",
            "modalidad_de_trabajo",
            "seniority",
            "marvin_rol",
        ]
        self.numerical_columns: list[str] = [
            "anos_de_experiencia",
            "antiguedad_en_la_empresa_actual",
            "anos_en_el_puesto_actual",
            "cuantas_personas_tenes_a_cargo",
            "edad",
        ]
        self.target_column: str = "salario"

    def build_pipeline(self) -> Pipeline:
        numerical_pipeline = Pipeline([("selector", DataFrameSelector(self.numerical_columns)), ("scaler", StandardScaler())])

        categorical_basic_cols = ["dedicacion", "contrato", "modalidad_de_trabajo"]
        categorical_basic_pipeline = Pipeline(
            [("selector", DataFrameSelector(categorical_basic_cols)), ("encoder", OneHotEncoder(sparse_output=False))]
        )

        seniority_pipeline = Pipeline([("selector", DataFrameSelector(["seniority"])), ("transformer", SeniorityTransformer())])

        org_size_pipeline = Pipeline(
            [("selector", DataFrameSelector(["cantidad_de_personas_en_tu_organizacion"])), ("transformer", OrganizationSizeTransformer())]
        )

        preprocessor = ColumnTransformer(
            transformers=[
                ("numerical", numerical_pipeline, self.numerical_columns),
                ("categorical_basic", categorical_basic_pipeline, categorical_basic_cols),
                ("seniority", seniority_pipeline, ["seniority"]),
                ("org_size", org_size_pipeline, ["cantidad_de_personas_en_tu_organizacion"]),
            ],
            remainder="drop",
        )

        if self.model is not None:
            self.pipeline = Pipeline(
                [("preprocessor", preprocessor), ("feature_selection", SelectFromModel(estimator=RandomForestRegressor())), ("model", self.model)]
            )
        else:
            self.pipeline = Pipeline([("preprocessor", preprocessor)])

        return self.pipeline

    def fit(self, X: DataFrame, y: Array) -> Self:
        if self.pipeline is None:
            self.build_pipeline()

        if X.isna().any().any():
            print("Advertencia: El dataset tiene valores NaN. La pipeline intentará manejarlos.")

        self.pipeline.fit(X, y)
        return self

    def transform(self, X: DataFrame) -> ndarray:
        if self.pipeline is None:
            raise ValueError("La pipeline no ha sido construida o entrenada")

        return self.pipeline.transform(X)

    def predict(self, X: DataFrame) -> ndarray:
        if self.pipeline is None or self.model is None:
            raise ValueError("La pipeline completa con modelo no está disponible")

        return self.pipeline.predict(X)
