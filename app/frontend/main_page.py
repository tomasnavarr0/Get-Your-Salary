import sys
from pathlib import Path
from typing import Any
import streamlit as st
import requests  # type: ignore[import]
import asyncio

sys.path.append(str(Path(__file__).parent.parent.parent))
from app.data_models.enums import Dedication, ContractType, ModalityType, CompanySize, SeniorityLevel, TechRole
from app.db import DBService
from app.db.models import SalaryRequestModel


async def add_to_db(salary_request: dict[str, Any]) -> None:
    db_service = DBService()
    await db_service.add_data(salary_request)


st.set_page_config(page_title="💰 Get Tech Salary", page_icon="💻", layout="wide")


def show_header():
    # Usamos 3 columnas con diferentes proporciones
    col_logo, col_title, col_cafe = st.columns([2, 4, 2])

    with col_logo:
        st.image("app/frontend/images/gys_logo.png", width=250)

    with col_title:
        # Centramos el título con CSS
        st.markdown(
            """
            <div style="display: flex; align-items: center; justify-content: center; height: 100%;">
                <h1 style="margin: 0;">💰 Get Tech Salary</h1>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col_cafe:
        # Botón de Cafecito alineado a la derecha
        st.markdown(
            f'<div style="text-align: right;">'
            f'<a href="https://cafecito.app/tomasnavarro" target="_blank">'
            f'<img src="https://cdn.cafecito.app/imgs/buttons/button_5.png" alt="Comprarme un café" width="250">'
            f"</a></div>",
            unsafe_allow_html=True,
        )


show_header()

TECH_ROLE_DISPLAY_NAMES = {
    TechRole.FRONTEND: "Frontend",
    TechRole.BACKEND: "Backend",
    TechRole.FULL_STACK: "Full Stack",
    TechRole.DATA_SCIENTIST: "Data Scientist",
    TechRole.DATA_ANALYST: "Data Analyst",
    TechRole.DATA_ENGINEER: "Data Engineer",
    TechRole.DEVOPS: "DevOps",
    TechRole.QA: "QA",
    TechRole.OTHER: "Otro",
}

with st.form("salary_prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📋 Información Básica")
        with st.container(border=True):
            username = st.text_input("Nombre de usuario", placeholder="Ingresa tu nombre de usuario")
            dedicacion = st.selectbox("Dedicación", [e.value for e in Dedication], index=0)
            contrato = st.selectbox("Tipo de contrato", [e.value for e in ContractType], index=0)
            modalidad = st.selectbox("Modalidad de trabajo", [e.value for e in ModalityType], index=0)
            company_size = st.selectbox("Tamaño de la organización", [e.value for e in CompanySize], index=2)

    with col2:
        st.markdown("### 👨‍💻 Perfil Profesional")
        with st.container(border=True):
            seniority = st.selectbox("Nivel de seniority", [e.value for e in SeniorityLevel], index=1)
            tech_role = st.selectbox("Rol tecnológico", options=list(TECH_ROLE_DISPLAY_NAMES.values()), index=0)
            experiencia = st.slider("Años de experiencia", min_value=0, max_value=50, value=3)
            antiguedad_empresa = st.slider("Antigüedad en la empresa actual (años)", min_value=0, max_value=50, value=2)

    st.markdown("### 📊 Detalles Adicionales")
    with st.container(border=True):
        col3, col4 = st.columns(2)
        with col3:
            antiguedad_puesto = st.slider("Años en el puesto actual", min_value=0, max_value=50, value=1)
        with col4:
            personas_cargo = st.slider("Personas a cargo", min_value=0, max_value=50, value=0)

    edad = st.slider("Edad", min_value=18, max_value=70, value=30)

    submit_button = st.form_submit_button("Obtener Salario", type="primary")


if submit_button:
    role_mapping = {v: k for k, v in TECH_ROLE_DISPLAY_NAMES.items()}
    selected_role = role_mapping[tech_role]

    payload = {
        "username": username,
        "dedicacion": dedicacion,
        "contrato": contrato,
        "cantidad_de_personas_en_tu_organizacion": company_size,
        "modalidad_de_trabajo": modalidad,
        "seniority": seniority,
        "marvin_rol": selected_role.value,
        "anos_de_experiencia": experiencia,
        "antiguedad_en_la_empresa_actual": antiguedad_empresa,
        "anos_en_el_puesto_actual": antiguedad_puesto,
        "cuantas_personas_tenes_a_cargo": personas_cargo,
        "edad": edad,
    }
    salary_request = SalaryRequestModel(**payload)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(add_to_db(salary_request))
    loop.close()
    payload.pop("username")

    with st.spinner("Calculando Salario..."):
        try:
            response = requests.post("http://api:8000/api/v1/predict", json=payload)

            if response.status_code == 200:
                result = response.json()
                predicted_salary = result.get("salary", 0)

                st.markdown(
                    f"<div class='prediction-result'>" f"💰 Salario estimado: <span style='color: #4CAF50;'>${predicted_salary:,.2f}</span>" f"</div>",
                    unsafe_allow_html=True,
                )

                with st.expander("Ver detalles técnicos"):
                    st.json(result)
            else:
                st.error(f"Error en la API: {response.status_code} - {response.text}")

        except Exception as e:
            st.error(f"Error al conectar con la API: {str(e)}")
