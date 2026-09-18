# Plan de construcción — 7 días

Cada día deja algo funcional que se puede probar. Marca las casillas a medida que avances.

**Decisiones tomadas:**
- SO objetivo: **Windows**
- LLM: **Ollama local (Llama 3.2)** — 100% gratis, sin API key, sin límites de uso ni internet
- Voz (TTS): **Piper, local y gratis** (nada de pago)
- Activación: **modo mixto** — wake word ("Hey Jarvis") + push-to-talk, con un comando/tecla para activar o desactivar la escucha continua en caliente
- API keys: **ninguna necesaria para el LLM, voz ni visión** (todo corre local vía Ollama). Solo el correo (Día 4) requiere credenciales, y son gratis.

## Credenciales a conseguir (en paralelo a los días de abajo)
- [ ] Instalar [Ollama](https://ollama.com) y descargar el modelo (`ollama pull llama3.2`) — necesario desde el Día 1, sin costo
- [ ] Proyecto en Google Cloud + credenciales OAuth de Gmail API (necesarias antes del Día 4; se puede dejar en modo "testing" con tu propia cuenta como usuario de prueba, no requiere verificación de Google, y es gratis)

## Día 1 — Base conversacional ✅ (scaffold inicial en este commit)
- [x] Estructura del proyecto y entorno virtual
- [x] Integración con Ollama (LLM local, gratis)
- [x] Chat básico por consola con memoria de conversación
- [ ] Instalar Ollama y descargar el modelo (`ollama pull llama3.2`), luego probar `python -m src.main`

## Día 2 — Voz
- [ ] Reconocimiento de voz (STT) con Whisper local
- [ ] Síntesis de voz (TTS) con Piper (local, sin API key)
- [ ] Palabra de activación ("Hey Jarvis") con OpenWakeWord (gratis, corre local)
- [ ] Modo push-to-talk como alternativa/respaldo (tecla para hablar sin depender del wake word)
- [ ] Comando de voz/atajo de teclado para activar o desactivar la escucha continua (privacidad: apagar el micrófono en segundo plano cuando quieras)
- [ ] Loop completo: escuchar → transcribir → responder → hablar

## Día 3 — Control del PC (Windows)
- [ ] Function calling: el LLM elige qué acción ejecutar
- [ ] Abrir apps / ejecutar comandos vía `subprocess` y `os.startfile`
- [ ] Gestión de ventanas con `pygetwindow` (enfocar, minimizar, cerrar)
- [ ] Capturas de pantalla
- [ ] Control de mouse/teclado (`pyautogui`)
- [ ] Confirmación obligatoria antes de acciones destructivas (borrar, cerrar sin guardar, etc.)

## Día 4 — Correo
- [ ] Crear proyecto en Google Cloud y habilitar Gmail API (si no se hizo antes)
- [ ] OAuth con Gmail API (token guardado localmente, fuera del repo)
- [ ] Leer y resumir correos nuevos
- [ ] Clasificar/priorizar bandeja de entrada
- [ ] Redactar respuestas (con confirmación antes de enviar)

## Día 5 — Visión
- [ ] Descargar un modelo multimodal en Ollama (ej. `ollama pull llama3.2-vision`)
- [ ] Captura de cámara con OpenCV
- [ ] Enviar frames al modelo multimodal local para describir la escena
- [ ] Detección básica de rostros/objetos
- [ ] Comando de voz tipo "Jarvis, ¿qué ves?"

## Día 6 — Interfaz y persistencia
- [ ] Overlay/HUD simple (ventana translúcida con estado del asistente)
- [ ] Memoria persistente entre sesiones (historial, preferencias)
- [ ] Manejo de errores y permisos por módulo (activar/desactivar voz, cámara, correo, control de PC)

## Día 7 — Pulido y demo
- [ ] Pruebas end-to-end de todos los módulos juntos
- [ ] Revisión de seguridad: API keys fuera del repo, confirmaciones en acciones sensibles
- [ ] Documentación de uso
- [ ] Grabación/demo final
