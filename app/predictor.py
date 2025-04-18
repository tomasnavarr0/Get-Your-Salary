import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from app.data_models import PredictionResponse
from typing import Any


class SalaryPredictor:
    def __init__(self):
        self.model = None
        self.metadata = None
        self.load_model()

    def load_model(self, model_path: str = "models/salary_pipeline_v1.pkl"):
        self.model = joblib.load(model_path)
        self.metadata = joblib.load(Path(model_path).parent / "metadata.pkl")

    def predict(self, input_data: dict[str, Any]) -> PredictionResponse:
        df = pd.DataFrame([input_data])
        log_pred = self.model.predict(df)

        return PredictionResponse(
            prediccion_log=float(log_pred[0]),
            salario_estimado=float(np.expm1(log_pred[0])),
            moneda="ARS",
            version_modelo=str(self.metadata["model_version"]),
        )
