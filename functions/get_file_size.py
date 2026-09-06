'''Returns the size of a specified file within the working directory'''

import os

from config import MAX_CHARS

def get_file_size(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        file_size = os.path.getsize(target_file)
        return f'File "{file_path}" is {file_size} bytes.'
    except Exception as e:
        return f"Error: {e}"

schema_get_file_size = {
    "type": "function",
    "function": {
        "name": "get_file_size",
        "description": "Returns the size of a specified file within the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the file whose size should be returned, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}