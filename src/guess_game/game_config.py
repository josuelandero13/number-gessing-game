from typing import Optional
from guess_game.difficulty_level import DifficultyLevel


class GameConfig:
    """Configuración del juego."""

    def __init__(
        self,
        min_number: int = 1,
        max_number: int = 100,
        difficulty: DifficultyLevel = DifficultyLevel.MEDIUM,
        custom_attempts: Optional[int] = None,
    ):
        self.min_number = min_number
        self.max_number = max_number
        self.difficulty = difficulty
        self.max_attempts = (
            custom_attempts if custom_attempts else difficulty.default_attempts
        )
