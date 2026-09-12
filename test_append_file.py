import pytest

from functions.append_file import append_file


@pytest.fixture
def working_dir(tmp_path):
    return str(tmp_path)


def test_append_file_success(working_dir):
    with open(f"{working_dir}/test.txt", "w") as f:
        f.write("Hello, ")

    result = append_file(working_dir, "test.txt", "world!")
    assert result == 'Successfully appended 6 characters to "test.txt"'
    with open(f"{working_dir}/test.txt") as f:
        assert f.read() == "Hello, world!"


def test_append_file_path_escape(working_dir):
    result = append_file(working_dir, "../outside.txt", "content")
    assert result.startswith("Error:")
    assert "outside" in result


def test_append_file_missing_file(working_dir):
    result = append_file(working_dir, "nonexistent.txt", "content")
    assert result == 'Error: File not found or is not a regular file: "nonexistent.txt"'
