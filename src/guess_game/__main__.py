import sys
from guess_game.game import GuessGame
from guess_game.game_ui import GameUI
from guess_game.game_config import GameConfig


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
