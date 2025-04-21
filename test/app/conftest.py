from polyfactory.factories.pydantic_factory import ModelFactory
import pytest
from app.salary_predictor import SalaryPredictor

from app.data_models import SalaryRequest


class SalaryRequestFactory(ModelFactory[SalaryRequest]):
    ...


@pytest.fixture
def salary_request() -> SalaryRequest:
    return SalaryRequestFactory.build()


@pytest.fixture
def salary_predictor() -> SalaryPredictor:
    return SalaryPredictor()
