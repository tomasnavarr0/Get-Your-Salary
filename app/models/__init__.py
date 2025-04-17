from pandas import DataFrame, Series
from numpy import ndarray

from .tech_roles import TechRoles

Array = DataFrame | Series | ndarray

__all__ = [
    "TechRoles",
]