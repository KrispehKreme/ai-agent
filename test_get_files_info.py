import pytest

from functions.get_files_info import get_files_info


@pytest.fixture
def working_dir(tmp_path):
    return str(tmp_path)


def test_get_files_info_success(working_dir):
    with open(f"{working_dir}/test.txt", "w") as f:
        f.write("This is a test file.")

    result = get_files_info(working_dir)
    assert "test.txt" in result
    assert "file_size=13 bytes" in result


def test_get_files_info_path_escape(working_dir):
    result = get_files_info(working_dir, "../")
    assert "outside" in result


def test_get_files_info_missing_directory(working_dir):
    result = get_files_info(working_dir, "nonexistent_dir")
    assert "not a directory" in result
