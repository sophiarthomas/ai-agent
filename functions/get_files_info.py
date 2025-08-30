import os 
from config import MAX_CHARS

def get_files_info(working_directory, directory="."):
    target_dir = os.path.abspath(os.path.join(working_directory, directory))
    abs_working_dir = os.path.abspath(working_directory)
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir): 
        return f'Error: Directory "{directory}" is not a directory'
    try: 
        files_info = []
        for file in os.listdir(target_dir): 
            filepath = os.path.join(target_dir, file)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath) 
            files_info.append(
                f"- {file}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return '\n'.join(files_info)


    except Exception as e:
        return f"Error listing files: {e}"               

def get_file_content(working_directory, file_path): 
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)
    if not target_file.startswith(abs_working_dir): 
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file): 
        return f'Error: File not found or is not a regular file: "{file_path}"'
    with open(target_file, "r") as f: 
        file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) >= MAX_CHARS: 
            file_content_string += "[...File " + target_file + " truncated at " + str(MAX_CHARS) + " characters]"
    return file_content_string

def write_file(working_directory, file_path, content): 
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)
    if not abs_file_path.startswith(abs_working_dir): 
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path): 
        try: 
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        except Exception as e: 
            return f"Error: creating directory: {e}"
    if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'
    try: 
        with open(abs_file_path, "w") as f: 
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e: 
        return f'Error: writing to file {e}'
