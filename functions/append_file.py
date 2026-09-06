'''Appends content to an existing file within the working directory. Returns an error if the file does not already exist (unlike write_file, it will not create it).'''

import os


def append_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file:
            return f'Error: Cannot append to "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_file, "a") as f:
            f.write(content)

        return f'Successfully appended {len(content)} characters to "{file_path}"'
    except Exception as e:
        return f"Error: {e}"

schema_append_file = {
    "type": "function",
    "function": {
        "name": "append_file",
        "description": "Appends content to an existing file within the working directory. Returns an error if the file does not already exist (unlike write_file, it will not create it).",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the file to append to, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "The content to append into the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}