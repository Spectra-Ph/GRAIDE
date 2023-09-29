from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from subprocess import run

UPLOAD_DIR_1 = Path("uploads_1")  # Define the first upload directory
UPLOAD_DIR_2 = Path("uploads_2")  # Define the second upload directory

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/uploadfile_1/")  # Endpoint for the first upload button
async def create_upload_file_1(file_upload: UploadFile):
    data = await file_upload.read()
    save_to = UPLOAD_DIR_1 / file_upload.filename
    with open(save_to, "wb") as f:
        f.write(data)
    return {"filename": file_upload.filename}

@app.post("/uploadfile_2/")  # Endpoint for the second upload button
async def create_upload_file_2(file_upload: UploadFile):
    data = await file_upload.read()
    save_to = UPLOAD_DIR_2 / file_upload.filename
    with open(save_to, "wb") as f:
        f.write(data)
    return {"filename": file_upload.filename}

@app.post("/grade")  # New endpoint to trigger grading
async def grade_files():
    try:
        # Assuming grading.py is in the same directory as main.py
        run(["python", "grading.py"])
        return {"message": "Grading initiated successfully"}
    except Exception as e:
        return {"error": str(e)}
