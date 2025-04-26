from fastapi import APIRouter
from app.salary_predictor import SalaryPredictor
from app.data_models import SalaryRequest
from app.data_models import PredictionResponse

router = APIRouter()
predictor = SalaryPredictor()


@router.post("/predict")
async def predict(request: SalaryRequest) -> PredictionResponse:
    return await predictor.predict(request.model_dump())
