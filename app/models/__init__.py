from pandas import DataFrame, Series
from numpy import ndarray

from .tech_roles import TechRole

Array = DataFrame | Series | ndarray

__all__ = [
    "TechRole",
    "Array"
]
