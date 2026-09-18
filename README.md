# Jarvis AI

Asistente de IA personal estilo Jarvis (Iron Man): habla contigo, te escucha, revisa tu correo, controla tu PC y puede "verte" con la cámara.

## Funciones planeadas

- **Voz**: palabra de activación ("Hey Jarvis"), reconocimiento de voz (STT) y síntesis de voz (TTS) natural.
- **Conversación**: LLM (Claude) con memoria de contexto entre sesiones.
- **Control del PC**: abrir apps, ejecutar comandos, mover archivos, capturas de pantalla, mouse/teclado — todo mediante function calling del LLM.
- **Correo**: leer, resumir, clasificar y redactar correos (Gmail API).
- **Visión**: captura de cámara, detección de objetos/rostros, descripción de lo que ve mediante un modelo multimodal.
- **Interfaz**: overlay/HUD simple para uso diario.

⚠️ El control del PC y el acceso a correo/cámara son funciones sensibles. El asistente pide confirmación antes de ejecutar acciones irreversibles (borrar archivos, enviar correos, etc.) y las credenciales nunca se guardan en el repositorio (usa `.env`, ignorado por git).

## Estado

Ver [TASKS.md](./TASKS.md) para el plan de construcción de 7 días y el progreso.

## Setup rápido

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # y completa tus API keys
python -m src.main
```

## Stack

- Python 3.11+
- LLM: Claude (Anthropic API) vía function calling
- STT: OpenAI Whisper (local)
- TTS: ElevenLabs o Piper (local)
- Wake word: OpenWakeWord / Porcupine
- Visión: OpenCV + modelo multimodal
- Correo: Gmail API (OAuth2)
- Control de PC: `pyautogui`, `subprocess`
