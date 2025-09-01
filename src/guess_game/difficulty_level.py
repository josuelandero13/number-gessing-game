from enum import Enum


class DifficultyLevel(Enum):
    """Niveles de dificultad del juego."""

    EASY = ("fácil", 15)
    MEDIUM = ("medio", 10)
    HARD = ("difícil", 5)
    CUSTOM = ("personalizado", 0)

    def __init__(self, name: str, attempts: int):
        self.display_name = name
        self.default_attempts = attempts
