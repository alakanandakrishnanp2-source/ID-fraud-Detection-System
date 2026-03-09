from fastapi import FastAPI, UploadFile, File
import shutil
import os

from image_validator import validate_image
from fraud_detector import analyze_document
from report_generator import generate_report

app = FastAPI()

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.post("/analyze-id/")


async def analyze_id(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    valid = validate_image(file_path)

    if not valid:
        return {"error": "Invalid Image Type"}

    analysis = analyze_document(file_path)

    report = generate_report(analysis)

    return report