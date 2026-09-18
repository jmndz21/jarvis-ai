# Jarvis AI

Asistente de IA personal estilo Jarvis (Iron Man): habla contigo, te escucha, revisa tu correo, controla tu PC y puede "verte" con la cámara.

## Funciones planeadas

- **Voz**: activación mixta — wake word ("Hey Jarvis") o push-to-talk, con la posibilidad de activar/desactivar la escucha continua en caliente. STT y TTS 100% locales (Whisper + Piper), sin API keys de voz.
- **Conversación**: LLM (Claude) con memoria de contexto entre sesiones.
- **Control del PC (Windows)**: abrir apps, ejecutar comandos, gestionar ventanas, mover archivos, capturas de pantalla, mouse/teclado — todo mediante function calling del LLM.
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

- Python 3.11+ (Windows)
- LLM: Claude (Anthropic API) vía function calling — también se usa para visión (es multimodal)
- STT: OpenAI Whisper (local)
- TTS: Piper (local, gratis, sin API key)
- Wake word: OpenWakeWord (local, gratis) + modo push-to-talk como respaldo
- Visión: OpenCV (captura) + Claude multimodal (descripción de escena)
- Correo: Gmail API (OAuth2)
- Control de PC: `pyautogui`, `pygetwindow`, `subprocess`
