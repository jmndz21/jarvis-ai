import os

from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
JARVIS_MODEL = os.environ.get("JARVIS_MODEL", "claude-sonnet-5")
JARVIS_NAME = os.environ.get("JARVIS_NAME", "Jarvis")
