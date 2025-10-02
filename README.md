# chat-bot

A minimal Python chat bot CLI starter.

## Quickstart

- Ensure Python 3.9+ is installed.
- Create a virtual environment:
  - Windows PowerShell: `python -m venv .venv`
- Run the bot without installing (uses stdlib only):
  - `python -m chatbot`

## Project layout

```
chat-bot/
  src/
    chatbot/
      __init__.py
      __main__.py
      cli.py
  .gitignore
  pyproject.toml
  README.md
```

## Notes
- No third-party dependencies are required for this starter.
- You can later add integrations (e.g., LLM APIs) by expanding `chatbot/cli.py`.
