"""Día 2: reconocimiento de voz (STT), síntesis (TTS) y wake word.

Decisiones de diseño (ver TASKS.md):
- TTS: Piper, 100% local, sin API key.
- Activación mixta: wake word ("Hey Jarvis") + push-to-talk como respaldo.
- La escucha continua (wake word) se puede activar/desactivar en caliente
  vía toggle_wake_word(), sin reiniciar el proceso.

Pendiente de implementar:
- listen() -> str                  # graba audio (push-to-talk) y lo transcribe con Whisper local
- speak(text: str) -> None         # sintetiza con Piper y reproduce el audio
- wait_for_wake_word() -> None     # bloquea hasta escuchar "Hey Jarvis" (solo si está activo)
- toggle_wake_word(enabled: bool) -> None  # enciende/apaga la escucha continua
"""

wake_word_enabled = True


def toggle_wake_word(enabled: bool) -> None:
    global wake_word_enabled
    wake_word_enabled = enabled
