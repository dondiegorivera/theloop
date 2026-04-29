"""theloop — closed agentic loop."""

from pathlib import Path

from dotenv import load_dotenv

# Load project-root .env once on package import, so subprocesses we spawn
# (pi, etc.) inherit the LiteLLM/provider keys from os.environ.
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

__version__ = "0.1.0"
