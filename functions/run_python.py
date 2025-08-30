import os 
import subprocess

def run_python_file(working_directory, file_path, args=None):
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)
    if not abs_file_path.startswith(abs_working_dir): 
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path): 
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"): 
        return f'Error: "{file_path}" is not a Python file.'
    try: 
        commands = ["python3", abs_file_path]
        if args:  
            commands.extend(args)     
        complete_process = subprocess.run(
            commands, 
            capture_output=True, 
            timeout=30,
            cwd=abs_working_dir,
            text=True
            )
        output = []
        if complete_process.stdout: 
            output.append(f"STDOUT:\n{complete_process.stdout}")
        if complete_process.stderr: 
            output.append(f"STDERR:\n{complete_process.stderr}")
        if complete_process.returncode != 0: 
            output.append(f"Process exited with code {complete_process.stderr}")
        return "\n".join(output) if output else "No output produced."
    except Exception as e: 
        return f'Error: executing Python file: {e}'