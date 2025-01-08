import os
import yaml
from create_python import PythonProgramGenerator
from execute_py import run_execute_script

def load_api_key_and_generate_program(user_input):
    # Load the API key from variable.yaml
    yaml_path = os.path.join(os.path.expanduser("~"), "PycharmProjects", "Automate_Python_Using_LLM", "../variable.yaml")
    with open(yaml_path, 'r') as file:
        config = yaml.safe_load(file)
        api_key = config['api_key']

    generator = PythonProgramGenerator(api_key)

    program_code = generator.generate_program(user_input)

    file_path = os.path.join(os.path.expanduser("~"), "PycharmProjects", "Automate_Python_Using_LLM", "files",
                             "../files/execute.py")
    generator.save_program(program_code, file_path)

    # Call the run_execute_script function
    run_execute_script()


