## AI Agent Toolkit

This repository contains utilities for interacting with Proxmox hosts, containers, and systemd services. Key components:

### Main Files
- `main.py`: Entry point for the AI agent's core functionality
- `config.py`: Configuration settings for the agent
- `prompts.py`: Handles user interaction and prompt engineering
- `pyproject.toml`: Project configuration file
- `.gitignore`: Specifies untracked files
- `uv.lock`: Lock file for Python dependencies

### Functional Modules
- `functions/`: Contains utility functions:
  - File operations (read/write/append)
  - Python script execution
  - File information retrieval
  - Git repository interactions

### Calculator Subsystem
- `calculator/`: Implements a command-line calculator with:
  - Expression evaluation
  - JSON output formatting
  - CLI interface

### Testing
- `tests/`: Unit tests for all core functions

### Development
- `.venv/`: Python virtual environment
- `.ruff_cache/`: Ruff linter cache
- `study_notes.txt`: Development notes

This project provides a comprehensive toolkit for managing and monitoring Proxmox environments while supporting auxiliary tools like the calculator application.