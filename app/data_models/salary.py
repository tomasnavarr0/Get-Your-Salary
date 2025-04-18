from pydantic import BaseModel


class SalaryRequest(BaseModel):
    dedicacion: str
    contrato: str
    cantidad_de_personas_en_tu_organizacion: str
    modalidad_de_trabajo: str
    seniority: str
    marvin_rol: int
    anos_de_experiencia: int
    antiguedad_en_la_empresa_actual: int
    anos_en_el_puesto_actual: int
    cuantas_personas_tenes_a_cargo: int
    edad: int
