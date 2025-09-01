import sys
from typing import Dict, Optional, Tuple
from guess_game.difficulty_level import DifficultyLevel


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

        return GameUI.select_options()

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

    def select_options():
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
