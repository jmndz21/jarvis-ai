# Plan de construcción — 7 días

Cada día deja algo funcional que se puede probar. Marca las casillas a medida que avances.

## Día 1 — Base conversacional ✅ (scaffold inicial en este commit)
- [x] Estructura del proyecto y entorno virtual
- [x] Integración con la API de Claude (Anthropic)
- [x] Chat básico por consola con memoria de conversación
- [ ] Probar con tu propia API key (`ANTHROPIC_API_KEY` en `.env`)

## Día 2 — Voz
- [ ] Reconocimiento de voz (STT) con Whisper local
- [ ] Síntesis de voz (TTS) — ElevenLabs o Piper
- [ ] Palabra de activación ("Hey Jarvis") con OpenWakeWord/Porcupine
- [ ] Loop completo: escuchar → transcribir → responder → hablar

## Día 3 — Control del PC
- [ ] Function calling: el LLM elige qué acción ejecutar
- [ ] Abrir apps / ejecutar comandos del sistema
- [ ] Capturas de pantalla
- [ ] Control de mouse/teclado (`pyautogui`)
- [ ] Confirmación obligatoria antes de acciones destructivas (borrar, cerrar sin guardar, etc.)

## Día 4 — Correo
- [ ] OAuth con Gmail API
- [ ] Leer y resumir correos nuevos
- [ ] Clasificar/priorizar bandeja de entrada
- [ ] Redactar respuestas (con confirmación antes de enviar)

## Día 5 — Visión
- [ ] Captura de cámara con OpenCV
- [ ] Enviar frames a un modelo multimodal para describir la escena
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
