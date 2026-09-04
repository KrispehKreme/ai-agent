import pytest

from functions.run_python_file import run_python_file


@pytest.fixture
def working_dir(tmp_path):
    return str(tmp_path)


def test_run_python_file_success(working_dir):
    with open(f"{working_dir}/test.py", "w") as f:
        f.write("print('Hello, world!')")

    result = run_python_file(working_dir, "test.py")
    assert "Hello, world!" in result


def test_run_python_file_path_escape(working_dir):
    result = run_python_file(working_dir, "../test.py")
    assert "outside" in result


def test_run_python_file_missing_file(working_dir):
    result = run_python_file(working_dir, "nonexistent.py")
    assert "does not exist" in result


def test_run_python_file_non_python_file(working_dir):
    with open(f"{working_dir}/test.txt", "w") as f:
        f.write("This is a test file.")

    result = run_python_file(working_dir, "test.txt")
    assert "is not a Python file" in result
