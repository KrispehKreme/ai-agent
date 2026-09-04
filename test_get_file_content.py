import pytest

from functions.get_file_content import get_file_content


@pytest.fixture
def working_dir(tmp_path):
    return str(tmp_path)


def test_get_file_content_success(working_dir):
    content = "This is a test file."
    with open(f"{working_dir}/test.txt", "w") as f:
        f.write(content)

    result = get_file_content(working_dir, "test.txt")
    assert result == content


def test_get_file_content_truncated(working_dir):
    content = "a" * 10500
    with open(f"{working_dir}/test.txt", "w") as f:
        f.write(content)

    result = get_file_content(working_dir, "test.txt")
    assert len(result) > 10000
    assert "[...File" in result


def test_get_file_content_path_escape(working_dir):
    result = get_file_content(working_dir, "../lorem.txt")
    assert "outside" in result


def test_get_file_content_missing_file(working_dir):
    result = get_file_content(working_dir, "nonexistent.txt")
    assert "not found" in result
