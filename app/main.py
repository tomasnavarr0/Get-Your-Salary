from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router


app = FastAPI(
    title="Salary Prediction API",
    description="Get your salary",
    version="1.0.0",
    contact={"name": "Nava", "email": "tomas.navarro@gmail.com"},
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
    responses={400: {"description": "Wrong request"}, 500: {"description": "Internal server error"}},
)
