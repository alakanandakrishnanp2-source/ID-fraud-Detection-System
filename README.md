# 🛡️ ID Document Forgery Detection System

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-orange)
![OCR](https://img.shields.io/badge/OCR-Tesseract-red)
![API](https://img.shields.io/badge/API-REST-blueviolet)

A prototype system designed to analyze uploaded **ID document images** and generate a **fraud risk assessment report** indicating whether the document appears genuine or suspicious.

The project demonstrates how **computer vision techniques and Optical Character Recognition (OCR)** can be used to detect potential tampering in identity documents.

---

# 📌 Project Overview

Identity verification plays an important role in many digital systems such as:

- Banking applications
- Online identity verification
- KYC systems
- Digital onboarding platforms

However, detecting **manipulated or forged ID documents** is a difficult task.

This project introduces a **prototype fraud detection service** that analyzes uploaded ID document images and evaluates the likelihood of tampering using multiple image analysis techniques.

The system generates a **fraud risk score and analysis report** based on the detected anomalies in the image.

---

# 🎯 Project Objective

The primary objectives of this project are:

- Accept ID document images through an API endpoint
- Validate the uploaded image format
- Perform image tampering analysis
- Extract text from the document using OCR
- Generate a structured fraud detection report

The goal is to demonstrate a **conceptual approach to image-based fraud detection using AI tools**.

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|--------|
| Python | Programming language |
| FastAPI | Backend API framework |
| Uvicorn | ASGI server for running the API |
| OpenCV | Image processing and computer vision |
| Pillow | Image validation |
| Pytesseract | OCR text extraction |
| NumPy | Numerical processing |
| Swagger UI | Interactive API testing interface |

---

# 🧠 Fraud Detection Techniques

The system performs several image analysis techniques to detect potential tampering.

## Blur Detection

Blur detection identifies whether the image is excessively blurred.  
Manipulated or edited images sometimes introduce blur artifacts.

## Edge Detection

Edge analysis evaluates the structure of edges in the image.  
Inconsistent or unnatural edges may indicate editing or manipulation.

## Error Level Analysis (ELA)

ELA is a digital image forensics technique that detects manipulated areas by analyzing compression differences within the image.

Edited regions typically have different compression levels compared to the rest of the image.

## OCR Text Extraction

Text is extracted from the document using **Tesseract OCR**, allowing the system to analyze visible information present in the ID document.

---

# 🏗️ System Architecture
