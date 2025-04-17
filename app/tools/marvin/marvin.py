import marvin
from .config import CLASSIFICATION_INSTRUCTIONS
from app.models import TechRole


class GetRole:
    def classify_data(self, text: str) -> TechRole:
        return marvin.classify(text, TechRole, instructions=CLASSIFICATION_INSTRUCTIONS)

    def classify_column(self, data_column: str) -> list[str]:
        return [self.classify_data(item).value for item in data_column]
