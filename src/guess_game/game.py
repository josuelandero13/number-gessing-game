import random
from guess_game.game_config import GameConfig
from typing import Dict, List, Optional


class GuessGame:
    """Lógica principal del juego."""

    def __init__(self, config: GameConfig):
        self.config = config
        self.secret_number: Optional[int] = None
        self.attempts = 0
        self.game_won = False
        self.guess_history: List[int] = []

    def start_new_game(self) -> int:
        """Iniciar un nuevo juego."""

        self.secret_number = random.randint(
            self.config.min_number, self.config.max_number
        )
        self.attempts = 0
        self.game_won = False
        self.guess_history = []

        return self.secret_number

    def make_guess(self, guess: int) -> Dict:
        """Realizar un intento de adivinanza."""

        self.attempts += 1
        self.guess_history.append(guess)

        if guess == self.secret_number:
            self.game_won = True
            return {
                "correct": True,
                "message": f"¡Felicidades! ¡Adivinaste el número {self.secret_number}!",
                "attempts": self.attempts,
                "remaining_attempts": self.config.max_attempts - self.attempts,
            }
        elif guess < self.secret_number:
            return {
                "correct": False,
                "message": "El número es MAYOR que tu guess. ¡Intenta de nuevo!",
                "hint": "higher",
                "remaining_attempts": self.config.max_attempts - self.attempts,
            }
        else:
            return {
                "correct": False,
                "message": "El número es MENOR que tu guess. ¡Intenta de nuevo!",
                "hint": "lower",
                "remaining_attempts": self.config.max_attempts - self.attempts,
            }

    def can_continue(self) -> bool:
        """Verificar si el juego puede continuar."""
        return self.attempts < self.config.max_attempts and not self.game_won

    def get_game_status(self) -> Dict:
        """Obtener estado actual del juego."""
        return {
            "attempts": self.attempts,
            "remaining_attempts": self.config.max_attempts - self.attempts,
            "game_won": self.game_won,
            "guess_history": self.guess_history.copy(),
        }
