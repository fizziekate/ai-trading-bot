# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

Repository overview
- Minimal Python chat-bot CLI starter using a src/ layout (setuptools packaging).
- Single package: chatbot under src/chatbot.
- No third-party dependencies declared.

Common commands
- Environment
  - Requires Python 3.9+.
  - Create a virtual environment (Windows PowerShell):
    - python -m venv .venv
- Run (without installing the package)
  - python -m chatbot
  - One-off stdin mode: python -m chatbot --once
- Install locally (editable) to enable console script
  - python -m pip install -e .
  - Then you can run: chat-bot or chat-bot --once
- Build distribution artifacts (sdist and wheel)
  - python -m pip install -U build
  - python -m build

Linting and tests
- Linting/formatting: none configured in this repo.
- Tests: no test suite present.

High-level architecture
- Packaging and entry points
  - pyproject.toml defines a src layout (tool.setuptools.package-dir) and a console script: chat-bot = chatbot.cli:main.
  - python -m chatbot executes src/chatbot/__main__.py which imports and calls main().
- CLI flow (chatbot/cli.py)
  - main(argv=None) parses --once. Without --once, it starts interactive_loop().
  - interactive_loop() reads from stdin in a loop and prints responses from reply().
  - reply(message) is a simple rule-based responder; recognizes :help, :quit, greetings (hello/hi/hey), time, and name.

Important files
- README.md: Quickstart (venv creation; run with python -m chatbot). Notes that there are no third-party dependencies.
- pyproject.toml: project metadata, console script mapping, src layout.

Notes
- Extend behavior by editing src/chatbot/cli.py.
