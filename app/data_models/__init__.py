from pandas import DataFrame, Series
from numpy import ndarray

from .tech_roles import TechRole
from .pred_response import PredictionResponse
from .salary import SalaryRequest

Array = DataFrame | Series | ndarray

__all__ = ["TechRole", "Array", "PredictionResponse", "SalaryRequest"]
