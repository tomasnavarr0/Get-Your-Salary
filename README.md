# Predicción de Salarios IT

## Descripción
Aplicación de Data Science que estima el salario para roles de Tecnología de la Información (IT) en base a variables proporcionadas por el usuario. El modelo ha sido entrenado con datos reales de encuestas laborales y ofrece resultados en tiempo real.

## Características
- **Interfaz amigable**: formulario web para ingresar datos clave y ver la predicción al instante.  
- **API REST**: endpoint `/predict` para integrar fácilmente el servicio en otras aplicaciones.  
- **Modelo sólido**: pipeline de preprocesamiento + algoritmo de regresión.  
- **Contenedores Docker**: despliegue reproducible con Docker Compose.  
- **Código modular**: separación clara entre componentes de datos, entrenamiento, API y frontend.

## Tecnologías
- **Lenguaje**: Python 3.9+  
- **Librerías de ML**: scikit-learn, pandas, numpy, joblib  
- **Backend**: FastAPI  
- **Frontend**: Streamlit (o Flask)  
- **Contenerización**: Docker & docker-compose  
- **Control de versiones**: Git

## Requisitos previos
- Docker  
- Docker Compose  
- (Opcional) Python 3.9+ y entorno virtual

## Instalación y ejecución
1. Clona el repositorio:  
   ```bash
   git clone https://tu-repositorio/vanguard-chat.git
    ```
    
2. Contruit y levantar contenedores:
    ```bash
    docker-compose up --build
    ```
3. Accede a la aplicación
    - Frontend (Streamlit): [http://localhost:8501](http://localhost:8501)  
    - API REST (FastAPI Swagger UI): [http://localhost:8000/docs](http://localhost:8000/docs)
