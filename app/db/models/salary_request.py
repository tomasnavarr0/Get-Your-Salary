from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class SalaryRequestModel(SQLModel, table=True):
    __tablename__ = "salary_requests"

    id: int | None = Field(default=None, primary_key=True)
    dedicacion: str
    contrato: str
    cantidad_de_personas_en_tu_organizacion: str
    modalidad_de_trabajo: str
    seniority: str
    marvin_rol: str
    anos_de_experiencia: int = Field(ge=0, le=50)
    antiguedad_en_la_empresa_actual: int = Field(ge=0, le=50)
    anos_en_el_puesto_actual: int = Field(ge=0, le=50)
    cuantas_personas_tenes_a_cargo: int = Field(ge=0, le=100)
    edad: int = Field(ge=18, le=70)
    date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    username: str | None = Field(default=None, nullable=True)
