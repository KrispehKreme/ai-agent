import os

import pytest

from functions.write_file import write_file


@pytest.fixture
def working_dir(tmp_path):
    return str(tmp_path)


def test_write_file_success(working_dir):
    result = write_file(working_dir, "test.txt", "This is a test file.")
    assert "Successfully wrote" in result


def test_write_file_path_escape(working_dir):
    result = write_file(working_dir, "/tmp/test.txt", "This is a test file.")
    assert "outside" in result


def test_write_file_directory(working_dir):
    os.makedirs(f"{working_dir}/test_dir")
    result = write_file(working_dir, "test_dir", "This is a test file.")
    assert "is a directory" in result
