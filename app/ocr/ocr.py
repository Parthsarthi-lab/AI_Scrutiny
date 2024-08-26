import pytesseract
from .preprocessing import enhance_image
import os

def ocr_process(image_path,doc_type):
    # Ensure the path is correctly formatted for Tesseract
    processed_image_path = enhance_image(image_path,doc_type)
    
    # Convert to a format compatible with Tesseract (use absolute path if needed)
    processed_image_path = os.path.abspath(processed_image_path)

    # Perform OCR
    text = pytesseract.image_to_string(processed_image_path, lang='eng')
    
    return text
