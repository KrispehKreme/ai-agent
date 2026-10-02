## AI Agent Toolkit

**Run:** `uv run python main.py "<prompt>"`  
**Test:** `python3 -m pytest -q tests`  
**Deploy:** none

A small tool-calling AI coding agent, built as a study project. `main.py` sends a
user prompt to an LLM over the OpenRouter API and runs a loop (up to
`MAX_ITERATIONS` turns) where the model can call functions to inspect and edit
files, until it gives a final text answer. The system prompt driving that loop
(`prompts.py`) instructs the model to explore, diagnose, fix, and verify bugs
using the available functions -- never to just print a suggested fix.

### Main files
- `main.py`: CLI entry point; runs the prompt/tool-call loop against OpenRouter.
- `call_function.py`: dispatches a model tool call to the matching function in
  `functions/`. Every call is currently hardcoded to run with
  `working_directory="./calculator"`, so this agent, as wired up today, always
  operates on the `calculator/` subproject below, regardless of the prompt.
- `config.py`: `MAX_CHARS`, the read truncation limit used by `get_file_content`.
- `prompts.py`: the system prompt defining the agent's tool-use workflow.

### `functions/` -- the tools available to the model
- `get_files_info.py`: list a directory's contents with size/type info.
- `get_file_content.py`: read a file, truncated to `MAX_CHARS`.
- `get_file_size.py`: return a file's size in bytes.
- `write_file.py`: create or overwrite a file (creates missing parent dirs).
- `append_file.py`: append to an existing file; errors if it doesn't exist.
- `run_python_file.py`: execute a `.py` file with optional arguments.

All of these resolve paths under `working_directory` and reject any path that
escapes it.

### `calculator/` -- the sample project the agent operates on
A small command-line calculator: `calculator/main.py` parses an expression from
argv, `pkg/calculator.py` evaluates it, and `pkg/render.py` formats the result
as JSON. `tests.py` covers it.

### Tests
- `tests/`: pytest suite (`test_harness_baseline.py`) against the toolkit
  functions.
- Root-level `test_*.py` files: additional, separate tests for individual
  `functions/` modules (not under `tests/`, so a plain `pytest tests/` run
  will not collect them).

### Other
- `study_notes.txt`, `.aider.*`: development/study artifacts, not part of the
  toolkit itself.
