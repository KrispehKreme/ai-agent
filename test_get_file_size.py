import pytest

from functions.get_file_size import get_file_size


@pytest.fixture
def working_dir(tmp_path):
    return str(tmp_path)


def test_get_file_size_success(working_dir):
    content = "This is a test file."
    with open(f"{working_dir}/test.txt", "w") as f:
        f.write(content)

    result = get_file_size(working_dir, "test.txt")
    assert result == f'File "test.txt" is {len(content)} bytes.'


def test_get_file_size_path_escape(working_dir):
    result = get_file_size(working_dir, "../outside.txt")
    assert result.startswith("Error:")
    assert "outside" in result


def test_get_file_size_missing_file(working_dir):
    result = get_file_size(working_dir, "nonexistent.txt")
    assert result == 'Error: File not found or is not a regular file: "nonexistent.txt"'
