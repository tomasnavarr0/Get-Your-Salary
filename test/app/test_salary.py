from app.data_models import SalaryRequest, PredictionResponse
from app.salary_predictor import SalaryPredictor


def test_salary_request(salary_predictor: SalaryPredictor, salary_request: SalaryRequest) -> None:
    prediction = salary_predictor.predict(salary_request.model_dump())
    assert isinstance(prediction, PredictionResponse)
    assert prediction.salary > 0
