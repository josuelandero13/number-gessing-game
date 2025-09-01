import pytest
from src.guess_game.__main__ import GuessGame, GameConfig


def test_game_initialization():
    """Test de inicialización del juego."""
    config = GameConfig(1, 100, 10)
    game = GuessGame(config)

    assert game.config == config
    assert game.secret_number is None
    assert game.attempts == 0
    assert not game.game_won


def test_start_new_game():
    """Test de inicio de nuevo juego."""
    config = GameConfig(1, 10, 5)
    game = GuessGame(config)
    secret = game.start_new_game()

    assert game.secret_number is not None
    assert 1 <= game.secret_number <= 10
    assert game.attempts == 0
    assert not game.game_won


def test_correct_guess():
    """Test de adivinanza correcta."""
    config = GameConfig(1, 10, 5)
    game = GuessGame(config)
    game.start_new_game()
    game.secret_number = 5  # Forzar número secreto

    result = game.make_guess(5)

    assert result["correct"] == True
    assert game.game_won == True
    assert game.attempts == 1


def test_incorrect_guess():
    """Test de adivinanza incorrecta."""
    config = GameConfig(1, 10, 5)
    game = GuessGame(config)
    game.start_new_game()
    game.secret_number = 5

    result = game.make_guess(3)  # Número menor

    assert result["correct"] == False
    assert result["hint"] == "higher"
    assert game.attempts == 1
    assert not game.game_won
