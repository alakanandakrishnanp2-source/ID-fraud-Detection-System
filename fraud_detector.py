import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageChops, ImageEnhance

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def detect_blur(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    variance = cv2.Laplacian(gray, cv2.CV_64F).var()

    if variance < 100:
        return True

    return False
def detect_edges(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray,100,200)

    edge_ratio = np.sum(edges) / edges.size

    return edge_ratio

def perform_ela(image_path):

    original = Image.open(image_path).convert("RGB")

    temp_image = "temp.jpg"

    original.save(temp_image,"JPEG",quality=90)

    resaved = Image.open(temp_image)

    ela_image = ImageChops.difference(original,resaved)

    extrema = ela_image.getextrema()

    max_diff = max([ex[1] for ex in extrema])

    if max_diff == 0:
        max_diff = 1

    scale = 255.0 / max_diff

    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)

    return ela_image
def ela_score(image_path):

    ela_image = perform_ela(image_path)

    ela_array = np.array(ela_image)

    mean_value = np.mean(ela_array)

    return mean_value
def extract_text(image_path):

    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    return text
def analyze_document(file_path):

    image = cv2.imread(file_path)

    blur = detect_blur(image)

    edges = detect_edges(image)

    ela = ela_score(file_path)

    text = extract_text(file_path)

    return {

        "blur_detected": blur,
        "edge_score": float(edges),
        "ela_score": float(ela),
        "extracted_text": text

    }