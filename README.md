# 🎯 Guess the Number Game

Un juego clásico de adivinanza de números implementado en Python con interfaz de línea de comandos (CLI). ¡Adivina el número secreto en la menor cantidad de intentos!

## 🚀 Características

- **🎮 Tres niveles de dificultad**: Fácil (15 intentos), Medio (10 intentos) y Difícil (5 intentos)
- **🔧 Modo personalizado**: Elige tu propio número de intentos (3-20)
- **💡 Sistema de pistas inteligentes**: Te indica si el número es mayor o menor
- **📊 Seguimiento en tiempo real**: Ve tus intentos y oportunidades restantes
- **🔄 Juego infinito**: Juega tantas veces como quieras
- **🎨 Interfaz amigable**: Emojis y mensajes coloridos en español
- **✅ Validación robusta**: Manejo de inputs inválidos y errores

## 📋 Requisitos del Sistema

- **Python 3.13 o superior**
- **UV** (manejador de paquetes moderno) o **pip** tradicional

## 🛠️ Instalación

### Método Recomendado: Usando UV

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/guess-the-number-game.git
cd guess-the-number-game

# Instalar dependencias y configurar entorno
uv sync

# Instalar el juego en modo editable
uv pip install -e .
```

### Ejecutar el juego directamente
```bash
uv run python -m guess_game
```

## 🎨 Tecnologías Utilizadas

- Python 3.13.7: Lenguaje principal con type hints
- Click: Framework para aplicaciones CLI profesionales
- UV: Manejador de paquetes moderno y ultra rápido
- pytest: Framework de testing robusto
- pytest-cov: Reportes de cobertura de código
- Black & isort: Formateo automático de código
- Flake8: Linter para mantener calidad de código