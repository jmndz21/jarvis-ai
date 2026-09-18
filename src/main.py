"""Día 1: chat por consola con Ollama (LLM local, gratis) y memoria de conversación."""

import sys

import ollama

from src.config import JARVIS_MODEL, JARVIS_NAME

SYSTEM_PROMPT = (
    f"Eres {JARVIS_NAME}, un asistente de IA personal estilo Jarvis. "
    "Respondes de forma breve, directa y útil, en el idioma en que te hablen."
)


def main() -> None:
    try:
        ollama.list()
    except Exception:
        print(
            "No se pudo conectar con Ollama. Instálalo desde https://ollama.com "
            "y asegúrate de que esté corriendo (el instalador lo deja como servicio en Windows)."
        )
        sys.exit(1)

    history: list[dict] = [{"role": "system", "content": SYSTEM_PROMPT}]

    print(f"{JARVIS_NAME} listo (modelo: {JARVIS_MODEL}). Escribe 'salir' para terminar.\n")

    while True:
        user_input = input("Tú: ").strip()
        if user_input.lower() in {"salir", "exit", "quit"}:
            print(f"{JARVIS_NAME}: Hasta luego.")
            break
        if not user_input:
            continue

        history.append({"role": "user", "content": user_input})

        try:
            response = ollama.chat(model=JARVIS_MODEL, messages=history)
        except ollama.ResponseError as e:
            if e.status_code == 404:
                print(
                    f"El modelo '{JARVIS_MODEL}' no está descargado. "
                    f"Corre: ollama pull {JARVIS_MODEL}"
                )
                sys.exit(1)
            raise

        reply = response["message"]["content"]
        print(f"{JARVIS_NAME}: {reply}\n")

        history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
