import os

from dotenv import load_dotenv

load_dotenv()

JARVIS_MODEL = os.environ.get("JARVIS_MODEL", "llama3.2")
JARVIS_NAME = os.environ.get("JARVIS_NAME", "Jarvis")
