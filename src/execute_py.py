import subprocess
import os
import traceback

def run_execute_script():
    # Define the path to the execute.py script
    script_path = os.path.join(os.path.expanduser("~"), "PycharmProjects", "automate_python_excel", "files",
                               "../files/execute.py")
    script_dir = os.path.dirname(script_path)

    try:
        # Change the working directory to the script's directory
        os.chdir(script_dir)

        # Run the execute.py script
        result = subprocess.run(["python", script_path], check=True, capture_output=True, text=True)
        print(f"Execution output: {result.stdout}")
        print(f"Execution errors: {result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the script: {e}")
        print(f"Return code: {e.returncode}")
        print(f"Output: {e.output}")
        print(f"Error output: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print(traceback.format_exc())

