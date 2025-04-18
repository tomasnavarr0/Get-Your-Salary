import streamlit as st

# Configuración inicial de la página
st.set_page_config(page_title="Salary Predictor", page_icon="💰", layout="wide", initial_sidebar_state="expanded")

# --- Estilos CSS personalizados ---
st.markdown(
    """
<style>
    .st-emotion-cache-1y4p8pa {
        padding: 2rem 1rem 10rem;
    }
    .title {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .prediction-result {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        padding: 1rem;
        background-color: #e8f5e9;
        border-radius: 5px;
        margin-top: 1rem;
    }
</style>
""",
    unsafe_allow_html=True,
)
