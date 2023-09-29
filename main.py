from fastapi import FastAPI, UploadFile, File, Request
import uvicorn
import shutil
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

UPLOAD_DIR = Path() / 'uploads'

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"]
,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
@app.get("/")
async def root():
    return {"message": "Hello World"}
"""

@app.post("/uploadfile/")
async def create_upload_file(file_upload: UploadFile):
    data = await file_upload.read()
    save_to = UPLOAD_DIR / file_upload.filename
    with open(save_to, "wb") as f:
        f.write(data)
    return {"filename": file_upload.filename}
