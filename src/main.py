from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
import os
from backround_taks import load_api_key_and_generate_program

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), user_input: str = Form(...)):
    # Save the uploaded CSV file
    file_location = os.path.join(os.path.expanduser("~"), "PycharmProjects", "Automate_Python_Using_LLM", "files",
                                 "../files/input.csv")
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Execute the function with the provided user input
    load_api_key_and_generate_program(user_input)

    return {"info": "File and input processed successfully"}

@app.get("/download/")
async def download_file():
    file_path = os.path.join(os.path.expanduser("~"), "PycharmProjects", "Automate_Python_Using_LLM", "files", "output.txt")

    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename="output.txt")
    else:
        print(f"File not found at path: {file_path}")
        return {"error": "File not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=9900, reload=True)
