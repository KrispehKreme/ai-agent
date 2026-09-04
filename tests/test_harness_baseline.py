"""Real assertions for the four tool functions, used as ground truth by
scripts/eval-local-model.sh (in the claude-daemon workspace) to grade
model-generated changes to this repo. Not part of ai-agent's own delegated
task set -- kept separate from the existing print-based test_*.py scripts on
purpose so "convert those to real assertions" remains available as a task.
"""
import os

import pytest

from config import MAX_CHARS
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file


@pytest.fixture
def workdir(tmp_path):
    (tmp_path / "sub").mkdir()
    (tmp_path / "hello.txt").write_text("hello world")
    (tmp_path / "sub" / "nested.txt").write_text("nested")
    (tmp_path / "script.py").write_text("print('ran')")
    return str(tmp_path)


def test_get_files_info_lists_entries(workdir):
    result = get_files_info(workdir, ".")
    assert "hello.txt" in result
    assert "sub" in result
    assert "is_dir=True" in result


def test_get_files_info_rejects_escape(workdir):
    result = get_files_info(workdir, "..")
    assert result.startswith("Error:")
    assert "outside" in result


def test_get_files_info_missing_dir(workdir):
    result = get_files_info(workdir, "nope")
    assert result.startswith("Error:")


def test_get_file_content_reads_file(workdir):
    assert get_file_content(workdir, "hello.txt") == "hello world"


def test_get_file_content_nested(workdir):
    assert get_file_content(workdir, "sub/nested.txt") == "nested"


def test_get_file_content_rejects_escape(workdir):
    result = get_file_content(workdir, "../etc/passwd")
    assert result.startswith("Error:")
    assert "outside" in result


def test_get_file_content_missing_file(workdir):
    result = get_file_content(workdir, "does_not_exist.txt")
    assert result.startswith("Error:")


def test_get_file_content_truncates(workdir):
    big = "x" * (MAX_CHARS + 500)
    (os_path := os.path.join(workdir, "big.txt"))
    with open(os_path, "w") as f:
        f.write(big)
    result = get_file_content(workdir, "big.txt")
    assert "truncated" in result
    assert len(result) < len(big) + 100


def test_write_file_creates_and_reports_length(workdir):
    result = write_file(workdir, "new.txt", "abc")
    assert "Successfully wrote" in result
    assert get_file_content(workdir, "new.txt") == "abc"


def test_write_file_creates_missing_parent_dirs(workdir):
    result = write_file(workdir, "deep/dir/new.txt", "abc")
    assert "Successfully wrote" in result
    assert get_file_content(workdir, "deep/dir/new.txt") == "abc"


def test_write_file_rejects_escape(workdir):
    result = write_file(workdir, "../escape.txt", "x")
    assert result.startswith("Error:")
    assert "outside" in result


def test_run_python_file_captures_stdout(workdir):
    result = run_python_file(workdir, "script.py")
    assert "STDOUT: ran" in result


def test_run_python_file_rejects_non_python(workdir):
    result = run_python_file(workdir, "hello.txt")
    assert result.startswith("Error:")


def test_run_python_file_missing_file(workdir):
    result = run_python_file(workdir, "nope.py")
    assert result.startswith("Error:")
