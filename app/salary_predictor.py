import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from sqlmodel import SQLModel
from app.db.models import PredictModel
from app.data_models import PredictionResponse
from app.db import DBService
from typing import Any


class SalaryPredictor:
    def __init__(self):
        self.model = None
        self.metadata = None
        self.load_model()

    def load_model(self, model_path: str = "models/salary_pipeline_v3.pkl"):
        self.model = joblib.load(model_path)
        self.metadata = joblib.load(Path(model_path).parent / "metadata_v3.pkl")

    @staticmethod
    async def upsert_db(sql_model_data: SQLModel) -> None:
        db_service = DBService()
        await db_service.add_data(sql_model_data)

    async def predict(self, input_data: dict[str, Any]) -> PredictionResponse:
        df = pd.DataFrame([input_data])
        log_pred = self.model.predict(df)
        pred_model = PredictionResponse(
            prediction_log=float(log_pred[0]),
            salary=float(np.expm1(log_pred[0])),
            currency="ARS",
            model_version=str(self.metadata["model_version"]),
        )
        sql_model = PredictModel(**pred_model.model_dump())
        await self.upsert_db(sql_model)

        return pred_model
