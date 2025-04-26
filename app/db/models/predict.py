from sqlmodel import SQLModel, Field


class PredictModel(SQLModel, table=True):
    __tablename__ = "predictions"

    id: int | None = Field(default=None, primary_key=True)
    prediction_log: float = Field(nullable=False)
    salary: float = Field(nullable=False)
    currency: str | None = Field(nullable=True, default="ARS")
    model_version: str = Field(nullable=True)
