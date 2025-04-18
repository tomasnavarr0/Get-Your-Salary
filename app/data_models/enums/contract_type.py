from enum import Enum


class ContractType(str, Enum):
    STAFF = "Staff (planta permanente)"
    CONTRACTOR = "Contractor"
