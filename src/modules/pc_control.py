"""Día 3: control del PC (Windows) vía function calling del LLM.

Pendiente de implementar según TASKS.md:
- open_app(name: str) -> None        # subprocess / os.startfile
- run_command(command: str) -> str   # subprocess, con confirmación previa
- take_screenshot() -> str           # devuelve ruta del archivo guardado
- move_file(src: str, dst: str) -> None
- focus_window(title: str) -> None   # pygetwindow
- click(x: int, y: int) -> None      # pyautogui
- type_text(text: str) -> None       # pyautogui

Toda acción destructiva (borrar, sobrescribir, cerrar sin guardar) debe
pedir confirmación explícita antes de ejecutarse.
"""
