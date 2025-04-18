from enum import Enum


class ModalityType(str, Enum):
    REMOTE = "100% remoto"
    HIBRID = "Híbrido (presencial y remoto)"
    PRESENCIAL = "100% presencial"
