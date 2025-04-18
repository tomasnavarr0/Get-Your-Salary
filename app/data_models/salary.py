from pydantic import BaseModel
from .enums import CompanySize, ContractType, SeniorityLevel, TechRole, ModalityType


class SalaryRequest(BaseModel):
    dedicacion: str
    contrato: ContractType
    cantidad_de_personas_en_tu_organizacion: CompanySize
    modalidad_de_trabajo: ModalityType
    seniority: SeniorityLevel
    marvin_rol: TechRole
    anos_de_experiencia: int
    antiguedad_en_la_empresa_actual: int
    anos_en_el_puesto_actual: int
    cuantas_personas_tenes_a_cargo: int
    edad: int
