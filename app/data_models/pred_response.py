from pydantic import BaseModel


class PredictionResponse(BaseModel):
    prediction_log: float
    salary: float
    currency: str
    model_version: str
