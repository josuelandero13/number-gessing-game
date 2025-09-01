#!/usr/bin/env python3
"""Guess the Number Game - Juego de adivinanza de números."""

import random
import sys
from enum import Enum
from typing import Dict, List, Optional, Tuple


class DifficultyLevel(Enum):
    """Niveles de dificultad del juego."""

    EASY = ("fácil", 15)
    MEDIUM = ("medio", 10)
    HARD = ("difícil", 5)
    CUSTOM = ("personalizado", 0)

    def __init__(self, name: str, attempts: int):
        self.display_name = name
        self.default_attempts = attempts


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


class GameUI:
    """Interfaz de usuario del juego."""

    @staticmethod
    def show_welcome_message():
        """Mostrar mensaje de bienvenida y reglas."""
        print("🎯" + "=" * 50)
        print("🎯           GUESS THE NUMBER GAME")
        print("🎯" + "=" * 50)
        print("\n📋 REGLAS DEL JUEGO:")
        print("• Yo pensaré en un número secreto entre 1 y 100")
        print("• Tú debes adivinarlo en la menor cantidad de intentos")
        print("• Después de cada guess, te daré una pista")
        print("• ¡Buena suerte!\n")

    @staticmethod
    def select_difficulty() -> Tuple[DifficultyLevel, Optional[int]]:
        """Seleccionar nivel de dificultad."""
        print("🎮 SELECCIONA EL NIVEL DE DIFICULTAD:")
        for i, level in enumerate(DifficultyLevel, 1):
            if level != DifficultyLevel.CUSTOM:
                print(
                    f"{i}. {level.display_name.capitalize()} - {level.default_attempts} intentos"
                )

        print(f"{len(DifficultyLevel)}. Personalizado")

        while True:
            try:
                choice = input("\n👉 Elige una opción (1-4): ").strip()
                if not choice:
                    continue

                choice_int = int(choice)
                if 1 <= choice_int <= len(DifficultyLevel):
                    selected_level = list(DifficultyLevel)[choice_int - 1]

                    if selected_level == DifficultyLevel.CUSTOM:
                        custom_attempts = GameUI.get_custom_attempts()
                        return selected_level, custom_attempts
                    else:
                        return selected_level, None

                print("❌ Por favor, elige una opción válida (1-4)")

            except ValueError:
                print("❌ Por favor, ingresa un número válido")

    @staticmethod
    def get_custom_attempts() -> int:
        """Obtener número personalizado de intentos."""
        while True:
            try:
                attempts = input(
                    "👉 ¿Cuántos intentos deseas? (mínimo 3, máximo 20): "
                ).strip()
                if not attempts:
                    continue

                attempts_int = int(attempts)
                if 3 <= attempts_int <= 20:
                    return attempts_int
                else:
                    print("❌ El número de intentos debe estar entre 3 y 20")

            except ValueError:
                print("❌ Por favor, ingresa un número válido")

    @staticmethod
    def get_user_guess(attempt: int, max_attempts: int) -> int:
        """Obtener guess del usuario."""
        while True:
            try:
                prompt = f"💭 Guess #{attempt}/{max_attempts} → Introduce un número entre 1 y 100: "
                guess = input(prompt).strip()

                if not guess:
                    continue

                guess_int = int(guess)
                if 1 <= guess_int <= 100:
                    return guess_int
                else:
                    print("❌ El número debe estar entre 1 y 100")

            except ValueError:
                print("❌ Por favor, ingresa un número válido")
            except KeyboardInterrupt:
                print("\n\n👋 ¡Hasta luego! Gracias por jugar.")
                sys.exit(0)

    @staticmethod
    def show_guess_result(result: Dict):
        """Mostrar resultado del guess."""
        print(f"\n{'✅' if result['correct'] else '❌'} {result['message']}")
        if not result["correct"]:
            print(f"📊 Intentos restantes: {result['remaining_attempts']}")
        print("-" * 50)

    @staticmethod
    def show_game_over(secret_number: int, game_won: bool, attempts: int):
        """Mostrar mensaje de game over."""
        print("\n" + "=" * 50)
        if game_won:
            print(f"🏆 ¡GANASTE! Adivinaste en {attempts} intentos")
        else:
            print(f"😢 GAME OVER - El número era: {secret_number}")
        print("=" * 50)

    @staticmethod
    def ask_play_again() -> bool:
        """Preguntar si quiere jugar de nuevo."""
        while True:
            response = input("\n¿Quieres jugar de nuevo? (s/n): ").strip().lower()
            if response in ["s", "si", "sí", "y", "yes"]:
                return True
            elif response in ["n", "no", "q", "quit"]:
                return False
            else:
                print("❌ Por favor, responde 's' para sí o 'n' para no")


def main():
    """Función principal del juego."""

    GameUI.show_welcome_message()

    while True:
        # Seleccionar dificultad
        difficulty, custom_attempts = GameUI.select_difficulty()

        # Configurar juego
        config = GameConfig(
            min_number=1,
            max_number=100,
            difficulty=difficulty,
            custom_attempts=custom_attempts,
        )

        # Mostrar información de la partida
        level_name = difficulty.display_name.capitalize()
        attempts_info = config.max_attempts
        print(f"\n🎮 Modo: {level_name} - {attempts_info} intentos")
        print("🔢 Pensando en un número entre 1 y 100...")
        print("-" * 50)

        # Iniciar juego
        game = GuessGame(config)
        secret_number = game.start_new_game()

        # Bucle principal del juego
        while game.can_continue():
            try:
                # Obtener guess del usuario
                guess = GameUI.get_user_guess(game.attempts + 1, config.max_attempts)

                # Procesar guess
                result = game.make_guess(guess)
                GameUI.show_guess_result(result)

                # Verificar si ganó
                if result["correct"]:
                    break

            except KeyboardInterrupt:
                print("\n\n👋 ¡Hasta luego! Gracias por jugar.")
                sys.exit(0)
            except Exception as e:
                print(f"❌ Error inesperado: {e}")
                continue

        # Mostrar resultado final
        GameUI.show_game_over(secret_number, game.game_won, game.attempts)

        # Preguntar si quiere jugar de nuevo
        if not GameUI.ask_play_again():
            print("\n🎉 ¡Gracias por jugar! Hasta la próxima. 👋")
            break

        print("\n" + "=" * 50)
        print("🔄 INICIANDO NUEVA PARTIDA")
        print("=" * 50)


if __name__ == "__main__":
    main()
