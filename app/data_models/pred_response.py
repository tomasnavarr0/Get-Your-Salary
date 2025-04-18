from pydantic import BaseModel


class PredictionResponse(BaseModel):
    prediccion_log: float
    salario_estimado: float
    moneda: str
    version_modelo: str
