"""Día 1: chat por consola con Claude y memoria de conversación."""

import sys

from anthropic import Anthropic

from src.config import ANTHROPIC_API_KEY, JARVIS_MODEL, JARVIS_NAME

SYSTEM_PROMPT = (
    f"Eres {JARVIS_NAME}, un asistente de IA personal estilo Jarvis. "
    "Respondes de forma breve, directa y útil, en el idioma en que te hablen."
)


def main() -> None:
    if not ANTHROPIC_API_KEY:
        print("Falta ANTHROPIC_API_KEY. Copia .env.example a .env y completa tu clave.")
        sys.exit(1)

    client = Anthropic(api_key=ANTHROPIC_API_KEY)
    history: list[dict] = []

    print(f"{JARVIS_NAME} listo. Escribe 'salir' para terminar.\n")

    while True:
        user_input = input("Tú: ").strip()
        if user_input.lower() in {"salir", "exit", "quit"}:
            print(f"{JARVIS_NAME}: Hasta luego.")
            break
        if not user_input:
            continue

        history.append({"role": "user", "content": user_input})

        response = client.messages.create(
            model=JARVIS_MODEL,
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=history,
        )

        reply = "".join(
            block.text for block in response.content if block.type == "text"
        )
        print(f"{JARVIS_NAME}: {reply}\n")

        history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
