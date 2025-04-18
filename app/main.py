from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router
import logging
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Starting application...")
    yield
    logging.info("Shutting down application...")


app = FastAPI(
    title="Salary Prediction API",
    description="API para predecir salarios basados en características del empleado",
    version="1.0.0",
    contact={"name": "Nava", "email": "tomas.navarro@gmail.com"},
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["system"], include_in_schema=False)
async def health_check():
    return {"status": "ok"}


app.include_router(
    router,
    prefix="/api/v1",
    tags=["predictions"],
    responses={400: {"description": "Solicitud inválida"}, 500: {"description": "Error interno del servidor"}},
)
