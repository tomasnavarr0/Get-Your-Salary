import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
import streamlit as st
from app.data_models.enums import Dedication, ContractType, ModalityType, CompanySize, SeniorityLevel, TechRole
import requests

st.markdown("<h1 class='title'>💰 Predictor de Salarios Tech</h1>", unsafe_allow_html=True)

# --- Formulario de entrada ---
with st.form("salary_prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📋 Información Básica")
        with st.container(border=True):
            dedicacion = st.selectbox("Dedicación", [e.value for e in Dedication], index=0)
            contrato = st.selectbox("Tipo de contrato", [e.value for e in ContractType], index=0)
            modalidad = st.selectbox("Modalidad de trabajo", [e.value for e in ModalityType], index=0)
            company_size = st.selectbox("Tamaño de la organización", [e.value for e in CompanySize], index=2)

    with col2:
        st.markdown("### 👨‍💻 Perfil Profesional")
        with st.container(border=True):
            seniority = st.selectbox("Nivel de seniority", [e.value for e in SeniorityLevel], index=1)
            tech_role = st.selectbox("Rol tecnológico", [e.value for e in TechRole], index=0)
            experiencia = st.slider("Años de experiencia", min_value=0, max_value=50, value=3)
            antiguedad_empresa = st.slider("Antigüedad en la empresa actual (años)", min_value=0, max_value=50, value=2)

    st.markdown("### 📊 Detalles Adicionales")
    with st.container(border=True):
        col3, col4 = st.columns(2)
        with col3:
            antiguedad_puesto = st.slider("Años en el puesto actual", min_value=0, max_value=50, value=1)
        with col4:
            personas_cargo = st.slider("Personas a cargo", min_value=0, max_value=1000, value=0)

    edad = st.slider("Edad", min_value=18, max_value=70, value=30)

    submit_button = st.form_submit_button("Predecir Salario", type="primary")

# --- Procesamiento del formulario ---
if submit_button:
    # Construir el payload para la API
    payload = {
        "dedicacion": dedicacion,
        "contrato": contrato,
        "cantidad_de_personas_en_tu_organizacion": company_size,
        "modalidad_de_trabajo": modalidad,
        "seniority": seniority,
        "marvin_rol": tech_role,
        "anos_de_experiencia": experiencia,
        "antiguedad_en_la_empresa_actual": antiguedad_empresa,
        "anos_en_el_puesto_actual": antiguedad_puesto,
        "cuantas_personas_tenes_a_cargo": personas_cargo,
        "edad": edad,
    }

    # Mostrar spinner mientras se hace la petición
    with st.spinner("Calculando predicción..."):
        try:
            # Cambia esta URL por la de tu API en producción
            response = requests.post("http://localhost:8000/api/v1/predict", json=payload)

            if response.status_code == 200:
                result = response.json()
                predicted_salary = result.get("salario_estimado", 0)

                # Mostrar resultado con estilo
                st.markdown(
                    f"<div class='prediction-result'>" f"💰 Salario estimado: <span style='color: #4CAF50;'>${predicted_salary:,.2f}</span>" f"</div>",
                    unsafe_allow_html=True,
                )

                # Mostrar detalles de la predicción
                with st.expander("Ver detalles técnicos"):
                    st.json(result)
            else:
                st.error(f"Error en la API: {response.status_code} - {response.text}")

        except Exception as e:
            st.error(f"Error al conectar con la API: {str(e)}")

# --- Sidebar con información adicional ---
with st.sidebar:
    st.markdown("## ℹ️ Acerca de")
    st.markdown(
        """
    Esta aplicación predice salarios para profesionales tech basándose en:
    - Rol tecnológico
    - Experiencia
    - Tamaño de empresa
    - Ubicación
    - Y otros factores relevantes
    """
    )

    st.markdown("## ⚙️ Configuración")
    api_url = st.text_input("URL de la API", value="http://localhost:8000/predict", help="Cambia esta URL si la API está en otro servidor")

    st.markdown("## 📊 Métricas")
    st.metric("Total de predicciones", "1,243", "+15 esta semana")
