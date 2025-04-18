from pydantic import BaseModel, ConfigDict, Field
from .enums import CompanySize, ContractType, SeniorityLevel, TechRole, ModalityType, Dedication


class SalaryRequest(BaseModel):
    dedicacion: Dedication
    contrato: ContractType
    cantidad_de_personas_en_tu_organizacion: CompanySize
    modalidad_de_trabajo: ModalityType
    seniority: SeniorityLevel
    marvin_rol: TechRole
    anos_de_experiencia: int = Field(ge=0, le=50)
    antiguedad_en_la_empresa_actual: int = Field(ge=0, le=50)
    anos_en_el_puesto_actual: int = Field(ge=0, le=50)
    cuantas_personas_tenes_a_cargo: int = Field(ge=0, le=1000)
    edad: int = Field(ge=18, le=70)

    model_config = ConfigDict(use_enum_values=True)
