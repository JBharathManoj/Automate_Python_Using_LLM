import openai

class PythonProgramGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_program(self, user_input):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """
                You are a python program expert you can give python program without any additional information along with all imports.
                use pandas.
                you will create some python program for the user to read csv and save as txt file.
                read csv just like r"input.csv" and save txt file just like r"output.txt"

                give me complete program end to end.
                don't include any print statements

                your job is to provide pure python code based on user input without any additional values.
                
                i need only python code without headder ```python ```
                
                I need ready to executable code with only python code without any comments or unwanted strings.
                """},
                {"role": "user", "content": user_input}
            ],
            temperature=0.5,
            max_tokens=1000
        )

        result = response.choices[0].message['content'].strip()
        return result

    def save_program(self, program_code, file_path):
        with open(file_path, "w") as file:
            file.write(program_code)


